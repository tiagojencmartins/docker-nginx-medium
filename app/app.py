from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return requests.get("http://nginx/weather-service/weatherforecast").text