from twilio.rest import Client
from icecream import ic
import requests
import os



ENDPOINT = 'https://api.openweathermap.org/data/2.5/weather'
apiKey = 'a380de130e48f840587f44a2a9645fa7'


account_sid = 'ACd6f720fc61caf9d24001ff717b7f33cf'
auth_token = '1cfb1eea866b40027c8e0f3d0eb41386'

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

if True:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='+19063980344',
    body='It\'s going to rain today. Remember to bring an ☔️',
    to='+905422165117'
    )

    ic(message.status)
