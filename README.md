
### Reference to install Django
https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-20-04


### COMMANDS

Create a new environment project
```
python3 -m venv MY_VIRTUAL_ENV
```

Activate environment
```
source MY_VIRTUAL_ENV/bin/activate
```

Deactivate environment
```
deactivate
```

Create new project
```
django-admin startproject MY_PROJECT .
```

Execute project
```
python manage.py runserver
```

Create application
```
python manage.py startapp blog
python manage.py startapp portfolio
```

Format or create my model with Ctrl+Shift+i and format *Using Black*

After create models, need create migrations
```
python manage.py makemigrations
python manage.py migrate
```

Create superuser for my panel django (http://127.0.0.1:8000/admin/)
```
python manage.py createsuperuser
//After the command above, this is the configuration
Username (leave blank to use 'alexander'): admin    
Email address: 
Password: 
Password (again): 
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```


