
# CAB BOOKING PROBLEM

### Problem Statement
We want to build a cab booking platform to allow a rider to book a cab.

### Details:
1. The location is represented as a (x, y) coordinate.  
2. Distance between two points (x1, y1) and(x2, y2) is sqrt((x1-x2)^2 + (y1-y2)^2)  
3. Platform has decided upon maximum distance a driver has to travel to pickup a rider.  
4. A cab has only 1 driver.  
5. Sharing of cab is not allowed between riders  
6. There is a single type of cab   

### Please build an application that exposes following features to riders and drivers.
1. Register a rider.  
2. Register a driver/cab  
3. Update a cab's location  
4. A driver can switch on/off his availability  
5. A rider can book a cab  
6. Fetch history of all rides taken by a rider.  
7. End the Trip  

### expectation
1. Demonstrable code is first expectation. To do this, you can choose any interface you are comfortable with - CLI, WebApp, MobileApp, APIs or even simply run the code via Tests or a main method.  
2. Code should be extensible.
3. Clean professional level code.
4. Functional Completeness including good modelling.
5. User Identification but not authentication.
6. Backend Database is optional. However modelling should be complete.

-------

# Solution
Clone this repository and run the code.

### Requirement:
 - Django 2.3
 - Python 3
 - MySQL 5.7
 - Postman

### Setup
- Create a [virtual environment](https://www.pythoncircle.com/post/404/virtual-environment-in-python-a-pocket-guide/) with Python 3. Activate it.  
- Install dependencies from requirements.txt file
- Clone code.   
- Create database. Migrate.  
- Run server.   
- Use postman collection to test endpoints.  

### Curl requests to test endpoints

#### Register a rider
```
curl --location --request POST 'localhost:8000/rider/register/' \
--form 'mobile=3434343434' \
--form 'email=rider1@yopmail.com' \
--form 'name=rider1' \
--form 'address=noida'
```

#### Register a driver
```
curl --location --request POST 'localhost:8000/driver/register/' \
--form 'mobile=666666661' \
--form 'vehicle_number=dl2can3333' \
--form 'name=driver3' \
--form 'address=Delhi'
```

#### Updating location and availability
```
curl --location --request POST 'localhost:8000/cab/location/update/' \
--form 'driver_id=1' \
--form 'x=20' \
--form 'y=10' \
--form 'is_available=True'
```

#### Book cab
```
curl --location --request POST 'localhost:8000/rider/cab/book/' \
--form 'rider_id=1' \
--form 'x=10' \
--form 'y=20'
```
-------

- [Host your Django Applications for free](https://www.pythoncircle.com/post/18/how-to-host-django-app-on-pythonanywhere-for-free/)
- [DigitalOcean vs PythonAnyWhere](https://www.pythoncircle.com/post/705/aws-ec2-vs-pythonanywhere-vs-digitalocean-for-hosting-django-application/)
