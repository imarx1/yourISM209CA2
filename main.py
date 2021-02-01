
from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/classDF'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route("/register/")
def register():
 return render_template('register.html', title="Register", information="Use the form displayed to register")

@app.route("/")
def home():
  return render_template('home.html', title="Home")


 # Let's get the request object and extract the parameters sent into local variables.

 firstname = request.form['firstname']
lastname = request.form['lastname']
othernames = request.form['othernames']
DOB = request.form['DOB']
Residentialadress = request.form['residentialadress']
nationality = request.form['nationality']
NIN= request.form['NIN']

 # let's write to the database
 try:
  user = .User(firstname=firstname, lastname=lastname, othernames=othernames, DOB=DOB,  Residentaladdress=Residentialadress, nationality=nationality, NIN=NIN)
  db.session.commit()

 except Exception as e:
  # Error caught, prepare error information for return
  information = 'Could not submit. The error message is {}'.format(e.__cause__)
  return render_template ('register.html', title="register", information="information")

  # If we have gotten to this point, it means that database write has been successful. Let us compose success info

  # Let us prepare success feedback information


 return render_template("register.html", title = "register", information=information)

if __name__ == "__main__":
 app.run(port=5432)  # here we are using a different port so as not to conflict with that allocated to our helloworld.py


