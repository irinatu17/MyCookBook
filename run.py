import os
from flask import Flask, render_template, url_for, flash, redirect
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
   import env


app = Flask(__name__)
# Config Settings & Environmental Variables located in env.py
app.config['MONGODB_NAME'] = os.environ.get('MONGODB_NAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)

# MongoDB Collections
users_coll = mongo.db.users
recipes_coll = mongo.db.recipes
cuisines_coll = mongo.db.cuisines
diets_coll = mongo.db.diets
meals_coll = mongo.db.meals

@app.route("/")
def test():
    return "Hello world"

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True) 