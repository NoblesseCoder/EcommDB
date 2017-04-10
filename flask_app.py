from flask import Flask
import os
 
app=Flask(__name__)


from views import *
 
if __name__ == '__main__':
	app.config['DEBUG'] = True
	port = int(os.environ.get("PORT", 8000))
	app.run(host='0.0.0.0', port=port)
	
