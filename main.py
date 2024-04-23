from twilio.rest import Client
from icecream import ic
import requests
import os



ENDPOINT = 'https://api.openweathermap.org/data/2.5/weather'
apiKey = os.getenv("API_KEY")


account_sid = os.getenv("SID")
auth_token = os.getenv("AUTH_TOKEN")

params = {
    'lat': 40.242730,
    'lon': 27.266370,
    'appid': apiKey,
    'cnt': 4
}

response = requests.get(ENDPOINT,params=params)
response.raise_for_status()

ic(response.status_code)


data = response.json()
rain = False

for hdata in data['weather']:
    if int(hdata['id']) < 700:
        rain = True


ic(rain)

if rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='VIRTURAL NUMBER',
    body='It\'s going to rain today. Remember to bring an ☔️',
    to='REAL NUMBER'
    )

    ic(message.status)
