from datetime import datetime

README_PATH = "README.md"

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(README_PATH, "r", encoding="utf-8") as file:
    content = file.read()

content = content.replace("{{TIME}}", now)

with open(README_PATH, "w", encoding="utf-8") as file:
    file.write(content)


