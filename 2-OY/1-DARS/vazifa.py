class f1:
    def __init__(self, brend, nomi, rangi, narxi, turi):
        self.brend = brend
        self.nomi = nomi
        self.rangi = rangi
        self.narxi = narxi
        self.turi = turi

    def __str__(self):
        return f"Bu funksiyaning vazifasi funksiya yaratilmaganda o'zi ishlaydi"

    def my_f1(self):
        return f"Menig konidsanerimnig brend {self.brend}"
    def sotish(self):
        return (f"Brend = {self.brend} \n"
                f"Nomi = {self.nomi} \n"
                f"Rangi = {self.rangi} \n"
                f"Narxi = {self.narxi}\n")

f1 = f1('f1', 'BMW', 'oq', 140000,'3')
print(f1.sotish())
