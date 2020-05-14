# [My CookBook](https://mycookbook-project.herokuapp.com/)
"My CookBook" - Practical Python and Data-Centric Development Milestone Project.

The main purpose of this full-stack MongoDB-based Flask project is to create a database of recipes that allows users to create, read, update and delete (CRUD) recipes.
"My CookBook" gives an access to all the recipes in the database for non-registered users. At the same time, it gives the opportunity to create an account and benifit from having convenient access to all features of the website.
Registered users can add new recipes, edit and delete their own ones, as well as edit their username and password or delete account.  
[My CookBook](https://mycookbook-project.herokuapp.com/) is a simple way to view, create and store your recipes!   
Sign in, get inspired, contribute, cook and enjoy!

---

## Table of Contents
1. [UX](#ux)
    - [User Stories](#user-stories)
    - [Design](#design)
    - [Wireframes](#wireframes)

2. [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)

3. [Technologies Used](#technologies-used)

4. [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Validators](#validators)
    - [Compatibility](#compatibility)

5. [Deployment](#deployment)
    - [Local Deployment](#local-deployment)
    - [Remote Deployment](#remote-deployment)

6. [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

---

## UX
My main goal in UX was to built a website minimalistic in design, simple to use; where users can create their own recipes, view all the recipes created by others,
edit and delete their recipes. The target audience for this app is anyone who has passion for cooking, wants to discover new recipes or needs to store their own recipes online.  
Creating modern, sleek and user-friendly interface with easy access to all information is the key to giving users feel of reliability, security and positiveness. 
With this in mind, I developed this app in a way that everyone can view all the recipes on the website, while only authors can make changes to their recipes.   
As well as that, structuring the website in well-organised readable way with easy navigation was another goal for this project.
### User Stories
**As a user, I want/expect:**
- to view all the recipes without having to register
- to view all recipe details (including cuisine, meal and diet types, cooking time, servings, list of ingredients and directions)
- to see how many recipes are on the website
- to create my own account
- to add new recipes 
- to edit my recipes 
- to view a list of my recipes on a separate page and see how many recipes I've created
- to delete my recipes
- to log out any time and have the session terminated
- to change my current username
- to change my current password
- to delete my account and all recipes I've created
- to use the website from any device (laptop, tablet, mobile)
### Design
The goal in design was to create a website that is overall user friendly, has a modern feel with emphasis on providing information about recipes in a readable and eye-catching way. Therefore, following design choices were made:
#### Framework
[Materialize](https://materializecss.com/), front-end framework based on Material Design was chosen for this project for its modern interface and ease of use. It was used for creating features such as navbar, cards, forms, modal, as well as for its grid.  
[JQuery](https://jquery.com/) was used for initializing some Materialize elements listed above, as well as for custom functions, simple DOM manipulation.
#### Colour Scheme
One of the main goals was to focus user's attention on the recipe cards and recipes' images. Therefore, I decided to have a lot of whitespaces and mostly white background accross the website, giving preferences to calm white and grey colours (e.g. for navbar, footer, forms). Bright colours are only used for buttons, icons and some headings to catch user's atention.    
The idea of using different shades of the same colour is implemented accross the website. The primary colour used for main buttons and headings is coral as it seems to create a nice contrast with grey and white backgrounds. The secondary colour used for icons, dividers and some other buttons is yellow.   
##### Main colour palette
 - ![#ff4242](https://placehold.it/15/ff4242/ff4242) `#ff4242` - **coral**
 - ![#fab700](https://placehold.it/15/fab700/fab700) `#fab700` - **yellow**
 - ![#c89200](https://placehold.it/15/c89200/c89200) `#c89200` - **darkyellow**
 - ![#2e2e2e](https://placehold.it/15/2e2e2e/2e2e2e) `#2e2e2e` - **lightblack**
 - ![#f5f5f5f3](https://placehold.it/15/f5f5f5f3/f5f5f5f3) `#f5f5f5f3` - **darkwhite**
 - ![#ffffff](https://placehold.it/15/ffffff/ffffff) `#ffffff` - **white** 
#### Typography
There are two fonts used across the project: [Open Sans](https://fonts.google.com/specimen/Open+Sans)-the main primary font and [Ubuntu](https://fonts.google.com/specimen/Ubuntu) - the secondary font, used for some headings and buttons.

#### Icons
Icons are used widely, as they are good attention grabbers. They help users to find and scan content. Another advantage of using them is to help to break language barriers. They create more user-friendly experience for people with non-native English.  
I used [FontAwesome](https://fontawesome.com/) as the main icon library across the project (e.g. for navbar, footer, forms, recipe details page). However,  [Materialize icons](https://materializecss.com/icons.html) were used as well in some cases.

### Wireframes
[Balsamiq Wireframes](https://balsamiq.com/) was used to create all wireframes for the project.

Initial wireframes with some comments for both desktop and mobile devices can be found [here](https://github.com/irinatu17/MyCookBook/tree/master/mycookbook/wireframes).

---

## Features
### Existing Features
#### Navbar
The navbar is fixed at the top of the page while scrolling down, what allows a user to easily navigate throughout the website.  The logo in the top right corner on desktop and in the center on smaller devices redirects to the home page when it is clicked.
On the smaller resolutions (tablet, mobile) it is collapsed into a burger icon, when it is clicked, slide out menu opens.     

For **non-logged in** users or **guests** navbar contains the following links:
- Home
- Browse Recipes
- Login
- Register
For **logged-in** users navbar contains the following links:
- Home
- Browse Recipes
- Account (it is a dropdown on desktop)
    - My Recipes
    - Add New Recipe
    - Settings
- Logout
#### Featured Recipes
The home page contains a button that redirects to the "All Recipes" page. It also displays 4 random images from 
the database using the `$sample` function of MongoDB. 
#### Browse All Recipes
All recipes page displays recipe cards sorted from the oldest to the most recently added. As well as that, there is a total number of recipes displayed in parentheses after the heading.
All recipe cards are clickable and redirect a user to the individual recipe page with detailed information.
The pagination at the bottom of the page allows to display 8 recipes per page.
#### Single Recipe details
Single recipe details page renders when user clicks on the recipe card. It displays information about the selected recipe:
recipe name, description, cuisine type, meal type, diet type, number of servings, cooking time, author, ingredients, directions and recipe image(or recipe placeholder).
If the user is author of the recipe, there are buttons "Edit" and "Delete", that redirect to the edit and delete recipe pages responsively.
#### Register
The register page allows user to create a new account. User is asked to fill the fields "username", "password" and "confirm password".
The code checks against existing username to assign only unique username, that must be 3-15 characters long. The same validation requirement applies to the password fields,
which must match the "confirm password" field. All passwords are hashed for security purposes. If user's input does not meet requirements, flash messages will inform user about the error.
When form is submitted successfullly, user is redirected to the home page, informing that account was created.
#### Login
The login page features the form with "username" and "password" fields, allowing registered user to log into their account.
If the entered username and hashed password match the ones in the database, user is redirected to the home page and informed that logged in was succsessful. Otherwise, flash messages will be displayed about incorrect user's input.
#### Logout 
Hitting "logout" button by logged in users ends their session and redirects to the homepage.
#### My recipes
My recipes page allows registered users to view all their recipes. It also displays the total number of all the user's recipes.
Pagination is in place displaying 8 recipes per page. If user has not created any recipes yet, there's a button "Add recipe" preceded by insruction, which redirects user to the add recipe page.
#### Add Recipe
Registered and logged in users can add new recipes through the form. There are some validations in place, all the fields except "Cuisine type", "Diet type" and "Recipe Image" are required. For the "recipe name" and "recipe description" characters limit is set.
If user does not provide a URL to the recipe image, recipe placeholder will be assigned for that recipe. There is also Tooltip-instruction saying that user can upload the image to a free image hosting website(e.g. ImgBB).
After succsessful addition, user is redirected to the created recipe details page. There is also a button "Cancel" that simply redirects user to the home page (in order to avoid to hit "back").
#### Edit Recipe
Edit recipe page allows logged in user to update the the information about the recipe. The "Edit" button will appear only for author of the recipe. 
As well as that, the defensive design(against brute-forcing) in place allows only authors of the recipe make changes. 
The form is pre-populated with the relevant data. After clicking "Edit recipe" button, the recipe is updated in the database and user is redirected to the updated recipe details page.
#### Delete Recipe
Delete recipe function allows only author of the recipe delete it. After user clicks the "delete" button in a Single Recipe Details page, the modal will be opened. It asks user to confirm that the recipe is wanted to be deleted. 
If so, clicking "delete" button, recipe will be removed from the database as well as from the user_recipes field of the recipe's author in users collection. There is also button "cancel" that is close the modal when it's clicked.
#### Account Settings page
Account Settings page contains username, randomly generated user avatar and 3 buttons "Change username", "Change password" and "Delete account".
#### Change username
The form displayed allows registered user to change the username. If checks if the new entered username is not exist in the database. After succsessfull submition, it redirect user to login page asking for logging in with a new username.
#### Change password
A user can change the current password by filling the form, that contains following fields "Current password", "New password", "Confirm New password".
Both new password have to match and be 3-15 characters long. If the form is successfullly submited, user is redirected to the account settings page with a flash message about successfullly changed password.
#### Delete account
Once the "delete account" button on the account settings page is clicked, the modal shows up asking to confirm if the user is sure wans to delete account. To verify it, user have to provide the password and after clicking "delete account" button, the account is removed from the users collection. All the recipes created by this user are removed from the recipes collection as well.
#### Footer
The footer features links to the social media which open in a new tab (by using `'target="_blank"`). 
#### 404 and 500 error pages
Custom 404 and 500 pages contains short information about the error and a button "Back Home". As well as that, it displays navbar that allows users easily come back to any page if they are got lost.

### Features Left to Implement
There are some features that I was not able to implement due to time time constraints, but would like to do it in future.
Both of these features are can be seen in my initial wireframes.
#### Search recipe
Search recipe function based on the keyword, recipe name allowing user to search for the recipe. Filters by cuisine, by meal type and by diet type would 
allow user to have more detailed search.
#### My favourites
User would have an opportunity to "like" others recipes, saving in "my favourites" collection, which would be displayed on a separate page.
Each recipe card will include small "heart" icon, clicking which user will add the selecteed recipe to "my favourits"

---

## Technologies Used

- [GitPod](https://www.gitpod.io/) - an online IDE for developing this project.
- [Git](https://git-scm.com/) - for version control.
- [GitHub](https://git-scm.com/) - for remotely storing project's code.
- [PIP](https://pip.pypa.io/en/stable/installing/) - for installation of necessary tools.
- [GIMP2](https://www.gimp.org/) - for editing, compressing and resizing images.
### Front-End
- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - to build the foundation of the project.
- [CSS](https://developer.mozilla.org/en-US/docs/Archive/CSS3) - to create custom styles.
### Back-End
- [Python 3.8.2](https://www.python.org/)[ -  back-end programming language used in this project.
- [Flask 1.1.2](https://flask.palletsprojects.com/en/1.1.x/) - microframework for building and rendering pages.
- [MongoDB Atlas](https://www.mongodb.com/) - NoSQL database for storing back-end data.
- [PyMongo](https://api.mongodb.com/python/current/) - for Python to get access the MongoDB database.
- [WTForms 2.2.1](https://pypi.org/project/WTForms/) - for creating forms with validation.
- [Werkzeug 0.16.1](https://werkzeug.palletsprojects.com/en/0.16.x/) - to generate and verify password hashing.
- [Jinja 2.10.1](https://jinja.palletsprojects.com/en/2.10.x/) - templating language for Python, to display back-end data in HTML.
- [Heroku](https://heroku.com/) - to host the project.
### Libraries
- [Materialize 1.0.0](https://materializecss.com/) - main responsive modern front-end framework used for grid and responsivesness.
- [Google Fonts](https://fonts.google.com/) - to import fonts.
- [FontAwesome](https://fontawesome.com/) - to provide icons used across the project. 
- [Adorable Avatars](http://avatars.adorable.io/) -  to create user avatars.
- [JQuery 3.5.0](https://jquery.com/) - to simplify DOM manipulation and to initialize Materialize functions.
---

## Testing
### Manual Testing

### Validators

### Compatibility



---

## Deployment
### Local Deployment
To be able to run this project, the following tools have to be installed:
- An IDE (I used **[GitPod]**(https://www.gitpod.io/) online IDE for creating this project)
- [MongoDB Atlas](https://www.mongodb.com/) (for creation your database)
- [Git](https://git-scm.com/)
- [PIP](https://pip.pypa.io/en/stable/installing/) 
- [Python](https://www.python.org/)   
#### Directions
1. You can clone this repository directly into the editor of your choice by pasting the following command in the terminal:   
`git clone https://github.com/irinatu17/MyCookBook`    
Alternatively, you can save a copy of this repository by clicking the green button "Clone or download" , then "Download Zip" button, and after by extracting the Zip file to your folder.
2. In the terminal window change directory CD to the correct file location(directory that you have just created)
3. Set up environment variables:
    - Create **.env** file in the root directory.
    - On the top of the file add `import os` to set the environment variables in the operating system.
    - Set the connection to your MongoDB database(MONGO_URI) and a SECRET_KEY with the following syntax:
    `os.environ["SECRET_KEY"] = "YourSecretKey"`   
    `os.environ["MONGO_URI"] = "YourMongoURI"`  
    .
4. Install all requirements from the **requirements.txt** file putting this command in your terminal:   
`pip3 install -r requirements.txt`  
*Note, GitPod does not require `sudo`, so if you use another IDE, you will need to include `sudo` in th beginning of the command: `sudo pip3 install -r requirements.txt`.*
5. Create a new Database called "MyCookBook" in [MongoDB Atlas](https://www.mongodb.com/). *You can sign up for free account, if you do not have one.*
6. In "MyCookBook" database create five following collections:
###### Cuisines
```
_id: <ObjectId>
cuisine_type: <String>
```
###### Meals
```
_id: <ObjectId>
meal_type: <String>
```
###### Diets
```
_id: <ObjectId>
diet_type: <String>
```
###### Users
```
_id: <ObjectId>
username: <String>
password: <String>
user_recipes: <Array>
```
###### Recipes
```
_id: <ObjectId>
recipe_name: <String>
description: <String>
cuisine_type: <String>
meal_type: <String>
cooking_time: <String>
diet_type: <String>
servings: <String>
ingredients: <Array>
directions: <Array>
author: <ObjectId>
image: <String>
```
7. You will now be able to run the application using the following command `python3 run.py`.   

### Heroku Deployment
To deploy the project to [Heroku](https://heroku.com/) the following steps need to be completed:
1. Create a **requirement.txt** file, which contains a list of the dependencies, using the following command in the terminal:  
`pip3 freeze > requirements.txt`
2. Create a **Procfile**, in order to tell Heroku how to run our project, using the following command in the terminal:   
`echo web: python run.py > Procfile`
3. `git add`, `git commit` and `git push` these files to GitHub repo
4. Create a **new app** in Heroku, assigning a name (must be unique) and set a region (for my project I set Europe)
5. From the heroku dashboard link the new Heroku app to your GitHub repository:    
    - "Deploy" - "Deployment method" - "GitHub"
6. In the **Settings** of the new Heroku app, 



---

## Credits

### Content
All recipes and recipes' images are taken from [BBC Good Food](https://www.bbcgoodfood.com/).
### Media
The project images are taken from the following sources:
- **Homepage background image** and **errorpage background image** : [Pixels](https://www.pexels.com/)
- **Favicon** : [Clipart-Library](http://clipart-library.com/)
- **Logo** : [Hatchful](https://hatchful.shopify.com/)
- **Background Image for forms** : [Unsplash](https://unsplash.com/), used for login, register, change username, change password pages.
- **Recipe placeholder** is taken from free available Google images. 

### Code
- **Flask Tutorials** - [Corey Schafer](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH) - Package structure, Blueprints, custom error pages, 
- **The Flask Mega-Tutorial** - [Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- **Flask WTForms Tutorials** - [Pretty Printed](https://www.youtube.com/watch?v=eu0tg4vgFr4&list=PLXmMXHVSvS-C_T5JWEDWIc9yEM3Hj52-1)

### Acknowledgements

---

**This is for educational use only.**
