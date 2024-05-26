import http.client
import json
import time

def send_discord_webhook(message, webhook_url):
    # Extract the host and the path from the webhook URL
    if webhook_url.startswith("https://"):
        webhook_url = webhook_url[8:]
    host, path = webhook_url.split("/", 1)
    
    # Prepare the data
    data = {
        "content": message,
    }
    headers = {
        "Content-Type": "application/json"
    }
    json_data = json.dumps(data)
    
    # Send the request
    conn = http.client.HTTPSConnection(host)
    conn.request("POST", f"/{path}", body=json_data, headers=headers)
    response = conn.getresponse()
    
    if response.status == 204:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status}")
        print("Response:", response.read().decode())

if __name__ == "__main__":
    webhook_url = input("Enter the Discord webhook URL: ")
    message = input("Enter the message to send on Discord: ")
    send_discord_webhook(message, webhook_url)
    time.sleep(2)  # Wait for 2 seconds before closing