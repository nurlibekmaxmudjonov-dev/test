"""
Inkasulyatsiya
"""
#
#
# class Biznes:
#     def __init__(self, nomi, login, password):
#         self.nomi = nomi
#         self._login = login
#         self.__password = password
#     def malumot(self):
#         return (f"Kamaniyaning nomi {self.nomi},"
#                 f" login {self._login}, {self.__password}")
# class Filial(Biznes):
#     def malumot(self):
#         return (f"Kamaniyaning nomi {self.nomi}"
#                 f"Login {self._login},")
# b = Biznes('Acer', 'acer', 'acer')
# f = Filial('Victus', 'acer', 'acer')
# print(b.malumot())
# print(f.malumot())

class BankHisobi:
    def __init__(self, ism, balans):
        self.ism = ism
        self.__balans = balans

    def balans(self):
        return f"{self.ism}ning balansi {self.__balans}"

b = BankHisobi('Shahodat', '999 mln')
print(b.balans())











