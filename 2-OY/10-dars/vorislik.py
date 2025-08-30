"""
vorislik
"""

class Transport:
    def __init__(self, nomi):
        self.nomi = nomi

class Car(Transport):
    def harakat(self):
        return f"{self.nomi} bu transport yolda harakatlanadi"

class Plane(Transport):
    def harakat(self):
        return f"{self.nomi} bu transport havoda harakatlanadi"

car = Car("BMW")
plane = Plane("B2")
print(car.harakat())
print(plane.harakat())