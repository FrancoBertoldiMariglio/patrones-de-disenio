from Dashboard import Dashboard
from WeatherData import WeatherData
from WeatherApp import WeatherApp
from WebInterface import WebInterface

if __name__ == "__main__":
    weather_data = WeatherData()
    weather_interface = WebInterface()
    weather_app = WeatherApp()
    dashboard = Dashboard()

    weather_data.attach(weather_interface)
    weather_data.attach(weather_app)
    weather_data.attach(dashboard)

    weather_data.set_temperature(25)

    weather_data.detach(weather_app)

    weather_data.set_temperature(30)
