from kavenegar import *
api = KavenegarAPI('587666362B7176556D744A415572753272695132384B4773393074307A53772F564A4C3947444B6F4474553D')
params = { 'sender' : '2000660110', 'receptor': '09202014827', 'message' :'.وب سرویس پیام کوتاه کاوه نگار' }
response = api.sms_send(params)

print(response)