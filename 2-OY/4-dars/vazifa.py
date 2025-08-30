class Transport:
    def __init__(self, nomi):
        self.nomi = nomi

    def harakatlan(self):
        return f"{self.nomi} harakatlanmoqda"


class Avtomabil(Transport):
    def harakatlan(self):
        return f"{self.nomi} maydonda harakatlanadi"


class Vertalot(Transport):
    def harakatlan(self):
        return f"{self.nomi} havoda uchadi"


avto = Avtomabil('f1')
vertalot = Vertalot('qruvchi')
print(avto.harakatlan())
print(vertalot.harakatlan())
