from flask import render_template, url_for, flash, redirect, request # import render_template function. url_for is a function that finds exact locations of routes for us. The request object from flask lets us access query parameters (from http://localhost:5000/login?next=%2Faccount)
from flask_blog import app, db, bcrypt
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog.models import User, Post # fix if coupled with "from __main__ import db" in models.py
from flask_login import login_user, logout_user, current_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    # create instance of form we will send to our application
    form = RegistrationForm()
    if form.validate_on_submit(): # Check if this is a new user and not an already existing one. Else we get sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) UNIQUE constraint failed: user.email. Ideally we add our own custom register form validation so it gets checked when we try to validate the form and we can give visual feedback of error messages to user, vs. doing database checks AFTER form is validated
        # First, hash password
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8") # decode converts from bytes to string
        # Create new instance of user
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created! You are now able to log in", "success")  # Add a flash message at the top
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form) # We have access to title and form inside our template

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    # create instance of form we will send to our application
    form = LoginForm()
    if form.validate_on_submit():
        # query database to make sure user exists when they log in via email
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data): # rehashing with same input using bcrypt.generate_password_hash() yields different results each time, so use check_password_hash with plaintext input
            login_user(user, remember=form.remember.data)
            # If we are not logged in and try to access account, we go to login route with url http://localhost:5000/login?next=%2Faccount. Use that account in url to go to account route after login
            next_page = request.args.get("next") # args is a dict, but args["next"] would be error if it doesn't exist. Use get and have default of home
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash("log in unsuccessful", "danger")
    return render_template("login.html", title="Login", form=form) # We have access to title and form inside our template

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/account")
@login_required
def account():
        return render_template("account.html", title="Account")

# Before we run app, we need to set environment variable to file we want to be our flask application. Here, export FLASK_APP=flask_blog.py
# localhost = 127.0.0.1