# This is where we initialize our application and bring together different components

# Flask is a good microframeowrk that makes it easy to work with backend web apps

from flask import Flask, render_template, url_for, flash, redirect # import Flask class and render_template function. url_for is a function that finds exact locations of routes for us
from flask_sqlalchemy import SQLAlchemy # In order to have real data instead of creating dummy data, we will use a database. SQLAlchemy is a popular ORM, or Object Relational Mapper and allows us to access database in object oriented way. It allows us to use different databases (SQLLite for testing vs PostGres for production) without changing Python code. All we need to do is pass in different database URL for SQLAlchemy to connect to.
# There is a regular sqlalchemy package, but flask_sqlalchemy is flask-specific extension that provides useful defaults and helpers for Flask application.
from forms import RegistrationForm, LoginForm
from models import User, Post # Circular import. ImportError: cannot import name 'User' from partially initialized module 'models' (most likely due to a circular import) (/mnt/c/Users/MinaG/Python Tutorials/flask_blog/models.py)
# The issue is this: when running python3 flask_blog.py, it is called __main__. So we run __main__, and go to this import. When we import, we run the ENTIRE import file. The first line is from flask_blog import db. Since it was called __main__ when we ran it, python RERUNS this flask_blog file, and hits this import but has not yet seen User class since it's below the "from flask_blog import db" line, so it throws that error.
# If we instead change models.py's "from flask_blog import db" to "from __main__ import db", it will fail at "ImportError: cannot import name 'db' from '__main__'" instead. Can fix by moving this import below db variable
# Better solution is to set up the code in a way where we don't run flask_blog directly so it doesn't get that __main__ name. We do this by turning application into package to simplify imports and separate things out better. To tell Python that our directory is a package, we need to create a __init__ file.
app = Flask(__name__) # app variable is instance of Flask class. Pass in __name__ so Flask knows where to look for templates and static files

# When we use these forms, we need to set a secret key for our app to protect against modifiying cookies and cross-site request forgery attacks
app.config["SECRET_KEY"] = "67a1d9a6ebd5246597e2c71085d9842b"
#import secrets; secrets.token_hex(16)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db' # Specify URI for database, which is where database is located. Here we do an SQLite database since it's easiest to get up and running with. SQLite database is just a file on our file system. /// means relative path from current file
db = SQLAlchemy(app) # SQLAlchemy database instance
# In SQLAlchemy, we can represent database structures as classes, otherwise called models. Each class will be its own table in the databse
