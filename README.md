## Step 1:
   Install the requirements.txt file in your virtualenv.

## Step 2:
   Some demo data are already stored in Default database sqlite3.

## Step 3 (Optional):
   **For Signup new Account**  
   Paste this URL into Postman:  
   
    http://127.0.0.1:8000/api/signup/
   
   Include JSON data with fields like email, name, password, mobile_number, age.

## Step 4:
   **For Login to an existing account.**  
   User email and password:  
   - Email: test@example.com  
   - Password: test@1234  
   Paste this URL into Postman:  
   
    http://127.0.0.1:8000/api/login/ 
  
  You will get refresh-token and access-token.

## Step 5:
   **Get Vendors List**  
   paste this url into Postman with GET request to get all vendors.
   - make sure you have added Authorization as key and Bearer Token as value.

           http://127.0.0.1:8000/api/vendors/


## Step 6:
   **create a Vendor**  
   paste this url into Postman with POST request to create a vendor.
   
      http://127.0.0.1:8000/api/vendors/
      
   - make sure you have added Authorization as key and Bearer Token as value and JSON demo Data in body.


           {
          "name": "Vendor3",
          "contact_details":"364647474",
          "address":"India Delhi",
          "vendor_code":"Vendor786868"
          }

## Step 7:
   **Get Details of a Vendor**  
   paste this url into Postman with GET request to get details of a vendor.
   
      http://127.0.0.1:8000/api/vendors/1/


## Step 8:
   **Get Purchase Order List**  
   paste this url into Postman with GET request to get all Purchase Order Lists.
   - make sure you have added Authorization as key and Bearer Token as value.

           http://127.0.0.1:8000/api/purchase_orders/

## Step 9:
   **Get details of a Purchase Order**  
   paste this url into Postman with GET request to get detail of a Purchase Order.
   - make sure you have added Authorization as key and Bearer Token as value.

           http://127.0.0.1:8000/api/purchase_orders/1/


## Step 10:
   **Get details of a Purchase Order**  
   paste this url into Postman with GET request to get detail of a Purchase Order.
   - make sure you have added Authorization as key and Bearer Token as value.

           http://127.0.0.1:8000/api/purchase_orders/1/

      
   
