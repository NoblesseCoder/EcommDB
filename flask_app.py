from flask import Flask
 
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tatsuya:shiba@localhost/flask_app' 

from views import *
 
if __name__ == '__main__':
	app.config['DEBUG'] = True
	app.run()