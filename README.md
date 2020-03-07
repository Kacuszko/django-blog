# django-blog

<code>pip install django</code>

Create project folder:
<code>django-admin startproject django_project</code>

Go to project folder:
<code>cd django_project</code>

Create start app folder:
<code>python manage.py startapp blog</code>

First migrate:
<code>python manage.py migrate</code>

Create first admin user:
<code>python manage.py createsuperuser</code>

Run server:
<code>python manage.py runserver</code>

After every changes in database:
<code>python manage.py makemigrations</code>