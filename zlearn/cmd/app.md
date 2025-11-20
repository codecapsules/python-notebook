### CMD

## create an env on the foldder.
py -m venv venv

## activate your env.
source venv/bin/activate

## See where python on your system is
which python

## Install/upgrade PIP.
pip install pip --upgrade

## Install Django on your env.
pip install django

## Freeze your installed libs on a file.
pip freeze > requirements.txt

## Install your libs from requirements on a fresh project.
pip install -r requirements.txt

## Create your django-admin core project.
django-admin startproject core .

## Create some apps.
py manage.py startapp [...]

## Create a migration.
py manage.py makemigrations

## Run migrations.
py manage.py migrate

## Run migrations.
py manage.py migrate

## Create a superuser.
py manage.py createasuperuser

## Launch a shell terminal.
py manage.py shell

