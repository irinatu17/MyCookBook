from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo


class RegisterForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=3, max=15)])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(min=3, max=15)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=3, max=15)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class ChangeUsernameForm(FlaskForm):
    new_username = StringField('New Username',
                               validators=[DataRequired(),
                                           Length(min=3, max=15)])

    submit = SubmitField('Change Username')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Current Password',
                                 validators=[DataRequired(),
                                             Length(min=3, max=15)])
    new_password = PasswordField('New Password', validators=[DataRequired(),
                                                             Length(min=3,
                                                                    max=15)])
    confirm_new_password = PasswordField('Confirm New Password',
                                         validators=[DataRequired(),
                                                     Length(min=3, max=15)])
    submit = SubmitField('Change Password')


class AddRecipe(FlaskForm):
    recipe_name = StringField('Recipe Name',
                              validators=[DataRequired(),
                                          Length(min=3, max=25)])
    recipe_description = TextAreaField('Recipe Description',
                                       validators=[DataRequired(),
                                                   Length(min=20, max=300)])
    cooking_time = IntegerField('Cooking Time', validators=[DataRequired()])
    servings = IntegerField('Number of Servings', validators=[DataRequired()])
    image = StringField('Recipe Image')
    ingredients = TextAreaField('Ingredients',
                                validators=[DataRequired()])
    directions = TextAreaField('Directions',
                               validators=[DataRequired()])
    cuisine_type = SelectField('Cuisine Type')
    meal_type = SelectField('Meal Type')
    diet_type = SelectField('Diet Type')
    submit = SubmitField('Add Recipe')
