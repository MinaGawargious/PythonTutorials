# Flask is a good microframeowrk that makes it easy to work with backend web apps

from flask import Flask, render_template, url_for, flash, redirect # import Flask class and render_template function. url_for is a function that finds exact locations of routes for us
from forms import RegistrationForm, LoginForm
app = Flask(__name__) # app variable is instance of Flask class. Pass in __name__ so Flask knows where to look for templates and static files

# When we use these forms, we need to set a secret key for our app to protect against modifiying cookies and cross-site request forgery attacks
app.config["SECRET_KEY"] = "67a1d9a6ebd5246597e2c71085d9842b"
#import secrets; secrets.token_hex(16)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/") # routes are what we type into browser to go to different pages, like about or contacts. @app.route() decorator handles all the complicated stuff and allows us to write a function that returns information to be shown for this specific route. / is root/home page
@app.route("/home") # Multiple routes handled by same function is easy. Just add another decorator
def home():
    # Webpages are more complex than this. Instead of having multi-line string, which has the potential of repeated HTML, we should instead use templates
    return render_template("home.html", posts=posts) # We will now have access to any variables we pass here inside our home.html. So we have access to posts and title

@app.route("/about")
def about():
    return render_template("about.html", title="About Page")

@app.route("/register", methods=["GET", "POST"])
def registration():
    # create instance of form we will send to our application
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")  # Add a flash message at the top
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form) # We have access to title and form inside our template

@app.route("/login", methods=["GET", "POST"])
def login():
    # create instance of form we will send to our application
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            # simulate successful login
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("log in unsuccessful", "danger")
    return render_template("login.html", title="Login", form=form) # We have access to title and form inside our template

# Before we run app, we need to set environment variable to file we want to be our flask application. Here, export FLASK_APP=flask_blog.py
# localhost = 127.0.0.1

# If we don't want to work with environment variables or flask run. Now we can do python flask_blog.py
if __name__ == "__main__":
    app.run(debug=True)