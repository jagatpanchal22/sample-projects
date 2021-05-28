#Django REST API
##Order Management example
###Getting started
1. Have python3 installed
2. Initialize a new virtual environment: python3 -m venv env
3. Activate your virtual env: source venv/bin/activate
4. Install the project dependencies: pip install -r requirements.txt
5. Install postgres, create a DB and replace the configurations in Django settings.
6. Got inside the project directory.
7. Apply migrations: python3 manage.py migrate
8. Create superuser : python3 manage.py createsuperuser
9. Start the local server: python3 manage.py runserver

###ENDPOINTS
1. GET, POST: /company 
2. GET, PUT, DELETE: /company/str:company_id
3. GET, POST: /company/str:company_id/orders
4. GET, PUT, DELETE: /company/str:company_id/orders/str:order_id
5. GET, POST: /order
6. GET, PUT, DELETE: /order/str:order_id
7. GET, POST: /user
8. GET, PUT, DELETE: /user/str:user_id
9. /admin