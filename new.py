import os
import requests
from plyer import notification
import time

def check_website_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
    except requests.ConnectionError:
        pass
    return False

def notify_site_back_online(url):
    notification_title = "Website Status"
    notification_message = f"The website {url} is back online!"

    notification.notify(
        title=notification_title,
        message=notification_message,
        app_icon=None,  # Set to the path of your icon file if you have one
        timeout=10,  # Adjust this value based on how long you want the notification to be visible
    )

    # Play a sound using osascript (replace 'path/to/soundfile.mp3' with your MP3 file)
    os.system("open alaarm.mp3")

def monitor_website(url):
    while True:
        if check_website_status(url):
            notify_site_back_online(url)
            break
        time.sleep(2)  # Check every 10 seconds (adjust as needed)

# Example usage
website_url = "https://academia.srmist.edu.in"
monitor_website(website_url)
