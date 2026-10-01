import os
import re

TEMPLATE_DIR = r"C:\Users\ANURAG PAREEK\OneDrive\Desktop\Resume\Qss1-main\qss1\qss\Project\templates"

def fix_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # Check if we need to load static
    if '{% load static %}' not in content:
        content = '{% load static %}\n' + content

    # Replace CSS references
    # style.css -> {% static 'css/style.css' %}
    content = re.sub(r'href="([^"]+\.css)"', r'href="{% static \'css/\1\' %}"', content)
    
    # Exclude external links if any were incorrectly matched (e.g., cdnjs)
    content = re.sub(r'href="{% static \'css/(https?://[^"]+)\' %}"', r'href="\1"', content)

    # Replace JS references
    # script.js -> {% static 'js/script.js' %}
    content = re.sub(r'src="([^"]+\.js)"', r'src="{% static \'js/\1\' %}"', content)
    content = re.sub(r'src="{% static \'js/(https?://[^"]+)\' %}"', r'src="\1"', content)
    
    # Replace Image references
    # image.jpg -> {% static 'images/image.jpg' %}
    content = re.sub(r'src="([^"]+\.(?:jpg|jpeg|png|gif|svg))"', r'src="{% static \'images/\1\' %}"', content)

    # Replace basic HTML links to use relative Django paths so they don't break unless wired
    # e.g., href="login.html" -> href="/login/"
    link_map = {
        'index.html': '/',
        'login.html': '/login/',
        'signup.html': '/signup/',
        'about.html': '/about/',
        'contact.html': '/contact/',
        'services.html': '/services/',
        'cleaning.html': '/services/cleaning/',
        'plumbing.html': '/services/plumbing/',
        'electricity.html': '/services/electricity/',
        'help.html': '/help/',
        'terms.html': '/terms/',
        'privacy.html': '/privacy/',
    }
    for old, new in link_map.items():
        content = content.replace(f'href="{old}"', f'href="{new}"')

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")

for filename in os.listdir(TEMPLATE_DIR):
    if filename.endswith('.html'):
        fix_html_file(os.path.join(TEMPLATE_DIR, filename))

print("Done fixing HTML files.")
