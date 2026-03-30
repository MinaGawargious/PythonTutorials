# This is where we initialize our application and bring together different components

# Flask is a good microframeowrk that makes it easy to work with backend web apps

from flask import Flask # import Flask class and render_template function. url_for is a function that finds exact locations of routes for us
from flask_sqlalchemy import SQLAlchemy # In order to have real data instead of creating dummy data, we will use a database. SQLAlchemy is a popular ORM, or Object Relational Mapper and allows us to access database in object oriented way. It allows us to use different databases (SQLLite for testing vs PostGres for production) without changing Python code. All we need to do is pass in different database URL for SQLAlchemy to connect to.
# There is a regular sqlalchemy package, but flask_sqlalchemy is flask-specific extension that provides useful defaults and helpers for Flask application.
app = Flask(__name__) # app variable is instance of Flask class. Pass in __name__ so Flask knows where to look for templates and static files

# When we use these forms, we need to set a secret key for our app to protect against modifiying cookies and cross-site request forgery attacks
app.config["SECRET_KEY"] = "67a1d9a6ebd5246597e2c71085d9842b"
#import secrets; secrets.token_hex(16)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db' # Specify URI for database, which is where database is located. Here we do an SQLite database since it's easiest to get up and running with. SQLite database is just a file on our file system. /// means relative path from current file
db = SQLAlchemy(app) # SQLAlchemy database instance
# In SQLAlchemy, we can represent database structures as classes, otherwise called models. Each class will be its own table in the databse

from flask_blog import routes # Do it here to avoid circular import error with the app variable