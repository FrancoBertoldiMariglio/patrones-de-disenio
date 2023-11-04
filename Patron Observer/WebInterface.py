from Observer import Observer


class WebInterface(Observer):
    def update(self, temperature):
        print(f"La interfaz web muestra la temperatura: {temperature}°C")
