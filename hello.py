#this is the index page of the web app

#import Flask class from flask package
from flask import Flask, render_template, url_for, flash, redirect
from markupsafe import escape
from forms import RegistrationForm, LoginForm




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
app.config["SECRET_KEY"]="b8e4b083ca949e1ae4678e1f8e75831e7ba40ad850b2525a609c42f719c30ea8"

#define a route to trigger the below view_funtion for page rendering
@app.route("/")
@app.route("/home")
def home():
    welcome="Welcome to Vishnu Kshethram"
    return render_template("home_page.html", posts=posts, welcome=welcome)

# About us pge
@app.route("/about")
def about_us():
    return render_template("about.html")

# Registration Page
@app.route("/register", methods=['GET', 'POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f"User Created Successfully. {form.username.data}")
        return redirect(url_for("login"))
    return render_template("register_page.html", form=form)

#Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=="malvinchi@gmail.com" and  form.password.data=="Chitra@06" :
            flash(f"You are logged in")
            return redirect(url_for("home"))
        else:
            flash(f"Lofgin Unsuccesful")
    return render_template("login_page_1.html", form=form)



####################@@@@@@@@@@@@@@@@@@@@@!!!!!!!!!!#############
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

# app run
if __name__=="__main__":
    app.run(host="0.0.0.0", port=6000, debug=True)
