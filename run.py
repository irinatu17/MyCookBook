import os
from flask import Flask, render_template, url_for, flash, redirect
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from forms import RegistrationForm, LoginForm

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

# Landing page
@app.route('/')
@app.route("/home")
def home():
    # Variable for recipes collection
    recipes = recipes_coll
    return render_template('home.html', title='Home')

# All recipes display
@app.route('/all_recipes')
def all_recipes():
    # Variable for recipes collection
    recipes = recipes_coll
    return render_template("all_recipes.html", recipes=recipes_coll.find(),
                           title='Recipes')

# Login
@app.route("/login",  methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Variable for users collection
        users = users_coll
        if form.username.data == 'admin' and form.password.data == 'password':
            flash('You have been successfully logged in!')
            return redirect(url_for('home'))
        else:
            flash('Username or password is incorrect. Please try again')
    return render_template('login.html',  form=form, title='Login')

# Register
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Variable for users collection
        users = users_coll


        flash(f'Account created for {form.username.data}!')
        return redirect(url_for('home'))
    return render_template('register.html', form=form,  title='Register')


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
