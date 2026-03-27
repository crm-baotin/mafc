import requests

TELEGRAM_BOT_TOKEN = "8213846644:AAG_Mom7MRzH97Y_-c7KQocQ0VS9qqf3mIc"
TELEGRAM_CHAT_ID = "6663298744"

def send_telegram(message: str):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }
        requests.post(url, data=payload, timeout=10)
    except:
        pass