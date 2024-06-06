#this is the index page of the web app

#import Flask class from flask package
from flask import Flask
from markupsafe import escape
from flask import render_template
from flask import url_for

# A list of dictionaries containing contents
posts =[{"title":"First Post",
         "author": "malvin",
         "date": "June 3, 2024",
         "content": " this is post no 1"
         },
        {"title":"Second Post",
         "author": "malini",
         "date": "June 4, 2024",
         "content": " this is post no 2"
         },
        {"title":"Third Post",
         "author": "chitra",
         "date": "June 5, 2024",
         "content": " this is post no 3"
         }
        ]

#instantiate flask
app = Flask(__name__)  # __name__ is a variable holding the app name

#define a route to trigger the below view_funtion for page rendering
@app.route("/")
@app.route("/home")
def home():
    welcome="<h1>Welcome to Vishnu Kshethram </h1>"
    return render_template("home_page.html", posts=posts)


#get the name of  any  user
@app.route("/name/<yourname>")
def show_name(yourname):
    return f"Hello, {escape(yourname)}!  Welcome"


#get age to show the convertor in parameter
@app.route("/age/<int:years>")
def get_age(years):
    return f"Your are {escape(years)} years old"


# testing templates functionlity
#create a function and map it to a URL
@app.route("/hello/")
@app.route("/hello/<person>")
def greet_person(person=None):
    urlfor1= url_for('show_name', yourname="vinodkumar")
    return render_template("greetings.html", name=person, ufr1=urlfor1, title="Greetings")


#testing Http Methods
#if get show login page else reload
@app.route("/login")
def login_page():
    return render_template("login_page.html")

# new login page
@app.route("/login_new")
def new_login():
    return render_template("login_page_1.html")

# About us pge
@app.route("/about")
def about_us():
    return render_template("about.html")
# app run
if __name__=="__main__":
    app.run(debug=True)
