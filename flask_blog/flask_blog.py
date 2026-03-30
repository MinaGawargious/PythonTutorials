# Flask is a good microframeowrk that makes it easy to work with backend web apps

from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect # import Flask class and render_template function. url_for is a function that finds exact locations of routes for us
from flask_sqlalchemy import SQLAlchemy # In order to have real data instead of creating dummy data, we will use a database. SQLAlchemy is a popular ORM, or Object Relational Mapper and allows us to access database in object oriented way. It allows us to use different databases (SQLLite for testing vs PostGres for production) without changing Python code. All we need to do is pass in different database URL for SQLAlchemy to connect to.
# There is a regular sqlalchemy package, but flask_sqlalchemy is flask-specific extension that provides useful defaults and helpers for Flask application.
from forms import RegistrationForm, LoginForm
app = Flask(__name__) # app variable is instance of Flask class. Pass in __name__ so Flask knows where to look for templates and static files

# When we use these forms, we need to set a secret key for our app to protect against modifiying cookies and cross-site request forgery attacks
app.config["SECRET_KEY"] = "67a1d9a6ebd5246597e2c71085d9842b"
#import secrets; secrets.token_hex(16)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db' # Specify URI for database, which is where database is located. Here we do an SQLite database since it's easiest to get up and running with. SQLite database is just a file on our file system. /// means relative path from current file
db = SQLAlchemy(app) # SQLAlchemy database instance
# In SQLAlchemy, we can represent database structures as classes, otherwise called models. Each class will be its own table in the databse

# Create database in terminal by doing "from flask_blog import db, app" followed by "with app.app_context(): db.create_all()"
class User(db.Model): # subclass of db.Model
    # columns to table
    id = db.Column(db.Integer, primary_key = True) # Specify type, and primary_key means unique id for our user assigned automatically.
    username = db.Column(db.String(20), unique=True, nullable=False) # max 20 character string that is unique and required (not nullable) (FIXME: What about min length of 2?)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg") # we will hash these image files that are 20 characters long so that they are unique (so one user changing to test.jpg doesn't change another user's image that happens to be named test.jpg too, right?). Alternatively, we could append a unique identifier, like username or id I assume. Default means we don't need to assign one at instantiation (but we can)
    password = db.Column(db.String(60), nullable=False) # Corey says hashing algorithm we use will make passwords 60 characters long. This will be stored in database instead of plaintext
    posts = db.relationship("Post", backref="author", lazy=True) # Users and Posts have a 1-to-many relationship. Users will author posts. 1 user can have multiple posts, but a post can only have 1 author. Here, we're saying posts attribute has a relationship to Post model. backref is like adding another column to the Post model that allows us to use author attribute to get user who wrote this post. lazy defines when SQLAlchemy loads data from database. True means SQLAlchemy loads data as necessary in 1 go. We can now use this posts attribute to get all the posts created by a user, and use author reference to get this user object.
    # Note, this is relationship, not a column, so if we were to open database structure sql client, we won't see this as a column. This just runs additional query in the background that gets all posts user has created.
    
    def __repr__(self): # For printing
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # don't call utcnow(), pass in the function itself not the current time now when we run the code. So the function will be run when we make a post, not when we run this code
    content = db.Column(db.Text, nullable=False) # db.Text vs db.String()?
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False) # Id of user who authored post. user with lowercase u since we are referencing table name and column name (User model has table name set to user with lowercase u, and Post model has table name set to post with lowercase p). But in User class's posts, we use the Post class name with capital P
    
    def __repr__(self): # For printing
        return f"Post('{self.title}', '{self.date_posted}')"

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