from flask_sqlalchemy import SQLAlchemy
from flask_app import app
from flask import Flask, render_template,request

from manager import db
from manager import Customer


@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		x=request.form['username']
		x_list=[Customer.query.all()[i].loginid for i in range(len(Customer.query.all()))]
		if x in x_list:
			z=Customer.query.filter_by(loginid=x).all()[0].passwd
			if(request.form['password']!=z):
				error = 'Invalid Credentials. Please try again.'
			else:
				return render_template('index.html')
    
		error = 'Invalid Credentials. Please try again.'    	
	return render_template('login.html', error=error)


#z=Customer.query.filter_by(loginid='admin').all()[0].passwd
	