from flask import Flask, render_template, request, redirect
import json
import os
from werkzeug.utils import secure_filename
#Outlined here is the code you'll need to add to make the site complete. Add the required code below the comments!

#instantiate flask app, you'll also want to add file handling here
app = Flask(__name__)


#Route Handling
#Level 1 Code: Profile Page
#Extra: add extra logic here to handle searching for profiles that don't exist


#LEVEL 2 Code: home/explore page
@app.route('/')
def index():
    return render_template("explore.jinja")

#LEVEL 3 Code (part 1): Sign Up Page to create a profile
#handle get requests to send back the form page, and post requests to handle submission of the form
#Extra: include logic to provide a default profile picture if one is not submitted


#Level 3 (Part 2): Create post page that adds post to a profile
#I added a post Title but note this is not actually needed based on requirements, it's just something extra and fun
#like above, you'll need to handle get requests to get the form, and post requests to handle it's submission


#Extra: 404 Routing
#routing for 404 for page that doesn't exist


if __name__ == '__main__':
    app.run(debug=True)