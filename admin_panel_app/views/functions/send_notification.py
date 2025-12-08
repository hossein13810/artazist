import json
from pathlib import Path

import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request


def send_notification(device_token, message_title, message_text):
    service_account_file = f'{Path(__file__).resolve().parent}/artazist-b84b1-16379cccb75e.json'
    project_id = "artazist-b84b1"
    scopes = ["https://www.googleapis.com/auth/firebase.messaging"]
    credentials = service_account.Credentials.from_service_account_file(service_account_file, scopes=scopes)
    credentials.refresh(Request())
    access_token = credentials.token

    url = f"https://fcm.googleapis.com/v1/projects/{project_id}/messages:send"

    message = {
        "message": {
            "token": device_token,
            "notification": {
                "title": message_title,
                "body": message_text
            },
            "data": {
                "key1": "value1"
            }
        }
    }

    response = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json; UTF-8",
        },
        data=json.dumps(message)
    )

    return response.status_code
