from flask import render_template, url_for, flash, redirect, request, session
from mycookbook import app, mongo
from werkzeug.security import generate_password_hash, check_password_hash
from mycookbook.forms import RegisterForm, LoginForm, \
    ChangeUsernameForm, ChangePasswordForm, Add_RecipeForm
from flask_pymongo import pymongo
from bson.objectid import ObjectId
import math

# MongoDB Collections variables
users_coll = mongo.db.users
recipes_coll = mongo.db.recipes
cuisines_coll = mongo.db.cuisines
diets_coll = mongo.db.diets
meals_coll = mongo.db.meals


'''
HOME PAGE
'''


@app.route('/')
@app.route("/home")
def home():
    '''
    Main home page.
    Allows users to view 4 random featured recipes
    from the database as clickable cards, located bellow the hero image.
    '''
    # Generate 4 random recipes from the DB
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
    '''
    READ.
    Displays all the recipes from the database using pagination.
    The limit is set to 8 recipes per page.
    Also displayes the number of all recipes.
    '''
    # CREDITS: the idea of pagination used below is taken and modified
    # from the Shane Muirhead's project
    limit_per_page = 8
    current_page = int(request.args.get('current_page', 1))
    # get total of all the recipes in db
    number_of_all_rec = recipes_coll.count()
    pages = range(1, int(math.ceil(number_of_all_rec / limit_per_page)) + 1)
    recipes = recipes_coll.find().sort('_id', pymongo.ASCENDING).skip(
        (current_page - 1)*limit_per_page).limit(limit_per_page)

    return render_template("all_recipes.html", recipes=recipes,
                           title='All Recipes', current_page=current_page,
                           pages=pages, number_of_all_rec=number_of_all_rec)


# Single Recipe details display
@app.route('/recipe_details/<recipe_id>')
def single_recipe_details(recipe_id):
    '''
    READ.
    Displays detailed information about a selected recipe.
    If logged id user is an author of the selected recipe,
    there are buttons "edit" and "delete" displayed
    giving the oportunity to manipulate the recipe.
    '''
    # find the selected recipe in DB by its id
    selected_recipe = recipes_coll.find_one({"_id": ObjectId(recipe_id)})
    # Set the author of the recipe
    author = users_coll.find_one(
        {"_id": ObjectId(selected_recipe.get("author"))})["username"]
    return render_template("single_recipe_details.html",
                           selected_recipe=selected_recipe, author=author,
                           title='Recipe Details')


# My recipes
@app.route('/my_recipes/<username>')
def my_recipes(username):
    '''
    READ.
    Displays the recipes created by logged in user in session.
    If user has not created any recipes yet, there's a button "add recipe"
    giving an opportunity to create a new recipe.
    Pagination is in place diplaying 8 recipes per page.
    Also displays the total number of recipes created by the user.
    '''
    my_id = users_coll.find_one({'username': session['username']})['_id']
    my_username = users_coll.find_one({'username': session
                                      ['username']})['username']
    # finds all user's recipes by author id
    my_recipes = recipes_coll.find({'author': my_id})
    # get total number of recipes created by the user
    number_of_my_rec = my_recipes.count()
    # Pagination, displays 8 recipes per page
    # CREDITS: the idea of pagination used below is taken and modified
    # from the Shane Muirhead's project
    limit_per_page = 8
    current_page = int(request.args.get('current_page', 1))
    pages = range(1, int(math.ceil(number_of_my_rec / limit_per_page)) + 1)
    recipes = my_recipes.sort('_id', pymongo.ASCENDING).skip(
        (current_page - 1)*limit_per_page).limit(limit_per_page)

    return render_template("my_recipes.html", my_recipes=my_recipes,
                           username=my_username, recipes=recipes,
                           number_of_my_rec=number_of_my_rec,
                           current_page=current_page, pages=pages,
                           title='My Recipes')


# Add recipe
@app.route('/add_recipe')
def add_recipe():
    '''
    CREATE.
    The function calls Add_RecipeForm class from forms.py
    to diplay the form for adding new recipe,
    fill dropdowns with data from cuisins, diets and meals collections.
    Only logged in users can view and fill the form
    '''
    # prevents guest users from viewing the form
    if 'username' not in session:
        flash('You must be logged in to add a new recipe!')
        return redirect(url_for('home'))
    # form variable to initialise the form
    form = Add_RecipeForm()
    # variables to fill dropdownes with data from collections
    diet_types = diets_coll.find()
    meal_types = meals_coll.find()
    cuisine_types = cuisines_coll.find()
    return render_template("add_recipe.html", diet_types=diet_types,
                           cuisine_types=cuisine_types, meal_types=meal_types,
                           form=form, title='New Recipe')


# Insert recipe
@app.route("/insert_recipe", methods=['GET', 'POST'])
def insert_recipe():
    '''
    CREATE.
    Inserts new created recipe to the "recipes" collection in DB
    after submission the form from the add_recipe page.
    '''

    # split ingredients and directions into lists
    ingredients = request.form.get("ingredients").splitlines()
    directions = request.form.get("recipe_directions").splitlines()
    # identifies the user in session to assign an author for new recipe
    author = users_coll.find_one({"username": session["username"]})["_id"]

    if request.method == 'POST':
        # inser the new recipe after submission the form
        new_recipe = {
            "recipe_name": request.form.get("recipe_name").strip(),
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
        # updates "user recipes" list with recipe_id added in user collection
        users_coll.update_one(
            {"_id": ObjectId(author)},
            {"$push": {"user_recipes": insert_recipe_intoDB.inserted_id}})
        flash('Your recipe  was succsessfully added!')
        return redirect(url_for(
            "single_recipe_details",
            recipe_id=insert_recipe_intoDB.inserted_id))


# Edit Recipe
@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    '''
    UPDATE.
    Renders edit_recipe page, provides the user with a form to edit task
    with pre-populated fields.
    '''
    # prevents guest users from viewing the form
    if 'username' not in session:
        flash('You must be logged in to edit a recipe!')
        return redirect(url_for('home'))
    user_in_session = users_coll.find_one({'username': session['username']})
    # get the selected recipe for filling the fields
    selected_recipe = recipes_coll.find_one({"_id": ObjectId(recipe_id)})
    # allows only author of the recipe to edit it;
    # protects againts brute-forcing
    if selected_recipe['author'] == user_in_session['_id']:
        # variables to fill dropdownes with data from collections
        diet_types = diets_coll.find()
        meal_types = meals_coll.find()
        cuisine_types = cuisines_coll.find()
        return render_template('edit_recipe.html',
                               selected_recipe=selected_recipe,
                               cuisine_types=cuisine_types,
                               diet_types=diet_types,
                               meal_types=meal_types, title='Edit Recipe')
    else:
        flash("You can only edit your own recipes!")
        return redirect(url_for('home'))


# Update Recipe in the Database
@app.route("/update_recipe/<recipe_id>", methods=["POST"])
def update_recipe(recipe_id):
    '''
    UPDATE.
    Updates the selected recipe in the database after submission the form.
    '''
    recipes = recipes_coll

    selected_recipe = recipes_coll.find_one({"_id": ObjectId(recipe_id)})
    # identifies the user in session to assign an author for edited recipe
    author = selected_recipe.get("author")
    # split ingredients and directions into lists
    ingredients = request.form.get("ingredients").splitlines()
    directions = request.form.get("directions").splitlines()
    if request.method == "POST":
        # updates the selected recipe with data gotten from the form
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
    '''
    DELETE.
    Removes the selected recipe from the database.
    Only the author of the recipe can delete the recipe.
    '''
    # prevents guest users from viewing the modal
    if 'username' not in session:
        flash('You must be logged in to delete a recipe!')
        return redirect(url_for('home'))
    user_in_session = users_coll.find_one({'username': session['username']})
    # get the selected recipe for filling the fields
    selected_recipe = recipes_coll.find_one({"_id": ObjectId(recipe_id)})
    # allows only author of the recipe to delete it;
    # protects againts brute-forcing
    if selected_recipe['author'] == user_in_session['_id']:
        recipes_coll.remove({"_id": ObjectId(recipe_id)})
        # find the author of the selected recipe
        author = users_coll.find_one({'username': session['username']})['_id']

        users_coll.update_one({"_id": ObjectId(author)},
                              {"$pull": {"user_recipes": ObjectId(recipe_id)}})
        flash('Your recipe has been deleted.')
        return redirect(url_for("home"))
    else:
        flash("You can only delete your own recipes!")
        return redirect(url_for('home'))


'''
USER ROUTES
'''


# Login
@app.route("/login",  methods=['GET', 'POST'])
def login():
    '''
    The login function calls LoginForm class from forms.py,
    It checks if the entered username and passwords are valid
    and then add user to session.
    '''
    # Check if the user is already logged in
    if 'username' in session:
        flash('You are already logged in!')
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        # Variable for users collection
        users = users_coll
        registered_user = users.find_one({'username':
                                          request.form['username']})

        if registered_user:
            # Check if password in the form is equal to the password in the DB
            if check_password_hash(registered_user['password'],
                                   request.form['password']):
                # Add user to session if passwords match
                session['username'] = request.form['username']
                flash('You have been successfully logged in!')
                return redirect(url_for('home'))
            else:
                # if user entered incorrect password
                flash("Incorrect username or password. Please try again")
                return redirect(url_for('login'))
        else:
            # if user entered incorrect username
            flash("Username does not exist! Please try again")
            return redirect(url_for('login'))
    return render_template('login.html',  form=form, title='Login')


# Register
@app.route("/register", methods=['GET', 'POST'])
def register():
    '''
    CREATE.
    Creates a new account; it calls the RegisterForm class from forms.py.
    Checks if the username is not already excist in database,
    hashes the entered password and add a new user to session.
    '''
    # checks if user is not already logged in
    if 'username' in session:
        flash('You are already registered!')
        return redirect(url_for('home'))

    form = RegisterForm()
    if form.validate_on_submit():
        # variable for users collection
        users = users_coll
        # checks if the username is unique
        registered_user = users_coll.find_one({'username':
                                               request.form['username']})
        if registered_user:
            flash("Sorry, this username is already taken!")
            return redirect(url_for('register'))
        else:
            # hashes the entered password
            hashed_password = generate_password_hash(request.form['password'])
            new_user = {
                "username": request.form['username'],
                "password": hashed_password,
                "user_recipes": [],
            }
            users.insert_one(new_user)
            # add new user to the session
            session["username"] = request.form['username']
            flash('Your account has been successfully created.')
            return redirect(url_for('home'))
    return render_template('register.html', form=form,  title='Register')


# Logout
@app.route("/logout")
def logout():
    '''
    Logs user out and redirects to home
    '''
    session.pop("username",  None)
    return redirect(url_for("home"))


# Account Settings
@app.route("/account_settings/<username>")
def account_settings(username):
    '''
    Account settings page - displays username,
    buttons for change_username, change_password
    and delete_account pages.
    '''
    # prevents guest users from viewing the page
    if 'username' not in session:
        flash('You must be logged in to view that page!')
    username = users_coll.find_one({'username':
                                    session['username']})['username']
    return render_template('account_settings.html',
                           username=username, title='Account Settings')


# Change username
@app.route("/change_username/<username>", methods=['GET', 'POST'])
def change_username(username):
    '''
    UPDATE.
    Allows user to change the current username.
    It calls the ChangeUsernameForm class from forms.py.
    Checks if the new username is unique and not exist in database,
    then clear the session and redirect user to login page.
    '''
    # prevents guest users from viewing the form
    if 'username' not in session:
        flash('You must be logged in to change username!')
    users = users_coll
    form = ChangeUsernameForm()
    if form.validate_on_submit():
        # checks if the new username is unique
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
        # clear the session and redirect to login page
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
    '''
    UPDATE.
    Allows user to change the current password.
    It calls the ChangePasswordForm class from forms.py.
    Checks if the current password is correct, validate new password.
    Then if new password matchs confirm password field,
    insert it to the database.
    '''
    # prevents guest users from viewing the form
    if 'username' not in session:
        flash('You must be logged in to change password!')
    users = users_coll
    form = ChangePasswordForm()
    username = users.find_one({'username': session['username']})['username']
    old_password = request.form.get('old_password')
    new_password = request.form.get('new_password')
    confirm_password = request.form.get("confirm_new_password")
    if form.validate_on_submit():
        # checks if current password matches existing password in database
        if check_password_hash(users.find_one({'username': username})
                               ['password'], old_password):
            # checks if new passwords match
            if new_password == confirm_password:
                # update the password and redirect to the settings page
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
    '''
    DELETE.
    Remove user's account from the database as well as all recipes
    created by this user. Before deletion of the account, user is asked
    to confirm it by entering password.
    '''
    # prevents guest users from viewing the form
    if 'username' not in session:
        flash('You must be logged in to delete an account!')
    user = users_coll.find_one({"username": username})
    # checks if password matches existing password in database
    if check_password_hash(user["password"],
                           request.form.get("confirm_password_to_delete")):
        # Removes all user's recipes from the Database
        all_user_recipes = user.get("user_recipes")
        for recipe in all_user_recipes:
            recipes_coll.remove({"_id": recipe})
        # remove user from database,clear session and redirect to the home page
        flash("Your account has been deleted.")
        session.pop("username", None)
        users_coll.remove({"_id": user.get("_id")})
        return redirect(url_for("home"))
    else:
        flash("Password is incorrect! Please try again")
        return redirect(url_for("account_settings", username=username))


'''
ERROR HANDLERS
'''


@app.errorhandler(404)
def error_404(error):
    '''
    Handles 404 error (page not found)
    '''
    return render_template('errors/404.html', error=True,
                           title="Page not found"), 404


@app.errorhandler(500)
def error_500(error):
    '''
    Handles 500 error (internal server error)
    '''
    return render_template('errors/500.html', error=True,
                           title="Internal Server Error"), 500
