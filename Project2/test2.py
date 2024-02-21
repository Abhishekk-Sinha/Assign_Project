#2. Create a Flask app that consumes data from external APIs and displays it to users.
#Try to find an public API which will give you a data and based on that call it and deploy it on cloud platform

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Coordinates for Delhi, India
    lat = 28.609355
    lon = 77.333560

    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = 'af73cb13d1500a75d33108328538f01a'

    # Format the URL with latitude, longitude, and API key
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Extract relevant information from the response data
        weather_description = data['weather'][0]['description']

        # Render the data in the HTML template
        return render_template('index.html', weather_description=weather_description)
    else:
        return 'Error fetching data from the external API'

if __name__ == '__main__':
    app.run(debug=True)
