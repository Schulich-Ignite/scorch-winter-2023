# To run this code you need to run
#  pip install jinja2
# You must run this from the /jinja_files folder or else jinja can't find the templates

# 1. Import
from jinja2 import Environment, select_autoescape, FileSystemLoader

# 2. Setup the environment
env = Environment(autoescape=select_autoescape(), loader=FileSystemLoader("templates"))

# 3. Load a template
example_template = env.get_template("index.jinja")

# 4. Render template with variables
html = example_template.render(name="kieran", age=23)

# Print result
print(html)

