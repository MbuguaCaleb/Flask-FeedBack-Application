**Flask feedback App**

```
Lerning to build a Python WebApp in flask.
Which will connect to a database, submit formdata and send
an email using SMTP
It is deployed in Heroku
Application will also be able to send an email...

```

**_Fundamentals_**

```
(a)How to use MailTrap.io EMail Client

It is a great service for development which gives your application a place
to send emails before you create an email client..



(b)Deploying a flask app/python application to Heroku

Once we delpoy we are going to create a production database


You must have a heroku account so as to deploy your application into Heroku


(c)App uses postgres as our DBMS!!


```

**Basic Commands(Notes)**

```
(a)Installing a virtual environment with PIP ENV..!

(python package manager pip)


sudo pip install pipenv

Virtual enviroment works such that when we install packages they get installed in our virtual environment instead of the global sytem.



(b)Running the virtual environment

(pipenv shell)
This command activates the virtual environment and creates a pipev file where all packages are stored


(c)An ORM is like an abstract layer to work with our database ..an example is flask-sqlalchmey(ORM Enable us work  with models)

```

**PROJECT PACKAGES**

```

pipenv install flask

pipenv install psycopg2

pipenv install psycopg2-binary

pipenv install flask-sqlalchemy

pipenv install gunicorn

```

**Important**

```
Selecting the correct interpreter...

(shift+ctrl+p) and select python intepreter.

```

**Folder structure**

```
(a)app.py -The entry point of the application.


(b)app.debug has been set to true since we are in development and we want the app to keep reloading
It is  more like nodemon in nodeJS!!

```
