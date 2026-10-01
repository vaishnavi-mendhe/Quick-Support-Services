import os
import re

TEMPLATE_DIR = r"C:\Users\ANURAG PAREEK\OneDrive\Desktop\Resume\Qss1-main\qss1\qss\Project\templates"

for filename in os.listdir(TEMPLATE_DIR):
    if filename.endswith('.html'):
        filepath = os.path.join(TEMPLATE_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove literal backslashes before single quotes
        new_content = content.replace(r"\'", "'")
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {filename}")
