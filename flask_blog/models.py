# from flask_blog import db # ImportError: cannot import name 'User' from partially initialized module 'models' (most likely due to a circular import)
from __main__ import db # ImportError: cannot import name 'db' from '__main__'
from datetime import datetime

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