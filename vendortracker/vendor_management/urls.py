from django.urls import path
from . import views

urlpatterns = [
    # users login and signup URLs
    path('signup/',views.UserSignupView.as_view(), name='user-signup'),
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    
    # Vendors
    path('vendors/', views.VendorListCreateView.as_view(), name='vendor-list-create'),
    path('vendors/<int:pk>/', views.VendorRetrieveUpdateDestroyView.as_view(), name='vendor-detail'),

    # Purchase Orders
    path('purchase_orders/', views.PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('purchase_orders/<int:pk>/', views.PurchaseOrderRetrieveUpdateDestroyView.as_view(), name='purchase-order-detail'),
    
    # purchase acknowledged
    path('purchase_orders/acknowledge/<int:pk>/', views.PurchaseOrderRetrieveView.as_view(),name='purchase-acknowledge-order'),


    # Vendor Performance Evaluation
    path('vendors/<int:vendor_id>/initial-performance/', views.CreateInitialPerformanceMetricsView.as_view(), name='create_initial_performance_metrics'),
    path('vendors/<int:pk>/performance/', views.VendorPerformanceView.as_view(), name='vendor-performance'),
]
