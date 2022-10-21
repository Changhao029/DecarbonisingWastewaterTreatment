# DecarbonisingWastewaterTreatment Web App:
## Content of Table
  - [Description](#description)
  - [Cloud Deployment](#clouddeployment)
  - [Local Deployment Document](#localdeployment)
  - [Future Features to improve this project](#futurefeature)
  - [User Manual](documents/User_Manual.md)
  - [API document](document/API_Document.md)
## Description <a name=description></a>
This web app:

Offer web-based interactive visualisations of the sensor data from WSP-based wastewater treatment plant;

Allow researcher or industry users to download data as csv file or the visualisations as png file for further analysis.
(https://teaching.csse.uwa.edu.au/units/CITS5206/cits5206projectsoffered2022.html)
### Technical Choice
- HTML + CSS + JavaScript
- Python 3.8
- Mysql
- Django Rest Framework
- Apache Echart(For data visualization)

## Cloud Deployment <a name=clouddeployment></a>
The current-version project has been deployed to AWS.

http://my5206projectfrontend.s3.ap-southeast-2.amazonaws.com/static/data_report.html


## Local Deployment Document <a name=localdeployment></a>
### 1. Install the pip3, Django, and environment
updata the apt

`sudo apt update `

`sudo apt upgrade`

install the pip3

`sudo apt install python3-pip`

install the Django

`pip3 install django`

install the python virtual environment

`sudo apt install python3-venv`

### 2. Deploy the code from the GitHub.
`git clone git@github.com:Changhao029/DecarbonisingWastewaterTreatment.git`

enter the project root directory

`cd DecarbonisingWastewaterTreatment`

create a virtual environment in the root directory

`python3 -m venv venv`

enter the virtual environment

`source ./venv/bin/activate`

install the requirements

`pip3 install -r requirements.txt`

### 3. Install the MySql
In the linux system, use the command to install mysql service.

`sudo apt-get install mysql-server`

Check if the mysql is installed successfully.

`mysql --version`

Change the password of the root user to 123456.

`sudo mysql`

`ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456'`

If you can enter mysql with the root name and the new password, 
you successfully change the password.

`mysql -u root -p`

Create the database named DecarbonisingWastewaterTreatment in mysql.

`create database DecarbonisingWastewaterTreatment;`

### 4. Run the project
After installing the mysql and creating the database, you can run the 
project in the virtual environment.

Enter the virtual environment.

`cd DecarbonisingWastewaterTreatment`

`source ./venv/bin/activate`

Database migration

`python3 manage.py makemigrations app`

`python3 manage.py migrate`

Run server

`python3 manage.py runserver 127.0.0.1:50003`

Import the test data in the database.
Open another terminal and type the command:

`curl -X POST 127.0.0.1:50003/fakedata/`

Then you can open the html page in the static directory with any browser.

### 5. Run the testing

In the project root directory, run this command to entre the virtual environment:

` source ./venv/bin/activate`

Next, run this command to run the unit testing case:

`python3 manage.py test`

[unit test code](#app/tests.py)

## Future Features to improve this project <a name=futurefeature></a>
1. Noticed with the rainfall graph, if user select a date period to show e.g., 
1/12 – 29-12, on the x-axis when it plots it just numbers the day from the first date, 
rather than listing the date. Again, from a user point of view, 
it would be more valuable to have the date as the label on the x-axis when displaying this daily rainfall data. 
Same thing applies for the humidity graph.

2. The download function and loading every chart function can be changed to asynchronous task, 
which can prevent the risk of timeout caused by large amount of data, and improve the user experience.
