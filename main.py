import requests
import time

# Configuration
website_url = "http://144.48.117.66/"
check_interval = 2  # seconds
pushover_user_key = "ud7ke2pct7bndhn4ar3i7ogyoknxfb"
pushover_api_token = "ah3td5ykyizv8zcn25ppy8sofk8ida"

def is_website_available(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        return False

def send_push_notification(message):
    pushover_url = "https://api.pushover.net/1/messages.json"
    payload = {
        "token": pushover_api_token,
        "user": pushover_user_key,
        "message": message
    }
    response = requests.post(pushover_url, data=payload)
    if response.status_code != 200:
        print("Failed to send notification")

while True:
    if is_website_available(website_url):
        print(f"{website_url} is available")
    else:
        print(f"{website_url} is down")
        send_push_notification(f"Alert: {website_url} is down!")
    time.sleep(check_interval)
