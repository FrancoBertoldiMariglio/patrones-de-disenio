from Subject import Subject

class WeatherData(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = None

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        print("Notificando cambios en la temperatura...")
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, newTemperature):
        self._temperature = newTemperature
        self.notify()
