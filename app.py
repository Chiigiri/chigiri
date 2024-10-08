from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        city = request.form['city']
        country = request.form['country']
        api_key = "095d43880d171d685bb252382a7f879e"
        
        try:
            weather_url = requests.get(
                f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial'
            )
            weather_data = weather_url.json()
            if weather_url.status_code == 200: 
                temp = weather_data['main']['temp']
                humidity = weather_data['main']['humidity']
                wind_speed = weather_data['wind']['speed']
                return render_template("result.html", temp=temp, humidity=humidity, wind_speed=wind_speed, city=city)
          
        except:
            return render_template("index.html")
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, port=4410)






