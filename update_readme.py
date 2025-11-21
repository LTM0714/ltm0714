from datetime import datetime
import requests

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# 1. 현재 시간
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
content = content.replace("{{TIME}}", now)

# 2. 최근 커밋
user = "LTM0714"
repo = "LTM0714"
commits = requests.get(f"https://api.github.com/repos/{user}/{repo}/commits").json()
latest_commit = commits[0]["commit"]["message"]
content = content.replace("{{COMMIT}}", latest_commit)

# 저장
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)