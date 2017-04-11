# EcommDB
EcommDB is an E-commerce Database driven by a Flask(Python) based web application.

EcommDB allows you to buy products online and make safe payments to the suppliers(also chose from different suppliers).You also have anoption of tracking down your order.(Security functionality is dummy in this project as for now.)

I made this as a part of my DBMS mini-project where we were asked to build an application so as to demonstrate the interacion of a web-application with a relational database and to perform some basic CRUD operations on the database.

### The database chosen in this project is postgresql.I have used flask-sqlalchemy(an ORM) on top of it.You would have to make some changes in code if you use a different ORM or database.


## Installations required(Linux(Ubuntu) users)-

    pip install Flask
      or sudo pip install Flask
    pip install Flask-Migrate
    pip install psycopg2
    pip install flask-sqlalchemy

Other basic reqirements can be seen from the requirements.txt file.

## Setting up postgresql

Once postgres is installed in the machine.
login to postgres-
sudo su postgres
Then enter psql to enter psql prompt.

Follow the following commands to set up a database with user access.

    CREATE USER username with PASSWORD 'passwd';
    CREATE DATABASE db_name;
    GRANT ALL PRIVILEGES ON DATABASE db_name to username;

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

#### Useful Commands-

    python manager.py db init
    python manager.py db migrate
    python manager.py db upgrade

The app has to be configured to interact with the database before any further operations.You can configure it as follows-

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/database_name'

(1) adds migration folder to the repository.Track records of all the migrations are kept in this folder.
(2)Generating initial migrations.
(3)The third command is to apply the migration to the database.

Each time the database models change repeat the migrate and upgrade commands.

### 5.static
This folder contains all the static files like images and the css stylesheets.
### 6.templates
This directory contains all the HTML files that need to be rendered.
