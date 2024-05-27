import http.client
import json

print("GitHub Page: github.com/Playgmes11/discord-webhook-sender")


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

def main():
    webhook_url = input("Enter the Discord webhook URL: ")
    message = input("Enter the message to send on Discord: ")
    spam_option = input("Do you want to sent this message many times? (1 for Yes, 2 for No): ")
    
    if spam_option == '1':
        frequency = int(input("How many times do you want to send this message: "))
        for _ in range(frequency):
            send_discord_webhook(message, webhook_url)
    elif spam_option == '2':
        send_discord_webhook(message, webhook_url)
    else:
        print("Invalid option. Please enter 1 or 2.")

if __name__ == "__main__":
    main()