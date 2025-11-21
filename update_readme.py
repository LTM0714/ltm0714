from datetime import datetime

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

content = content.replace("{{TIME}}", now)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
