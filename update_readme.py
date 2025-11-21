from datetime import datetime
import requests

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# 1. 현재 시간
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
content = content.replace("{{TIME}}", now)

# 저장
with open("README.md", "w", encoding="utf-8") as f:

    f.write(content)
