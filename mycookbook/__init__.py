import os
from flask import Flask
from flask_pymongo import PyMongo
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
# Config Settings & Environmental Variables located in env.py
app.config['MONGODB_NAME'] = "MyCookBook"
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)
'''
The following import has to be at the bottom of the file,
as it need to import routes after the app ha been initialised
to prevents circular imports.
'''
from mycookbook import routes
