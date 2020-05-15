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
    - [Heroku Deployment](#heroku-deployment)

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
The navbar is fixed at the top of the page, this allows a user to easily navigate throughout the website. The logo is located in the top right corner on a desktop and in the center on smaller devices. It redirects the user to the home page when clicked.
On the smaller resolutions (tablet, mobile) the navbar is collapsed into a burger icon. A slide out menu opens when the burger icon is clicked.     

For **non-logged in** users or **guests** navbar contains the following links:
- Home
- Browse Recipes
- Login
- Register    
   
For **logged-in** users navbar contains the following links:
- Home
- Browse Recipes
- Account (it is a dropdown on a desktop)
    - My Recipes
    - Add Recipe
    - Settings
- Logout
#### Home page and Featured Recipes
The home page contains a button that redirects a user to the "All Recipes" page. It also displays 4 random images from 
the database using the `$sample` function of MongoDB. 
#### Browse All Recipes
The all recipes page displays recipe cards sorted from the oldest to the most recently added. As well as that, there is a total number of recipes displayed in parentheses after the heading.
All recipe cards are clickable and redirect a user to the individual recipe page with detailed information.
The pagination at the bottom of the page allows to display 8 recipes per page.
#### Single Recipe details
The single recipe details page renders when user clicks on the recipe card. It displays information about the selected recipe:
recipe name, description, cuisine type, meal type, diet type, number of servings, cooking time, author, ingredients, directions and recipe image (or recipe placeholder if no image was added by user).
If the user is an author of the recipe, there are buttons "Edit" and "Delete", that redirect to the edit and delete recipe pages, respectively.
#### Register
The register page allows a user to create a new account. The user is asked to fill the fields "username", "password" and "confirm password".
When adding a username, the code compares it against existing usernames to ensure that it is unique. A username must be 3-15 characters long. The same requirement applies to the password field.
The "confirm password" field must match the original password. All passwords are hashed for security purposes. If user's input does not meet requirements, flash messages will inform a user about the error.
When the form is submitted successfully, a user is redirected to the home page and informed that account was created.
There is also a link to the login page for existing users at the bottom of the form.
#### Login
The login page features the form with "username" and "password" fields, allowing registered users to log into their account.
If the entered username and hashed password match the ones in the database, a user is redirected to the home page and informed that the  log in was successful. Otherwise, flash messages will be displayed about incorrect user's input.
There is also a link to the register page for new users at the bottom of the form.
#### Logout 
Hitting "logout" button by the logged in users ends their session and redirects to the homepage.
#### My recipes
My recipes page allows registered users to view all their recipes. It also displays the total number of all the user's recipes. Below that there is a button "Add new recipe" taht redirects a user to the "Add recipe" page.
Pagination is in place displaying 8 recipes per page. If user has not created any recipes yet, there's a message that asks a user to create one.
#### Add Recipe
The registered and logged in users can add new recipes through the form. There are some validations in place - all the fields except "Cuisine type", "Diet type" and "Recipe Image" are required. For the "recipe name" and "recipe description" fields, limit of characters is set.
If user does not provide a URL to the recipe image, the recipe placeholder will be assigned for that recipe. There is also a Tooltip-instruction saying that a user can upload the image to a free image hosting website(e.g. ImgBB).   
After the succsessful addition, a user is redirected to the newly created recipe details page. There is also a button "Cancel" that simply redirects a user to the home page (in order to avoid to hit "back" button in a browser).
#### Edit Recipe
The edit recipe page allows the logged in user to update information about the recipe. The "Edit" button will appear only for the author of the recipe.   
As well as that, the defensive design (against brute-forcing) in place allows only author of the recipe to make changes. 
The form is pre-populated with the original recipe's details. After clicking "Edit recipe" button, the recipe is updated in the database and a user is redirected to the details page of the updated recipe.   
There is also a button "Cancel" that simply redirects a user to the home page (in order to avoid to hit "back" button in a browser)
#### Delete Recipe
The delete recipe function allows only author of the recipe to delete it. After a user clicks the "delete" button in a Single Recipe Details page, the modal will be opened. It asks a user to confirm if the recipe is to be deleted. 
If so, upon clicking "delete" button the recipe will be removed from the database as well as from the "user_recipes" field of the recipe's author in "users" collection. There is also a button "cancel" that closes the modal when it's clicked.
#### Account Settings page
The Account Settings page contains username, randomly generated user avatar with a greeting and 3 buttons: "Change username", "Change password" and "Delete account". These buttons redirect a user to the corresponding page.
#### Change username
The Change Username form displayed allows the registered user to change their username. It checks if the new entered username is present in the database. The current username is displayed above the new username field. There is also a question mark that displays requirements for the field when hovered over. After succsessfull submission, it redirects a user to the login page asking to log in with a new username. There is also a button "Cancel" that simply redirects a user to the account settings page.
#### Change password
A user can change their current password by filling the form that contains following fields: "Current password", "New password", "Confirm New password".
Both new password have to match and be 3-15 characters long. There is a question mark that displays requirements for the field when hovered over. If the form is successfully submitted, a user is redirected to the account settings page with a flash message about successfully changed password. There is also a button "Cancel" that simply redirects a user to the account settings page.
#### Delete account
Once the "delete account" button on the account settings page is clicked, the modal shows up asking to confirm if the user certainly wants to delete their account. To verify this, user has to provide the password. After clicking the "delete account" button, the account is removed from the "users" collection. All the recipes created by this user are removed from the "recipes" collection as well. There is also a button "Cancel" that closes the modal.
#### Footer
The footer features links to the social media which open in a new tab (by using `'target="_blank"`). 
#### 404 and 500 error pages
Customized 404 and 500 pages contain short information about the error and a button "Back Home". As well as that, they display navbar that allows users to come back easily to any page if they got lost.

### Features Left to Implement
There are some features that I considered were of secondary importance and I have not implemented them yet due to time constraints, but would like to do so in future.
Both of these features are displayed in my initial wireframes.
#### Search recipe
The search recipe function is based on the keyword and recipe name, allowing user to search for the recipe. Filters "by cuisine", "by meal type" and "by diet type" would allow user to have more detailed search.
#### My favourites
User would have an opportunity to "like" other recipes, saving them in "my favourites" collection, which would be displayed on a separate page.
Each recipe card will include a small "heart" icon, clicking which will enable user to add the selected recipe to "my favourits".

---

## Technologies Used

- [GitPod](https://www.gitpod.io/) - an online IDE for developing this project.
- [Git](https://git-scm.com/) - for version control.
- [GitHub](https://git-scm.com/) - for remotely storing project's code.
- [PIP](https://pip.pypa.io/en/stable/installing/) - for installation of necessary tools.
- [GIMP2](https://www.gimp.org/) - for editing, compressing and resizing images.
- [Am I Responsive](http://ami.responsivedesign.is/) - for creation of the images in the readme file and checking responsiveness.
### Front-End
- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - to build the foundation of the project.
- [CSS](https://developer.mozilla.org/en-US/docs/Archive/CSS3) - to create custom styles.
### Back-End
- [Python 3.8.2](https://www.python.org/) -  back-end programming language used in this project.
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
#### User stories testing
All the following manual testing was implemented on both desktop and mobile devices.
##### All recipes and single recipe display
When I click on "All Recipe page", I can see recipe cards display in rows, 8 recipes per page. From that view, I can see image, recipe name and short information about the recipe.
Clicking on the recipe cards, redirects me to the single recipe page, where I can see all detailed information about the recipe. I tested this functionality as a non-logged in (guest) user and logged-in user and it perfectly works in both cases.
I also can see the total number of the recipes in parentheses. I tried to add and delete some recipes, and this total number changes accordingly.
##### Create a new user account
I created my own main account, as well as few testing accounts to test this functionality. Clicking on "Register" button in the navbar opens the form, where I can put username and password to create a new account. I tried to put an existing username, different passwords in "password" and "confirm password" fields, put less then 3 or more then 15 charachters.
In all cases I got corresponding flash error message. As well as that, I tried to leave an empty field and submit the form, but got an error message again asking to fill the field. When the form was successfully submitted, I was redirected to the home page, seeing a message that my new account was created. 
I also checked the link to the Login page at the bottom of the form, which workes well. 
##### Login
Clicking on "Login" button in the navbar opens the form, allowing me to login to my account. I checked validation against empty fields or incorrect details, so I was not able to submit the form if somemething was entered incorrectly. After successful login I was redirected to the home page, seeing the message that I was logged in. 
I also checked the link to the Register page at the bottom of the form, which workes well.
##### Change username/password
To test it I changed my username and password multiple times to ensure that functionality woeks well. Both pages opens when the corresponding buttons are clicked. Validations against existing username and against incorrect input works well. 
In both forms I can see the flash messages about changes I made. As well as that, If I click "Cancel" button, I will be redirected to the "Account Settings" page.
For "change username" function, I checked database to make sure that username was updated there.  
##### Delete Account
I deleted some testing accounts to test the functionality. Clicking the "Delete account" button on the Account Settings page, the modal opens and I am asked to confirm the deletion by entering my password. I tried to put the wrong password, but got a flash message. 
When I input the correct password, I am redirected to the home page and see the message that my account was deleted. After I checked the database to make sure that the account was removed, as well as all the recipes created by this user.
##### Add New Recipe
I added plenty of test recipes with to check  the functionality throughout the development.  If I leave some of the required fields empty, I am not able to submit the form. I can see flash messages displayed if I my input does not meet lenght requirement. I also tried to create recipe without the URL image provided to check if the placeholder is in place and it works well.
##### Edit Recipe
If I am the author of selected recipe, I can see the buttons "Edit" and "Delete" in the single_recipe page. I tried to view someone else's recipes and the buttons were not displays. I also tried to change the link manually to edit other's recipe. However, I was not able to open the form and got the message, that I can only edit my own recipes, which means defensive design works well against brute forcing.
Being the author of the recipe, I can view the form with pre-populated fields and can change anything that I want. If all fields valid, after submission I can see tha changes I made in a Single Recipe Details Page. I tried to edit a number of recipes and edit different fields, everything works correctly.
##### Delete Recipe
I deleted some dummy testing recipes to test the functionality. After clicking "delete" button,  I can see the modal showed up asking me to confirm the deletion. Clicking "Cancel" I am redirected back and modal closes. After clicking "Delete" button in the modal, I am redirected to the home page and can see the message about the succsessful delition.  
Then I checked the database to make sure, that the recipe was removed. As well as that I tested against brute-forcing, trying to delete another user's recipe(by changing the link manually), but wasn't able to do that.
##### My Recipes
The link in the navbar leads to My Recipes page, where I can see the total number of my recipes, recipes cards, "Add New Recipe" button and pagination in place. I tested it by clicking the buttons in pagination, by creating/deleting a recipe to check total number. All functionality works well.
##### 404 and 500 errors
I manually changed URL to get a non-existing page or page, which I do not have rights to access, to test error pages. In both cases cutom pages renders and all links in navbar and the button "Back Home" work well.
##### Navbar/ Footer
All links in navbar and footer were manually tested to ensure that they are pointing to the correct destination.


Apart from that, I also manually tested the app with **debugger**: `debug=True` throughout all development process. 
So every time when there was an error (when app crashed), debugger displayed an error message to the view, that allowed me to find the location of the error and fix it.
#### Further testing
I also asked my friends, family members and fellow students in Slack to thoroughly test my website in all possible deviced. So, a number of new accounts were created and new recipes added/editted and some of them then deleted. 
At that stage I got useful feedback and few issues were found out: 
##### Knowing bugs
 - The text of the "Delete" and "Edit" buttons desappear on the smaller devices(320px size), so I added media query to fix this issue
 - There was a similar issue with "Change username", "Change password" buttons, to solve it I removed "buttons-container" class to increase width of the buttons dividers
 - I was adviced to make "Add Recipe" button more visible to the user, as it was dicplayed only on the navbar deopdown. To fix that, I added "Add new recipe" button to the "My Recipes" page above the recipes cards. Also I added icons in the navbar dropdown to give a user visual clue about the links.
 - I also added a small-greeting text above the user avtar in "Account Settings" to make it more user-friendly as some users did not understand "what does this face means".
### Validators
#### Html
All HTML files were tested through [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input). Since it does not recognize Jinja2 templating language, it shows a number of errors. Apart from that, no other error was found across html pages.
#### CSS
CSS files were tested through [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). Since it does not recognize CSS variables (I use `:root{}` for colours and fonts variables), there are several Parse Errors found.  
 As well as that, there are few error warnings for some -webkit, -moz pseudo element selectors. Both of the error can be safely ignored as they are not errors in fact. The rest of the CSS files was completely valid.
#### JavaScript
JS file was tested through [Esprima](https://esprima.org/demo/validate.html) and [JSHint](https://jshint.com/) validators, code was syntactically valid.  "$" was not defined by JSHint (it is necessary for jQuery Materialize initializing).
#### Python
All python files were tested through [PEP8 Online](http://pep8online.com/) validator and were completely PEP8 compliant, 
except one thing:   
- in "_init_.py" file, the following import `from mycookbook import routes` has to be located at the bottom of the file
as it needs to import routes after the app has been initialised
to prevent circular imports.

### Compatibility and Responsivesness
This website were been testing during the development across **multiple browsers** (Chrome, Safary, Opera, FireFox, Internet Explorer) and on **multiple devices**: mobile (iPhone 5, 6, 8, Samsung Galaxy, Sony Xperia), tablets(iPad) and laptops (with HiDPI and MDPI and touch screens).
As well as on **Google Chrome's developer tools** to see how it looks across all the different device screen sizes to ensure compatibility and responsiveness.
I also used [Am I Responsive](http://ami.responsivedesign.is/) online tool for checking responsiveness on different devices.
Plenty of changes were made and necessary media queries added to make the website fully responsive. 
The one noticed issue was found that website renders poorly on Internet Explorer browser(as it is outdated). However the website renders well as expected on the modern browsers.

---

## Deployment
### Local Deployment
To be able to run this project, the following tools have to be installed:
- An IDE  (I used [GitPod](https://www.gitpod.io/) online IDE for creating this project)
- [MongoDB Atlas](https://www.mongodb.com/) (for creation your database)
- [Git](https://git-scm.com/)
- [PIP](https://pip.pypa.io/en/stable/installing/) 
- [Python](https://www.python.org/)   
#### Directions
1. You can clone this repository directly into the editor of your choice by pasting the following command into the terminal:   
`git clone https://github.com/irinatu17/MyCookBook`    
Alternatively, you can save a copy of this repository by clicking the green button "Clone or download" , then "Download Zip" button, and after extract the Zip file to your folder.
2. In the terminal window change directory (CD) to the correct file location (directory that you have just created).
3. Set up environment variables:
    - Create **.env** file in the root directory.
    - On the top of the file add `import os` to set the environment variables in the operating system.
    - Set the connection to your MongoDB database(MONGO_URI) and a SECRET_KEY with the following syntax:
    `os.environ["SECRET_KEY"] = "YourSecretKey"`   
    `os.environ["MONGO_URI"] = "YourMongoURI"`  
    .
4. Install all requirements from the **requirements.txt** file putting this command into your terminal:   
`pip3 install -r requirements.txt`  
*Note: GitPod does not require `sudo`, so if you use another IDE, you will need to include `sudo` in the beginning of the command: `sudo pip3 install -r requirements.txt`.*
5. Create a new Database called "MyCookBook" in [MongoDB Atlas](https://www.mongodb.com/).   
*You can sign up for free account, if you do not have one.*
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
2. Create a **Procfile**, in order to tell Heroku how to run the project, using the following command in the terminal:   
`echo web: python run.py > Procfile`
3. `git add`, `git commit` and `git push` these files to GitHub repository
4. Create a **new app** in Heroku, assigning a name (must be unique) and set a region (for my project I set Europe)
5. From the Heroku dashboard link the new Heroku app to your GitHub repository:    
    - "Deploy" -> "Deployment method" -> "GitHub"
    - then "Enable automatic deployment"
6. To start the web process, put the following command into the terminal: `heroku ps:scale web=1` to scale dynos
7. In the **Settings** tab of the new Heroku app, click on "Reveal Config Vars" and set the following config vars:
    - **IP** : 0.0.0.0
    - **PORT** : 8080
    - **MONGO_URI** : `<link to your MongoDB database>`
    - **SECRET_KEY** : `<your secret key>`
    - **DEBUG**: **FALSE**  
*Note: your MONGO_URI and SECRET_KEY must match the ones you entered in .env.py file*

8. The app will be deployed and ready to run. Click "Open App" to view the app.   

**Note**: if you have not linked GitHub and Heroku following step N.5, alternatively as the last step of deployment, you can put the following command into your terminal:   
 `heroku login`, after a successful log in `git push heroku master` - to push the app to Heroku, and finally click "Open App" in Heroku dashboard to view the app.




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
