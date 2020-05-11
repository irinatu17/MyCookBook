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

Wireframes for both desktop and mobile devices can be found [here]().

---

## Features
### Existing Features
#### Navbar

### Features Left to Implement

---

## Technologies Used

- [GitPod](https://www.gitpod.io/) - online IDE for developing this project.
- [Git](https://git-scm.com/) - for version control.
- [GitHub](https://git-scm.com/) - for remotely storing project's code.
- [PIP](https://pip.pypa.io/en/stable/installing/) - for installation of necessary tools.
- [GIMP2](https://www.gimp.org/) - for editing, compressing and resizing images.
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

### Validators

### Compatibility



---

## Deployment
### Local Deployment

### Remote Deployment

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
