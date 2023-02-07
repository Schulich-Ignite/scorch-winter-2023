# To run this code you need to run
#  pip install jinja2

# 1. Import
from jinja2 import Environment, select_autoescape

# 2. Setup the environment
env = Environment(autoescape=select_autoescape())

# 3. Load a template
example_template = env.from_string(r"""
<h1>Hello {{name | capitalize}},</h1>

<p>You are {{ age }} years old</p>
""")

# 4. Render template with variables
html = example_template.render(name="kieran", age=23)

# Print result
print(html)

