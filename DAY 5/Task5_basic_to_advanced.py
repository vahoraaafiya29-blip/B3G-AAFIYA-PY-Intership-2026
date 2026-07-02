class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        self._celsius = value

    @property
    def to_kelvin(self):
        return self.celsius + 273.15
    

t=Temperature(25)

print("Celsius:", t.celsius)
print("Kelvin:", t.to_kelvin)
