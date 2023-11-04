from Observer import Observer


class Dashboard(Observer):
    def update(self, temperature):
        print(f"El panel de control muestra la temperatura: {temperature}°C")
