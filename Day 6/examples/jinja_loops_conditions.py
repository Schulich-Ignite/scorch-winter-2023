# To run this code you need to run
#  pip install jinja2

# 1. Import
from jinja2 import Environment, select_autoescape

# 2. Setup the environment
env = Environment(autoescape=select_autoescape())

# 3. Load a template
example_template = env.from_string(r"""
<h1> Shopping list </h1>

<ul>
{% for item in shopping_list %}
    <li> {{item}} </li>
{% endfor %}
<ul>

<ul>
{% for item in shopping_list %}
    <li> {{item}} is number {{ loop.index }} </li>
{% endfor %}
<ul>

{% if age >= 23 %}
    <p> Based </p>
{% else %}
    <p> Less based </p>
{% endif %}
""")

# 4. Render template with variables
html = example_template.render(shopping_list=["Eggs", "Ham", "Spam"], age=23)

# Print result
print(html)
