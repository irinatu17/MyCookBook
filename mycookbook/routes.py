from flask import render_template, url_for, flash, redirect, request, session
from mycookbook import app, mongo
from werkzeug.security import generate_password_hash, check_password_hash
from mycookbook.forms import RegistrationForm, LoginForm
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId


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
    if 'username' in session:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        # Variable for users collection
        users = users_coll
        registered_user = users_coll.find_one({'username': request.form['username']})
        if registered_user:
            flash("Sorry, this username is already taken!")
            return redirect(url_for('register'))
        else:
            hashed_password = generate_password_hash(request.form['password'])
            new_user = {
                "username": request.form['username'],
                "password": hashed_password,
                "user_recipes": [],
            }
            users.insert_one(new_user)
            session["username"] = request.form['username']
            flash(f'Your account have been successfully created.')
            return redirect(url_for('home'))
    return render_template('register.html', form=form,  title='Register')
