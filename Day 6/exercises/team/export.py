# To run this code you need to run
#  pip install jinja2
# You must run this from the /jinja_files folder or else jinja can't find the templates

# 1. Import
from jinja2 import Environment, select_autoescape, FileSystemLoader
import os

# 2. Setup the environment
env = Environment(autoescape=select_autoescape(), loader=FileSystemLoader("."))

# 3. Load a template
example_template = env.get_template("index.jinja")

# 4. Render template with variables

team_members = [
    {"name":"Jake", "role":"CFO","description":"Sint pariatur adipisicing magna aliqua deserunt.", "image":"https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80"},
    {"name":"Megan", "role":"CTO","description":"Sint pariatur adipisicing magna aliqua deserunt.", "image":"https://images.unsplash.com/photo-1502823403499-6ccfcf4fb453?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"},
    {"name":"Alex", "role":"CEO","description":"Sint pariatur adipisicing magna aliqua deserunt.","image":"https://images.unsplash.com/photo-1634034379073-f689b460a3fc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80"},
    ]

html = example_template.render(team_members=team_members)

# Export to file

if os.path.exists("index.html"):
    os.remove("index.html")

with open("index.html", "w+") as html_file:
    html_file.write(html)
