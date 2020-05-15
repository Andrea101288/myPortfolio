# Import FlaskLibrary
from flask import Flask, render_template, url_for
import requests

# We use the flask class to instanciate a class
app = Flask(__name__)
print(__name__)

# this is a Decorator! We already saw it
@app.route('/')
def my_home():    
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):    
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    return 'form submitted hooooray'



