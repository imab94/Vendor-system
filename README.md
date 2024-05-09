## Step 1:
   1. Download zip code of vendor system in your local machine.
   2. create virtual env using this command

            python -m venv name_of_env
      
   4. Install the requirements.txt file inside your virtualenv.
   5. go to project directory i.e. vendortracker.
   6. Run this command to make the local sever (Django Server) live.

            python manage.py runserver

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
   **Get Purchase Order List.**  
   paste this url into Postman with GET request to get all Purchase Order Lists.
   - make sure you have added Authorization as key and Bearer Token as value.

           http://127.0.0.1:8000/api/purchase_orders/

## Step 9:
   **Get details of a Purchase Order.**  
   paste this url into Postman with GET request to get detail of a Purchase Order.
   - make sure you have added Authorization as key and Bearer Token as value.

           http://127.0.0.1:8000/api/purchase_orders/1/


## Step 10:
   **create a Purchase Order.**  
   paste this url into Postman with POST request to create a Purchase order.
   
      http://127.0.0.1:8000/api/purchase_orders/
      
   - make sure you have added Authorization as key and Bearer Token as value and JSON demo Data in body.

         {
          "po_number": "PO346789",
          "items": [
              {
                  "name": "Item6",
                  "description": "Description of Item6",
                  "quantity": 14,
                  "price": 150
              },
              {
                  "name": "Item7",
                  "description": "Description of Item7",
                  "quantity": 2,
                  "price": 80
              }
          ],
          "quantity": 8,
          "issue_date": "2024-05-01T12:00:00Z",
          "vendor": 1
         }

## Step 11:
   **make acknowledgement of a purchase order.**
   paste this url into postman and make sure you have added Bearer Token as Authorization Token.

      http://127.0.0.1:8000/api/purchase_orders/acknowledge/1/


## Step 12:
   **make initial performance of vendors**
   paste this url into postman and make sure you have added Bearer Token as Authorization Token.

         http://127.0.0.1:8000/api/vendors/3/initial-performance/

## Step 13:
   **get performace of a specific vendor like on_time_delivery,quality_rating_avg,average_response_time,full_fillment_rate.**
   paste this url into postman and make sure you have added Bearer Token as Authorization Token.


      http://127.0.0.1:8000/api/vendors/1/performance/       #for vendor 1
