class Inson:
    """
    Bu classnig vazifasi Inson haqida malumot beradi
    """

    def __init__(self, ism, familiya, yosh, otasining_ismi, nomeri, pas, email, jinsi):
        """
        :param ism: Ism kiritiladi
        :param familiya:
        :param yosh:
        :param otasining_ismi:
        :param nomeri:
        :param pas:
        :param email:
        :param jinsi:
        """
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
        self.otasining_ismi = otasining_ismi
        self.nomeri = nomeri
        self.pas = pas
        self.email = email
        self.jinsi = jinsi

    def __str__(self):
        """
        :return: Bu funksiya ism va familiyani qaytaradi
        """
        return (f"Mening ismim {self.ism} \n"
                f"Familiya {self.familiya}")

    def malumot(self):
        """
        :return: Bu to'liq malumot qaytaradi
        """
        a = (f"Ismim = {self.ism}\n"
             f"Familiya = {self.familiya}\n"
             f"Nomerim = {self.nomeri}")
        return a


ism = input("Ism = ")
familiya = input("familiya = ")
yosh = input("yosh = ")
otasini = input("Otasining ismi = ")
nomeri = input("nomeri = ")
pas = input("paswordni kiriting = ")
email = input("Email = ")
jinsi = input("jinsi = ")
inson = Inson(ism, familiya, yosh, otasini, nomeri, pas, email, jinsi)
a = Inson('Dior', 'Axmadjonov', '21', 'Abdullo', '0123485', '242', '32ege', 'M')

print(a)
print(inson.malumot())
