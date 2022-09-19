# DecarbonisingWastewaterTreatment

## Local Deployment Document
### 1. Install the pip3, Django, and environment
updata the apt

`sudo apt updata `

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

### Run the project
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

`curl 127.0.0.1:50003/fakedata/`

Then you can open the html page in the static directory with any browser.