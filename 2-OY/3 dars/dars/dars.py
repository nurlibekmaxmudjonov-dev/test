"""
--------------------Vorislik----------------------
"""




class Hayvon:
    def __init__(self, nomi):
        self.nomi = nomi
class Ot(Hayvon):
    def __str__(self):
        return f"Bu Ot nomli class"
    def tezlik(self):
        return f"{self.nomi} --- bu hayvonn tez yuguradi"
class Sher(Hayvon):
    def qirol(self):
        return f"{self.nomi} O'rmon va hayvonlar qiroli"
b = Sher('Sher')
a = Ot('Mustang')
print(a.tezlik())


def malumot(self):
        return "Malumot"


class BMW(Moshina):
    def __init__(self, brend, rangi, narxi, max_tezligi, ot_kuchi):
        super().__init__(brend, rangi, narxi)
        self.max_tezligi = max_tezligi
        self.ot_kuchi = ot_kuchi
        print(b.qirol())


    class Moshina:
        def __init__(self, brend, rangi, narxi):
            self.brend = brend
            self.rangi = rangi
            self.narxi = narxi

        def __str__(self):
            return "BU class Ota class"

    def umumiy(self):
        return (f"Brend = {self.brend}\n"
                f"Nomi = {self.rangi}")


bmw = BMW('Bmw', 'Qora', 1234442, '350km/h', 1500)
print(bmw.umumiy())
print(bmw.malumot())