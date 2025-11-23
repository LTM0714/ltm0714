from datetime import datetime
import re

README_PATH = "README.md"
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(README_PATH, "r", encoding="utf-8") as file:
    content = file.read()

# "현재 시간:" 뒤의 모든 내용을 최신 시간으로 교체
content = re.sub(
    r"🕒 현재 시간:.*",
    f"🕒 현재 시간: {now}",
    content
)

with open(README_PATH, "w", encoding="utf-8") as file:
    file.write(content)
