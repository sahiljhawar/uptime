import requests
import json
import os
from datetime import datetime


def check_uptime(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False


def update_uptime_data(new_entries, max_entries=1000):
    filename = "uptime_data.json"

    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)
    else:
        data = {}

    for url, entry in new_entries.items():
        if url not in data:
            data[url] = []
        data[url].append(entry)

        data[url] = data[url][-max_entries:]

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)


def get_urls_from_env():
    sites_env = os.environ.get("SITES", "")
    return [url.strip() for url in sites_env.split("\n") if url.strip()]


def main():
    urls = get_urls_from_env()

    timestamp = datetime.utcnow().isoformat()
    new_entries = {}

    for url in urls:
        is_up = check_uptime(url)
        new_entries[url] = {"timestamp": timestamp, "status": "up" if is_up else "down"}
        print(f"Uptime check completed for {url}. Status: {'Up' if is_up else 'Down'}")

    update_uptime_data(new_entries)


if __name__ == "__main__":
    main()
