from flask import render_template, url_for, flash, redirect, request, session
from mycookbook import app, mongo
from werkzeug.security import generate_password_hash, check_password_hash
from mycookbook.forms import RegisterForm, LoginForm, \
    ChangeUsernameForm, ChangePasswordForm, Add_RecipeForm
from flask_pymongo import pymongo
from bson.objectid import ObjectId
import math


# MongoDB Collections
users_coll = mongo.db.users
recipes_coll = mongo.db.recipes
cuisines_coll = mongo.db.cuisines
diets_coll = mongo.db.diets
meals_coll = mongo.db.meals

# Landing page
@app.route('/')
@app.route("/home")
# The idea of getting random recipes using "$sample" is taken 
# from MongoDB documentation: https://docs.mongodb.com/manual/reference/operator/aggregation/sample/
def home():
    featured_recipes = ([recipe for recipe in recipes_coll.aggregate
                        ([{"$sample": {"size": 4}}])])
    return render_template('home.html', featured_recipes=featured_recipes,
                           title='Home')


'''
RECIPES ROUTES

'''
# All recipes display
@app.route('/all_recipes')
def all_recipes():
    limit_per_page = 8
    current_page = int(request.args.get('current_page', 1))
    number_of_all_rec = recipes_coll.count()
    pages = range(1, int(math.ceil(number_of_all_rec / limit_per_page)) + 1)
    recipes = recipes_coll.find().sort('_id', pymongo.ASCENDING).skip(
        (current_page - 1)*limit_per_page).limit(limit_per_page)

    return render_template("all_recipes.html", recipes=recipes,
                           title='All Recipes', current_page=current_page,
                           pages=pages)
# Single Recipe details display
@app.route('/recipe_details/<recipe_id>')
def single_recipe_details(recipe_id):

    selected_recipe = recipes_coll.find_one({"_id": ObjectId(recipe_id)})
    author = users_coll.find_one(
        {"_id": ObjectId(selected_recipe.get("author"))})["username"]
    return render_template("single_recipe_details.html",
                           selected_recipe=selected_recipe, author=author,
                           title='Recipe Details')

# My recipes
@app.route('/my_recipes/<username>')
def my_recipes(username):
    my_id = users_coll.find_one({'username': session['username']})['_id']
    my_username = users_coll.find_one({'username': session
                                      ['username']})['username']
    my_recipes = recipes_coll.find({'author': my_id})
    number_of_recipes = recipes_coll.find({'author': my_id}).count()
    return render_template("my_recipes.html", my_recipes=my_recipes,
                           username=my_username,
                           number_of_recipes=number_of_recipes,
                           title='My Recipes')

# Add recipe
@app.route('/add_recipe')
def add_recipe():
    form = Add_RecipeForm()
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
            "image": request.form.get("image")
        }
        insert_recipe_intoDB = recipes_coll.insert_one(new_recipe)
        users_coll.update_one(
            {"_id": ObjectId(author)},
            {"$push": {"user_recipes": insert_recipe_intoDB.inserted_id}})
        return redirect(url_for(
            "home",
            recipe_id=insert_recipe_intoDB.inserted_id))

# Edit Recipe
@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    selected_recipe = recipes_coll.find_one({"_id": ObjectId(recipe_id)})
    diet_types = diets_coll.find()
    meal_types = meals_coll.find()
    cuisine_types = cuisines_coll.find()
    return render_template('edit_recipe.html', selected_recipe=selected_recipe,
                           cuisine_types=cuisine_types, diet_types=diet_types,
                           meal_types=meal_types, title='Edit Recipe')


# Update Recipe in Database
@app.route("/update_recipe/<recipe_id>", methods=["POST"])
def update_recipe(recipe_id):
    recipes = recipes_coll
    selected_recipe = recipes_coll.find_one({"_id": ObjectId(recipe_id)})
    author = selected_recipe.get("author")
    ingredients = request.form.get("ingredients").splitlines()
    directions = request.form.get("directions").splitlines()
    if request.method == "POST":
        recipes.update({"_id": ObjectId(recipe_id)}, {
            "recipe_name": request.form.get("recipe_name"),
            "description": request.form.get("recipe_description"),
            "cuisine_type": request.form.get("cuisine_type"),
            "meal_type": request.form.get("meal_type"),
            "cooking_time": request.form.get("cooking_time"),
            "diet_type": request.form.get("diet_type"),
            "servings": request.form.get("servings"),
            "ingredients": ingredients,
            "directions": directions,
            'author': author,
            "image": request.form.get("recipe_image")
        })
        return redirect(url_for("single_recipe_details",
                                recipe_id=recipe_id))

# Delete Recipe
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    recipes_coll.remove({"_id": ObjectId(recipe_id)})
    author = users_coll.find_one({'username': session['username']})['_id']
    users_coll.update_one({"_id": ObjectId(author)},
                          {"$pull": {"user_recipes": ObjectId(recipe_id)}})

    return redirect(url_for("all_recipes"))


'''
USER ROUTES

'''
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

# Change username
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

# Change password
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
                users.update_one({'username': username},
                                 {'$set': {'password': generate_password_hash
                                           (request.form['new_password'])}})
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

# Delete Account
@app.route("/delete_account/<username>", methods=['GET', 'POST'])
def delete_account(username):
    user = users_coll.find_one({"username": username})
    if check_password_hash(user["password"],
                           request.form.get("confirm_password_to_delete")):
        # Removes all user's recipes from the Database
        all_user_recipes = user.get("user_recipes")
        for recipe in all_user_recipes:
            recipes_coll.remove({"_id": recipe})
        flash("Your account has been deleted.")
        session.pop("username", None)
        users_coll.remove({"_id": user.get("_id")})
        return redirect(url_for("home"))
    else:
        flash("Password is incorrect! Please try again")
        return redirect(url_for("account_settings", username=username))


'''
Error handlers

'''
# handle 404 error (page not found)
@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404.html', error=True,
                           title="Page not found"), 404

# handle 500 error (internal server error)
@app.errorhandler(500)
def error_500(error):
    return render_template('errors/500.html', error=True,
                           title="Internal Server Error"), 500
