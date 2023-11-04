from Observer import Observer


class WeatherApp(Observer):
    def update(self, temperature):
        print(f"La aplicación móvil muestra la temperatura: {temperature}°C")