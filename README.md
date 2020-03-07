# django-blog

<code>pip install django</code>

<p>Create project folder:</p>
<code>django-admin startproject django_project</code>

<p>Go to project folder:
<code>cd django_project</code></p>

Create start app folder:<br>
<code>python manage.py startapp blog</code>

Initial migrate:<br>
<code>python manage.py migrate</code>

Create first admin user:<br>
<code>python manage.py createsuperuser</code>

Run server:<br>
<code>python manage.py runserver</code>

Make migration after every changes in database:<br>
<code>python manage.py makemigrations</code>
To see SQL code which will be run in migration:<br>
<code>python manage.py sqlmigrate blog 0001</code>
blog = app name<br>
0001 = migration number<br>
Then migrate it:<br>
<code>python manage.py migrate</code>