from django.shortcuts import render
from .models import Vendor,PurchaseOrder,HistoricalPerformance
from .serializers import VendorSerializer,PurchaseOrderSerializer,HistoricalPerformanceSerializer,UserSignupSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics,status
from rest_framework.views import APIView
from django.db.models import Avg
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
import json

User = get_user_model()

# Create your views here.

def calculate_on_time_delivery_rate(vendor):
    # print("vendor cal====",vendor)
    completed_pos = vendor.purchase_orders.filter(status='completed')
    # print("completed_pos",completed_pos)
    total_completed_pos = completed_pos.count()
    on_time_deliveries = completed_pos.filter(delivery_date__lte=timezone.now()).count()
    return on_time_deliveries / total_completed_pos if total_completed_pos > 0 else 0.0

def calculate_quality_rating_avg(vendor):
    completed_pos_with_rating = vendor.purchase_orders.filter(status='completed', quality_rating__isnull=False)
    return completed_pos_with_rating.aggregate(average_rating=Avg('quality_rating'))['average_rating'] or 0.0

def calculate_average_response_time(vendor):
    acknowledged_pos = vendor.purchase_orders.filter(status='acknowledged')
    total_acknowledged_pos = acknowledged_pos.count()
    if total_acknowledged_pos == 0:
        return 0.0
    total_response_time = sum((po.acknowledgment_date - po.issue_date).total_seconds() for po in acknowledged_pos)
    return total_response_time / total_acknowledged_pos

def calculate_fulfillment_rate(vendor):
    total_pos = vendor.purchase_orders.count()
    fulfilled_pos = vendor.purchase_orders.filter(status='completed').count()
    return fulfilled_pos / total_pos if total_pos > 0 else 0.0


class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer


class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer
    

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            'logged-in as':str(user.email),
            'refresh-token': str(refresh),
            'access-token': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
        
        
class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    

class VendorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class PurchaseOrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class CreateInitialPerformanceMetricsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, vendor_id):
        # print("vendor id: ", vendor_id)
        # print("request: ", request)
        vendor = Vendor.objects.get(pk=vendor_id)

        performance_metrics = {
            'on_time_delivery_rate': calculate_on_time_delivery_rate(vendor),
            'quality_rating_avg': calculate_quality_rating_avg(vendor),
            'average_response_time': calculate_average_response_time(vendor),
            'fulfillment_rate': calculate_fulfillment_rate(vendor),
        }

        # Create HistoricalPerformance instance with calculated metrics
        historical_performance = HistoricalPerformance.objects.create(
            vendor=vendor,
            on_time_delivery_rate=performance_metrics['on_time_delivery_rate'],
            quality_rating_avg=performance_metrics['quality_rating_avg'],
            average_response_time=performance_metrics['average_response_time'],
            fulfillment_rate=performance_metrics['fulfillment_rate']
        )
        serializer = HistoricalPerformanceSerializer(historical_performance)
        return Response({'message': 'performance metrics created successfully.',
                         'historical_performance':serializer.data,
                         })

class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = HistoricalPerformance.objects.all()
    # print("queryset====",queryset) 
    serializer_class = HistoricalPerformanceSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def retrieve(self, request, *args, **kwargs):
        # print("request====",request)
        instance = self.get_object()
        # print("instance------------",instance)
        vendor = instance.vendor
        # print("vendor------------",vendor)
        performance_metrics = {
            'on_time_delivery_rate': calculate_on_time_delivery_rate(vendor),
            'quality_rating_avg': calculate_quality_rating_avg(vendor),
            'average_response_time': calculate_average_response_time(vendor),
            'fulfillment_rate': calculate_fulfillment_rate(vendor),
        }

        serializer = self.get_serializer(data=performance_metrics)
        serializer.is_valid()
        return Response(serializer.data)

    
class PurchaseOrderRetrieveView(generics.RetrieveAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def post(self, request, *args, **kwargs):
        instance = self.get_object()

        # adding acknowledgment_date
        instance.acknowledgment_date = timezone.now()
        instance.save()
        serializer = self.get_serializer(instance)

        return Response({'message': 'Purchase order acknowledged successfully.',
                         'data':serializer.data
                         })
