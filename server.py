# Import FlaskLibrary
from flask import Flask, render_template, url_for, request, redirect
import requests
import csv

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

# With this method we grab data from the sender and we store it in a txt file!
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/formSubmitted.html')
        except:
            return 'did not save to database..'
    else:
        return 'something went wrong. Try again!'

# in this way we'll store in a txt file
# def write_to_file(data):
#     with open ('./database.txt', 'a') as database:
#             database.write(f"-------\nEmail: {data['email']}\nSubject: {data['subject']}\nMessage: {data['message']}\n\n-------")

def write_to_csv(data):
    with open ('./database.csv', 'a', newline='') as database2:
            csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([data['email'],data['subject'],data['message']])

