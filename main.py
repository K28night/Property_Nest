from flask import *
from public import public
from admin import admin
import os
app=Flask(__name__) 
# initializes the Flask application. The app object is used to define routes, set configurations, and run the server.

# it will create instance of Flask class


# app.config['UPLOAD_FOLDER']=picfolder
# it will set the path for the static folder where images will be uploaded
app.config['SECRET_KEY']='28784'

app.register_blueprint(public)
app.register_blueprint(admin)

app.run(debug=True)
