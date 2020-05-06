from flask import render_template, url_for, flash, redirect, request, session
from mycookbook import app, mongo
from werkzeug.security import generate_password_hash, check_password_hash
from mycookbook.forms import RegisterForm, LoginForm, \
    ChangeUsernameForm, ChangePasswordForm, Add_Edit_RecipeForm
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

# My recipes
@app.route('/my_recipes')
def my_recipes():
    return render_template("my_recipes.html",
                           title='My Recipes')

# Add recipe
@app.route('/add_recipe')
def add_recipe():
    form = Add_Edit_RecipeForm(request.form)
    diet_types = diets_coll.find()
    meal_types = meals_coll.find()
    cuisine_types = cuisines_coll.find()
    return render_template("add_recipe.html", diet_types=diet_types,
                           cuisine_types=cuisine_types, meal_types=meal_types,
                           form=form, title='New Recipe')

# Insert recipe
@app.route("/insert_recipe", methods=['GET', 'POST'])
def insert_recipe():
    ingredients = request.form.get("ingredients").splitlines()
    directions = request.form.get("recipe_directions").splitlines()
    author = users_coll.find_one({"username": session["username"]})["_id"]

    if request.method == 'POST':

        new_recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "description": request.form.get("recipe_description"),
            "cuisine_type": request.form.get("cuisine_type"),
            "meal_type": request.form.get("meal_type"),
            "diet_type": request.form.get("diet_type"),
            "cooking_time": request.form.get("cooking_time"),
            "servings": request.form.get("servings"),
            "ingredients": ingredients,
            "directions": directions,
            'author': author,
            "image": request.form.get("recipe_image")
        }
        insert_recipe_intoDB = recipes_coll.insert_one(new_recipe)
        users_coll.update_one(
            {"_id": ObjectId(author)},
            {"$push": {"user_recipes": insert_recipe_intoDB.inserted_id}})
        return redirect(url_for(
            "home",
            recipe_id=insert_recipe_intoDB.inserted_id))


# Login
@app.route("/login",  methods=['GET', 'POST'])
def login():
    # Check if the user is already logged in
    if 'username' in session:
        flash('You are already logged in')
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        # Variable for users collection
        users = users_coll
        registered_user = users.find_one({'username':
                                          request.form['username']})

        if registered_user:
            # Check if password entered by user is equal to the password in the DB
            if check_password_hash(registered_user['password'],
                                   request.form['password']):
                # Add user to session if passwords match
                session['username'] = request.form['username']
                flash('You have been successfully logged in!')
                return redirect(url_for('home'))
            else:
                flash("Incorrect username or password. Please try again")
                return redirect(url_for('login'))
        else:
            flash("Username does not exist! Please try again")
            return redirect(url_for('login'))
    return render_template('login.html',  form=form, title='Login')

# Register
@app.route("/register", methods=['GET', 'POST'])
def register():
    if 'username' in session:
        return redirect(url_for('home'))

    form = RegisterForm()
    if form.validate_on_submit():
        # Variable for users collection
        users = users_coll
        registered_user = users_coll.find_one({'username':
                                               request.form['username']})
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

# Logout
@app.route("/logout")
def logout():
    session.pop("username",  None)
    return redirect(url_for("home"))

# Account Settings
@app.route("/account_settings/<username>")
def account_settings(username):
    username = users_coll.find_one({'username':
                                    session['username']})['username']
    return render_template('account_settings.html',
                           username=username, title='Account Settings')


@app.route("/change_username/<username>", methods=['GET', 'POST'])
def change_username(username):

    users = users_coll
    form = ChangeUsernameForm()
    if form.validate_on_submit():
        registered_user = users.find_one({'username':
                                         request.form['new_username']})
        if registered_user:
            flash('Sorry, username is already taken. Try another one')
            return redirect(url_for('change_username',
                                    username=session["username"]))
        else:
            users.update_one(
                {"username": username},
                {"$set": {"username": request.form["new_username"]}})
        flash("Your username was updated successfully.\
                    Please, login with your new username")
        session.pop("username",  None)
        return redirect(url_for("login"))

    return render_template('change_username.html',
                           username=session["username"],
                           form=form, title='Change Username')


@app.route("/change_password/<username>", methods=['GET', 'POST'])
def change_password(username):
    users = users_coll
    form = ChangePasswordForm()
    username = users.find_one({'username': session['username']})['username']
    old_password = request.form.get('old_password')
    new_password = request.form.get('new_password')
    confirm_password = request.form.get("confirm_new_password")
    
    if form.validate_on_submit():
        if check_password_hash(users.find_one({'username': username})
                               ['password'], old_password):
            if new_password == confirm_password:
                users.update_one({'username': username}, {'$set': {'password': generate_password_hash(request.form['new_password'])}})
                flash("Success! Your password was updated.")
                return redirect(url_for('account_settings', username=username))
            else:
                flash("New passwords do not match! Please try again")
                return redirect(url_for("change_password",
                                        username=session["username"]))
        else:
            flash('Incorrect original password! Please try again')
            return redirect(url_for('change_password',
                            username=session["username"]))
    return render_template('change_password.html', username=username,
                           form=form, title='Change Password')


@app.route("/delete_account/<username>", methods=['GET', 'POST'])
def delete_account(username):
    user = users_coll.find_one({"username": username})
    if check_password_hash(user["password"],
                           request.form["confirm_password_to_delete"]):
        flash("Your account has been deleted.")
        session.pop("username", None)
        users_coll.remove({"_id": user.get("_id")})
        return redirect(url_for("home"))
    else:
        flash("Password is incorrect! Please try again")
        return redirect(url_for("account_settings", username=username))
