from jinja2 import Template, FileSystemLoader, Environment

# Define your variables
name = 'ajay'
email = 'ajay@gmail.com'
numbers = [1, 2, 4, 5, 6]

# Create a Jinja2 environment with a file system loader
env = Environment(loader=FileSystemLoader('.'))  # Assuming your template file is in the current directory

# Load the template file
template = env.get_template('index_template.html')

# Render the template with your variables
rendered_form = template.render(pl_name=name, pl_email=email, numbers=numbers)

# Write the rendered content to a new file
with open('index.html', 'w') as output:
    output.write(rendered_form)
