import requests

from admin_panel_app.models import SourcesData


def send_sms(phone_number, message):
    access_hash = None
    if SourcesData.objects.filter(id=1).exists():
        access_hash = SourcesData.objects.get(id=1).kavenegar_access_hash

    url = f'https://api.kavenegar.com/v1/{access_hash}/sms/send.json'

    data = {
        'receptor': f'+98{phone_number}',
        'message': f'{message}\nلغو11',
    }
    req = requests.post(url, data=data)
    return req.status_code
