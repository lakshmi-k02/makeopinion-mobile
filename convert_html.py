import re
import os
import glob

def update_html_file(file_path):
    # Read the contents of the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Update navigation section URLs to change .php to .html
    html_content = re.sub(
        r'https://www\.makeopinion\.com/en/(.*?)(\.php)',
        r'https://lakshmi-k02.github.io/makeopinion-mobile/\1.html',
        html_content
    )

    # Handle .php to .html for URLs starting with lakshmi-k02.github.io
    html_content = re.sub(
        r'https://lakshmi-k02\.github\.io/makeopinion-mobile/(.*?)(\.php)',
        r'https://lakshmi-k02.github.io/makeopinion-mobile/\1.html',
        html_content
    )

    # Update the base URL for other cases
    html_content = re.sub(
        r'https://makeopinion\.com/en',
        r'https://lakshmi-k02.github.io/makeopinion-mobile',
        html_content
    )

    # Update external scripts and stylesheets
    html_content = re.sub(
        r'https://lakshmi-k02\.github\.io/makeopinion-mobile/assets/css/(.*?\.css)',
        r'https://lakshmi-k02.github.io/makeopinion-mobile/assets/css/\1',
        html_content
    )
    html_content = re.sub(
        r'https://lakshmi-k02\.github\.io/makeopinion-mobile/assets/js/(.*?\.js)',
        r'https://lakshmi-k02.github.io/makeopinion-mobile/assets/js/\1',
        html_content
    )

    # Update localhost section URLs
    html_content = re.sub(
        r'http://localhost:3000',
        r'https://lakshmi-k02.github.io/makeopinion-mobile',
        html_content
    )

    # Save the updated HTML content to the same file
    with open(file_path, 'w', encoding='utf-8') as updated_file:
        updated_file.write(html_content)

    print(f"Updated HTML file: {file_path}")


def update_html_files_in_folder(folder_path):
    # Find all .html files in the given folder
    html_files = glob.glob(os.path.join(folder_path, '*.html'))

    # Process each file
    for file_path in html_files:
        update_html_file(file_path)

# Example usage: Process all .html files in the current folder
current_folder = os.getcwd()  # Get the current working directory
update_html_files_in_folder(current_folder)
