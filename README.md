# django-rest-framework-deploy-heroku
Deploy Django REST API to Heroku

## Creating the Git repository
* git init 
* Create a file called `.gitignore` with the following content:
```
# See the name for you IDE
.vscode
# If you are using sqlite3
*.sqlite3
# Name of your virtuan env
.venv
*pyc
```
* git add .
* git commit -m 'First commit'

## Hidding instance configuration
* pip install python-decouple
* create an .env file at the root path and insert the following variables
- SECRET_KEY = Your$eCretKeyHere (Get this secrety key from the settings.py)
- DEBUG=True

### Settings.py
* from decouple import config
* SECRET_KEY = config('SECRET_KEY')
* DEBUG = config('DEBUG', default=False, cast=bool)

## Configuring the Data Base
* pip install dj-database-url

### Settings.py
* from dj_database_url import parse as dburl

default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=dburl),
}


## Static files 
pip install dj-static

### wsgi
* from dj_static import Cling
* application = Cling(get_wsgi_application())

### Settings.py
* STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

## Create a requirements-dev.txt
pip freeze > requirements-dev.txt

## Create a file requirements.txt file and include reference to previows file and add two more requirements
* -r requirements-dev.txt
* gunicorn
* psycopg2

## Create a file Procfile and add the following code
* web: gunicorn MyApi.wsgi --log-file -

## Create a file runtime.txt and add the following core
* python-3.7.10

## Creating the app at Heroku
  visit heroku website : https://dashboard.heroku.com/apps

## Setting the allowed hosts
* include your address at the ALLOWED_HOSTS directives in settings.py - Just the domain, make sure that you will take the protocol and slashes from the string

## You need to disable the collectstatic
* heroku config:set DISABLE_COLLECTSTATIC=1

## Publishing the app
* git add .
* git commit -m 'deploy the app'
* git push heroku master --force

## Creating the data base
* heroku run python3 manage.py migrate

## Creating the Django admin user
* heroku run python3 manage.py createsuperuser

