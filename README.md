# AnotherDeliveryApp
A Delivery App



## How to use

### Setting Up Development Server (Virtual Environment)

 - Clone the project using `git clone` command.
 - Type `cd AnotherDeliveryApp`
 - If virtualenv is not installed, run sudo apt-get install pipenv followed by:
	`pipenv install | pipenv shell (Ubuntu / Mac)`
 - Run `python manage.py migrate`.
 - Run `python manage.py collectstatic`
 - Install Postgres
 - Create a user in postgresql with username `postgres` and password `password`.
 - Create a database in postgresql with name `servfect`,
 - Create a superuser with the command `python manage.py createsuperuser`.
 - Start the server using `python manage.py` runserver 
 - Visit `http://localhost:8000/admin`
 - Create Users(Customers and Delivery Agent) and Set their GeoLocation.
 - Use Postman to send request to the server
 - Get the token of user from `127.0.0.1:8000/api-token-auth/` by sending the correct username and password
 - Post the pickup point's coordinates and the Authorization token to the `127.0.0.1:8000/delivery` page . 
 - If a driver is free and is closest to the Pickup point, they would be automatically assigned the delivery. 

