import os
from flask import Flask, render_template, url_for, flash, redirect
app = Flask(__name__)


@app.route("/")
def test():
    return "Hello world"

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True) 