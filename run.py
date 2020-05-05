import os
from flask import Flask, render_template, url_for, flash, redirect

if os.path.exists("env.py"):
   import env

app = Flask(__name__)

app.config['MONGODB_NAME'] = os.environ.get('MONGODB_NAME')
app.config['MONGODB_URI'] = os.environ.get('MONGODB_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@app.route("/")
def test():
    return "Hello world"

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True) 