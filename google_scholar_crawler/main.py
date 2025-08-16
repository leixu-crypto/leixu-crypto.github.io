from scholarly import scholarly
import json
import os
import signal

# 设置超时（例如 60 秒）
def timeout_handler(signum, frame):
    raise TimeoutError("Execution timed out")

signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(60)

try:
    author = scholarly.search_author_id('HY5jH_MAAAAJ')
    scholarly.fill(author, sections=['indices'])

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(author.get('citedby', 'N/A')),
        "color": "9cf"
    }

    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w") as f:
        json.dump(shieldio_data, f)

except TimeoutError:
    print("❌ Script timed out.")
    exit(1)

except Exception as e:
    print("❌ An error occurred:", e)
    exit(1)
