# To run this code you need to run
#  pip install jinja2
from datetime import datetime

# 1. Import
from jinja2 import Environment, select_autoescape

# 2. Setup the environment
env = Environment(autoescape=select_autoescape())

# 3. Load a template
example_template = env.from_string(r"""
<h1> Hello {{ config['name'] }}</p>

<p>The year is {{date.year}}</p>
""")

# 4. Render template with variables
config = {"name":"Kieran"}
html = example_template.render(config=config, date=datetime.now())

# Print result
print(html)
