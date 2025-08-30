class Transport:
    def __init__(self, nomi):
        self.nomi = nomi
    def harakatlan(self):
        return f"{self.nomi} harakatlanmoqda"
class Avtomabil(Transport):
    def harakatlan(self):
        return f"{self.nomi} yo'lda harakatlanadi"
class Samalyot(Transport):
    def harakatlan(self):
        return f"{self.nomi} havoda uchadi"

avto = Avtomabil('BMW')
samalyot = Samalyot('B2')
print(avto.harakatlan())
print(samalyot.harakatlan())
