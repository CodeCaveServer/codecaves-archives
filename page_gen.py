import os

pages = []
page_path = "pages"
html_templates = ""

# Find all the files in the pages folder
for filename in os.listdir(page_path):
    if filename.endswith(".html"):
        page_name = os.path.splitext(filename)[0]
        pages.append(page_name)

# Generate HTML templates for each page
for page_name in pages:
    html_templates += f'<a href="{page_path}/{page_name}.html">{page_name}</a><br>'

# Create the index.html file
index_html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Index</title>
</head>
<body>
    <h1>Index</h1>
    {html_templates}
</body>
</html>
"""

# Write the index.html file
with open("index.html", "w") as file:
    file.write(index_html)


print("index.html generated successfully.")
