import os

js_dir = r"c:\Users\ANURAG PAREEK\OneDrive\Desktop\Resume\Qss1-main\qss1\qss\Project\static\js"
for root, _, files in os.walk(js_dir):
    for f in files:
        if f.endswith('.js'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            if 'index.html' in content:
                content = content.replace("'index.html'", "'/'")
                content = content.replace('"index.html"', '"/"')
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(content)
                print(f"Fixed relative paths in {f}")
