import re

def update_html_file(file_path):
    # Read the contents of the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Update navigation section URLs
    html_content = re.sub(
        r'https://www\.makeopinion\.com/en/(.*?)\.php',
        r'https://lakshmi-k02.github.io/makeopinion-mobile/\1.html',
        html_content
    )

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

    # Save the updated HTML content to a new file
    updated_file_path = file_path.replace('.html', '-updated.html')
    with open(updated_file_path, 'w', encoding='utf-8') as updated_file:
        updated_file.write(html_content)

    print(f"Updated HTML file saved as: {updated_file_path}")

# Example usage
input_file = 'user-students.html'  # Replace with your actual HTML file path
update_html_file(input_file)
