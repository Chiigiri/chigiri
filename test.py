import requests
city="indianapolis"
country="US"
api_key="9ece2c39cec5a95731b8ea9514ef5c83"
weather_url= requests.get(f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial')

weather_data=weather_url.json()

temp=weather_data['main']['temp']
humidity=weather_data['main']['humidity']
wind_speed=weather_data['wind']['speed']