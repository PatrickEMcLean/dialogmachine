import markdown
import os
import re
import argparse
import shutil
from jinja2 import Environment, FileSystemLoader

# Setup argument parser
parser = argparse.ArgumentParser(description="Render markdown file to HTML.")
parser.add_argument('input_file', nargs='?', default='dialog.md', help="Name of the file to render.")
args = parser.parse_args()

# Setup Jinja2 environment
env = Environment(loader=FileSystemLoader('./'))

# Read the file
with open(args.input_file, 'r') as f:
    text = f.read()

# Split the text into documents
documents = text.split('---')

# Define the output directory
output_dir = './output'

# Delete the output directory if it exists
if os.path.exists(output_dir):
    shutil.rmtree(output_dir)

# Create the output directory
os.makedirs(output_dir)

# Loop over the documents
for index, doc in enumerate(documents):
    # Skip any empty documents
    if doc.strip() == '':
        continue

    # Convert the document to HTML
    html = markdown.markdown(doc)

    # Extract the H1 heading
    h1_match = re.search(r'^#\s+(.*)$', doc, re.MULTILINE)
    
    # If an H1 heading was found, use it as the filename.
    # Otherwise, use a default filename.
    if h1_match:
        filename = h1_match.group(1)
    else:
        filename = 'document'

    # Make the filename safe for use as a file name
    filename = filename.replace(' ', '_')
    filename = re.sub(r'\W+', '', filename)  # remove non-alphanumeric characters

    # If it's the first document, prepend "START_" to the filename
    if index == 0:
        filename = 'START_' + filename

    # Load the template
    template = env.get_template('template.html')

    # Render the template with the title and content
    rendered_html = template.render(title=filename, content=html)

    # Write the rendered HTML to a file in the output directory
    with open(os.path.join(output_dir, f'{filename}.html'), 'w') as f:
        f.write(rendered_html)