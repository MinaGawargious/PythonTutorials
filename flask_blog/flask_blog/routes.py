from flask import render_template, url_for, flash, redirect, request, abort # import render_template function. url_for is a function that finds exact locations of routes for us. The request object from flask lets us access query parameters (from http://localhost:5000/login?next=%2Faccount)
from flask_blog import app, db, bcrypt
from flask_blog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from flask_blog.models import User, Post # fix if coupled with "from __main__ import db" in models.py
from flask_login import login_user, logout_user, current_user, login_required
import secrets, os
from PIL import Image

@app.route("/") # routes are what we type into browser to go to different pages, like about or contacts. @app.route() decorator handles all the complicated stuff and allows us to write a function that returns information to be shown for this specific route. / is root/home page
@app.route("/home") # Multiple routes handled by same function is easy. Just add another decorator
def home():
    posts = Post.query.all()
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

# Save user's image that they uploaded to our filesystem/database
def save_picture(form_picture):
    # We want unique image names to avoid collisions. Randomize the name of image with random hex
    random_hex = secrets.token_hex(8) # 8 byes
    file_name, file_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + file_ext
    # Get root path of our app all the way to our package directory
    picture_path = os.path.join(app.root_path, "static/profile_pics", picture_filename)
    
    # We resize it in CSS to 125 px anyway, so no need to store full size image on server and take up space and slow down site
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    
    i.save(picture_path) # saved image to filesystem
    return picture_filename

@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        # picture is not a required field and does not have default preset, so check manually here:
        if form.picture.data:
            picture_filename = save_picture(form.picture.data)
            current_user.image_file = picture_filename
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your account has been updated!", "success")
        return redirect(url_for("account")) # Don't let it fall to render_template to avoid POST-GET-REDIRECT pattern. This is that popup when we refresh a page that says "Are you sure you want to reload? Data will be resubmitted". This means we will run another post request when we refresh our page. Redirecting sends a get request instead.
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for("static", filename="profile_pics/" + current_user.image_file)
    return render_template("account.html", title="Account", image_file=image_file, form=form)

@app.route("/post/new", methods=["GET", "POST"])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title = form.title.data, content = form.content.data, author=current_user) # Use author backreference instead of setting user id. Could do either. Cleaner this way
        db.session.add(post)
        db.session.commit() 
        flash("Your post has been created!", "success")
        return redirect(url_for("home"))
    return render_template("create_post.html", title="New Post", form=form, legend="New Post")

# Flask gives us the ability to add variables in our routes. Here, we create route where id of post is part of route
@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post.html", title=post.title, post=post)

@app.route("/post/<int:post_id>/update", methods=["GET", "POST"])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403) # HTTP response for forbidden route
    form = PostForm()
    
    # For a POST:
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit() # No need to do db.session.add since they're already in database. Just update
        flash("Your post has been updated!", "success")
        return redirect(url_for("post", post_id=post.id))
    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
    return render_template("create_post.html", title="Update Post", form=form, legend="Update Post")
    
@app.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403) # HTTP response for forbidden route
    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted!", "success")
    return redirect(url_for("home"))
    

# Before we run app, we need to set environment variable to file we want to be our flask application. Here, export FLASK_APP=flask_blog.py
# localhost = 127.0.0.1