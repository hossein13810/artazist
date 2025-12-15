import requests


def send_notification(device_token, message_text):
    PUSHY_API_KEY = "e14ee828b4bad06fb90afc3ebfbfeef34efe87cbcb12fbd2f2c59e229d105d48"

    payload = {
        "to": device_token,
        "data": {
            "message": message_text
        }
    }

    headers = {
        "Authorization": f"Bearer {PUSHY_API_KEY}"
    }

    response = requests.post(
        f"https://api.pushy.me/push?api_key={PUSHY_API_KEY}",
        json=payload,
        headers=headers
    )

    return response.status_code
