import os
import shutil
from block_markdown import markdown_to_html_node

def extract_title(markdown):
    """
    Extract the title from the markdown content.
    The title is defined as the first line that starts with '# '.
    If no h1 is found, raise value error.
    """
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No title found in markdown content.")

def generate_page(from_path, template_path, dest_path, base_path):
    """
    Generate a page by reading markdown from 'from_path', applying the template from 'template_path',
    and writing the result to 'dest_path'.
    """
    print(f"Generating page from {from_path} using template {template_path} to {dest_path}")

    with open(from_path, 'r') as f:
        markdown_content = f.read()
    
    with open(template_path, 'r') as f:
        template_content = f.read()
    
    markdown_html_string = markdown_to_html_node(markdown_content).to_html()
    page_title = extract_title(markdown_content)

    final_content = template_content.replace("{{ Title }}", page_title)
    final_content = final_content.replace("{{ Content }}", markdown_html_string)
    final_content = final_content.replace('href="/', f'href="{base_path}/')
    final_content = final_content.replace('src="/', f'src="{base_path}/')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    with open(dest_path, 'w') as f:
        f.write(final_content)
    print(f"Page generated at {dest_path}")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    """
    Recursively generate pages for all markdown files in 'dir_path_content' using the template at 'template_path',
    and write them to 'dest_dir_path', preserving the directory structure.
    """
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith('.md'):
                relative_path = os.path.relpath(root, dir_path_content)
                from_path = os.path.join(root, file)
                dest_path = os.path.join(dest_dir_path, relative_path, file.replace('.md', '.html'))
                generate_page(from_path, template_path, dest_path, base_path)