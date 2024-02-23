download the zip file
unzip the file and naviate to the folder in file explorer
open terminal in the unzipped path
follow along:



pip install virtualenv
virtualenv venv
source /venv/bin/activate
pip install -r requirements.txt
cd webproject

make sure there is a mysql server installed in the running machine and it is running.

make a database in the sql server with the command(strictly the same name):
create database somtu_events;
change the password in the setting.py file inthe webProject/webproject folder.
  |
  \/
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
