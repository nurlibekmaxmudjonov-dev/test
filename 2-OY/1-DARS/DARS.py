class Car:
    def __init__(self, brend, nomi, rangi, narxi, turi):
        self.brend = brend
        self.nomi = nomi
        self.rangi = rangi
        self.narxi = narxi
        self.turi = turi

    def __str__(self):
        return f"Bu funksiyaning vazifasi funksiya yaratilmaganda o'zi ishlaydi"

    def my_car(self):
        return f"Menig moshinamning rangi {self.rangi}"
    def sotish(self):
        return (f"Brend = {self.brend} \n"
                f"Nomi = {self.nomi} \n"
                f"Rangi = {self.rangi} \n"
                f"Narxi = {self.narxi}\n")

car = Car('BMW', 'M5', 'Qora', 150000, 4)
print(car.sotish())
