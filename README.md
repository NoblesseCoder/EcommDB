# EcommDB
EcommDB is an E-commerce Database driven by a Flask(Python) based web application.I made this as a part of my DBMS
mini-project where we were asked to build an application so as to demonstrate the interacion of a web-application with a relational database and to perform some basic CRUD operations on the database.

I haven't used sessions in this project but the real functionality would require them.In this project I simulated sessions using
references alone.  

### The database chosen in this project is postgresql.I have used flask-sqlalchemy(an ORM) on top of it.you would have to make the neccesary changes in code if you use a different ORM or database.


## Installations required(Linux(Ubuntu) users)-

1. pip install Flask
or sudo pip install Flask
2. pip install Flask-Migrate
3. pip install psycopg2
4. pip install flask-sqlalchemy

Other basic reqirements can be seen from the requirements.txt file.

## Setting up postgresql

Once postgres is installed in the machine.
login to postgres-
sudo su postgres
Then enter psql to enter psql prompt.

Follow the following commands to set up a database with user access.

1. CREATE USER username with PASSWORD 'passwd';
2. CREATE DATABASE db_name;
3. GRANT ALL PRIVILEGES ON DATABASE db_name to username;

This will set up a database with a user and password for external applications to access the database.You will require the username,database name and the password to set up the flask app to querry from the database 

## File Structure-

### 1.flask_app.py
This python file is the main app that starts the local host and thus the application itself.
### 2.views.py
This python file contains the code for ruting of the app to different references and also rendering of HTML files.
This also contains the interactions with the database.

The code in views.py could be put in flask_app.py itself.
I have done this split up for a better understanding of different functionalities.
### 3.manager.py
You could call this as models.py.This file contains the classes of all the relational models of your database.
### 4.migrations
This is a result of flask migrate.It is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic. The database operations are made available through the Flask command-line interface or through the Flask-Script extension.
### 5.static
This folder contains all the static files like images and the css stylesheets.
### 6.templates
This directory contains all the HTML files that need to be rendered.
