import random
import string
from flask import Flask, render_template, redirect, render_template_string, request

app = Flask(__name__)


comments = [ # List of all comments, added to by send_comment()
    {
        "name": "John Doe",
        "comment": "This post was <strong>dope</strong>"
    },
    {
        "name": "Jane Doe",
        "comment": "I've never wished I <em>couldn't</em> read so much in my life"
    },
    
    {
        "name": "Mr.R0507",
        "comment": "Hehe got your password: {{user.password}}, if you want it back send $20 to my paypal"
    },
    
    {
        "name": "Fedora1967",
        "comment": "All the passwords! {%for current_user in users%} {{current_user.name}}: {{current_user.password}} <br>{%endfor%}"
    },
]

users = [ # List of all users, added to by send_comment()
    {
        "name": "John Doe",
        "password": "P4ssW0rd"
    },
    {
        "name": "Jane Doe",
        "password": "Maxy2021"
    },
    {
        "name": "Mr.R0507",
        "password":"give_me_the_passwords"
    },
    {
        "name": "Fedora1967",
        "password":"lol_i'm_not_giving_you_my_pw"
    }
]

@app.route('/post')
def get_post():
    """Gets the only post in the system"""
    return render_template("post.jinja", comments=comments)


@app.route('/comment', methods=["POST"])
def send_comment():
    """Gets the only post in the system"""
    if request.form:
        name = generate_name()
        users.append({
            "name": name,
            "password": rand_pass(15)
        })
        comments.append({
            "name": name,
            # This is the comment content
            "comment": request.form["comment"] 
            
        })
    return redirect("/post")

## Below are all helper functions, you don't need to worry about these

@app.route('/')
def index():
    """There is no homepage in this demo, so redirect people to /post"""
    return redirect("/post")

@app.template_filter('process_comment')
def process_comment(comment):
    """Takes in a comment and renders it as a jinja template"""
    # Choose a random user, in real life this would be 
    # replaced with however they would be logged in
    user = random.choice(users)

    # TODO: Process the comment to make it safe
    return render_template_string(comment, user=user, users=users)

def rand_pass(max_length):
    """Generate a random password"""
    if max_length<6:
        max_length = 6
    return ''.join([f"{random.choice(string.ascii_lowercase)}{random.choice(string.ascii_uppercase)}" for _ in range(random.randint(6,max_length))])

def generate_name():
    """Generates a fake name"""
    first_names=["John", "James", "Colton", "Bradly", "Francine", "Jane", "Anne"]
    last_names =["Bowler", "Smith", "Franks", "Wong", "Lemire", "Evans"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

if __name__ == '__main__':
    app.run(debug=True)