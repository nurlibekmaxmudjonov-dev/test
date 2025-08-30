class ATM:
    def __init__(self):
        self.balans = 0
        self.parol = self._parol_ol()
        self.bloklangan = False

    def _parol_ol(self):
        try:
            with open('password.txt', 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            print("Parol topilmadi")
            return None

    def parol_tekshir(self):
        urinishlar = 3
        while urinishlar > 0:
            kiritilgan_parol = input("Parol kiriting : ")
            if kiritilgan_parol == self.parol:
                print("Muofiqiyatli kirdingiz 👍")
                return True
            else:
                urinishlar -= 1
                print("Parolingiz xato ")
        print("Kartangiz bloklandi sababi 3 martadan kop xato parol kiritdingiz")
        self.bloklangan = True
        return False

    def balans_korish(self):
        print(f"Siznig balansingiz {self.balans} so'm")

    def pull_qoshish(self):
        miqdor = int(input("Summa kiriting : "))
        self.balans += miqdor
        print(f"Qo'shilgan summa = {miqdor}\n"
              f"Balans = {self.balans}")

    def pull_yechish(self):
        miqdor = int(input("Summa kiritng = "))
        if miqdor <= self.balans:
            self.balans -= miqdor
            print(f"Yechilgan summa = {miqdor}\n"
                  f"Balans = {self.balans}")
        else:
            print("Hisonimgizda yetarlicha mablag' yo'q")

    def menu(self):
        while True:
            print("---------ATM------------")
            print("1. Balans ko'rish")
            print("2. Pul qohish")
            print("3. Pul yechish")
            print("4. Chiqish")
            tanlov = input("Tanlang (1-4) : ")
            if tanlov == "1":
                self.balans_korish()
            elif tanlov == "2":
                self.pull_qoshish()
            elif tanlov == "3":
                self.pull_yechish()
            elif tanlov == "4":
                print("Tizimdan chiqildi")
                break
            else:
                print("Bunday buyruq mavjud emas")


atm = ATM()
if atm.parol_tekshir():
    atm.menu()
else:
    print("Tizimdan foydalana olmaysiz")
