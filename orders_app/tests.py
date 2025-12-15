import requests

API_KEY = "service.ff0468f8995a4ec0bfcd290a44efb0f0"

lat = 38.251558
lng = 48.297227

url = f"https://api.neshan.org/v5/reverse?lat={lat}&lng={lng}"

headers = {
    "Api-Key": API_KEY
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"❌ خطا در درخواست ({response.status_code}):", response.text)
