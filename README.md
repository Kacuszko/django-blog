# django-blog
Blog created in Django

## Getting started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

```
pip install django
```
```
pip install django-crispy-forms
```

### Installing

A step by step series of examples that tell you how to create project from base.

Create project folder:
```
django-admin startproject django_project
```

Go to project folder:
```
cd django_project
```

Create start app folder:
```
python manage.py startapp blog
```

Initial migrate:
```
python manage.py migrate
```

Create first admin user:
```
python manage.py createsuperuser
```

Run server:
```
python manage.py runserver
```

### Make migration after every change in database:
To make migration:
```
python manage.py makemigrations
```

To see SQL code which will be run in migration:
```
python manage.py sqlmigrate blog 0001
```
WHERE blog is app name, 0001 is migration number

Then migrate it:
```
python manage.py migrate
```