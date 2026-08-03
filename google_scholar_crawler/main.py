import json
import os
import urllib.parse
import urllib.request

AUTHOR_ID = "HY5jH_MAAAAJ"
API_KEY = os.environ["SERPAPI_KEY"]

params = urllib.parse.urlencode({
    "engine": "google_scholar_author",
    "author_id": AUTHOR_ID,
    "hl": "en",
    "api_key": API_KEY,
})

url = f"https://serpapi.com/search.json?{params}"

try:
    with urllib.request.urlopen(url, timeout=30) as response:
        data = json.load(response)

    if "error" in data:
        raise RuntimeError(data["error"])

    citations = data["cited_by"]["table"][0]["citations"]["all"]

    badge_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(citations),
        "color": "9cf",
    }

    os.makedirs("results", exist_ok=True)

    with open("results/gs_data.json", "w", encoding="utf-8") as output:
        json.dump(badge_data, output)

    print(f"Google Scholar citations updated to {citations}")

except Exception as error:
    print(f"Failed to update citations: {error}")
    raise
