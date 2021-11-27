
Reference to install Django
https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-20-04


COMMANDS

Create a new environment project
```
python3 -m venv MY_PROJECT
```

Activate environment
```
source MY_PROJECT/bin/activate
```

Deactivate environment
```
deactivate
```

Create new project
```
django-admin startproject django_password_generator .
```

Execute project
```
python manage.py runserver
```