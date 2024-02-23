download the zip file<br>
unzip the file and naviate to the folder in file explorer<br>
open terminal in the unzipped path<br>
follow along:<br>



pip install virtualenv <br>
virtualenv venv <br>
source /venv/bin/activate <br>
pip install -r requirements.txt <br>
cd webproject <br>

make sure there is a mysql server installed in the running machine and it is running.<br>

make a database in the sql server with the command(strictly the same name):<br>
create database somtu_events;<br>
change the password in the setting.py file inthe webProject/webproject folder.<br>
  |<br>
  \/<br>
python manage.py createsuperuser<br>
python manage.py makemigrations<br>
python manage.py migrate<br>
python manage.py runserver<br>
