from flask_sqlalchemy import SQLAlchemy
from flask_app import app
from flask import Flask, render_template,request,session, redirect, url_for
from strgen import StringGenerator as SG
#Here I have used strgen to geneate random IDs for my customers

#The models need to be imported from manager before use for CRUD operations
from manager import db
from manager import Customer

#set secret key for the app in order to use sessions 
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

#routing the app to the login page.(In this case this is my starting page)
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
				session['username']=x #storing session variable
				return render_template('index.html')
    
		error = 'Invalid Credentials. Please try again.'    	
	return render_template('login.html', error=error)

#routing to createuser page
@app.route('/createuser',methods=['GET', 'POST'])
def createuser():
	if request.method=='POST':
		fn=request.form['field1']
		ln=request.form['field2']
		lid=request.form['field3']
		cno=request.form['field4']
		pwd=request.form['field5']
		x_list=[Customer.query.all()[i].loginid for i in range(len(Customer.query.all()))]
		c_id=SG("[\u\d]{9}").render()
		if(fn!='' and ln!='' and cno!='' and pwd!='' and (lid not in x_list)):
			a=Customer(id=c_id,first_name=fn,last_name=ln,loginid=lid,passwd=pwd,contact_num=cno)
			db.session.add(a)
			db.session.commit()
			return render_template('success.html')
		else:
			return 'Failure:credentials are not filled in properly'
	
	return render_template('createuser.html')

#Delete the session variable on logout
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))
