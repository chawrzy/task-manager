import requests

TOKEN = "8448012593:AAHWDWktyGNxldCRhgvas6P3Aa474RcQPtc"
CHAT_ID = "722775425"


def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    try:
        response = requests.post(
            url,
            data={
                "chat_id": CHAT_ID,
                "text": text
            }
        )

        if response.status_code == 200:
            print("Message sent ✔")
        else:
            print("Failed to send message ❌", response.text)

    except Exception as e:
        print("Telegram error:", e)