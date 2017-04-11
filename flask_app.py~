from flask import Flask
import os
 
#define flask app
app=Flask(__name__)


from views import *
 
if __name__ == '__main__':
	app.config['DEBUG'] = True #helps you to see changes without re-running app
	port = int(os.environ.get("PORT", 8000)) #change the port no. if the one you are using is busy
	app.run(host='0.0.0.0', port=port)
	
