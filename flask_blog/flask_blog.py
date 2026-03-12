# Flask is a good microframeowrk that makes it easy to work with backend web apps

from flask import Flask # import Flask class
app = Flask(__name__) # app variable is instance of Flask class. Pass in __name__ so Flask knows where to look for templates and static files

@app.route("/") # routes are what we type into browser to go to different pages, like about or contacts. @app.route() decorator handles all the complicated stuff and allows us to write a function that returns information to be shown for this specific route. / is root/home page
@app.route("/home") # Multiple routes handled by same function is easy. Just add another decorator
def home():
    return "<h1>Home Page</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

# Before we run app, we need to set environment variable to file we want to be our flask application. Here, export FLASK_APP=flask_blog.py
# localhost = 127.0.0.1

# If we don't want to work with environment variables or flask run. Now we can do python flask_blog.py
if __name__ == "__main__":
    app.run(debug=True)