import os
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static/user_uploads"

@app.route('/submit_form', methods=['GET', 'POST'])
def handle_form_submission():
    """This is the code that handles submitted forms"""
    if request.form:
        filename = request.form["filename"]

        if not filename.endswith(".jpg"):
            filename = filename + ".jpg"

        # Check if file exists
        if 'fileconent' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['fileconent']
        if file.filename == '': # Invalid file
            print('No selected file')
            return redirect(request.url)

        # Save file if it exists
        if file:
            # Should probably also check if file exists and refuse to override it
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect("/")


## The rest are helper functions, you don't need to modify these

@app.route('/')
def index():
    return render_template("file_uploader.jinja", user_files=get_current_files())

def get_current_files():
    """Gets the current files in /static/user_uploads"""
    current_files = []
    for filename in os.listdir("static/user_uploads"):
        current_files.append({
            "name":filename, 
            "path":os.path.join("static","user_uploads",filename)
        })
    return current_files

@app.route('/profile/1')
def get_profile():
    """This page will load the profile page of a user"""
    return render_template("profile.jinja")

if __name__ == '__main__':
    app.run(debug=True)