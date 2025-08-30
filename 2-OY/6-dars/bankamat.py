"""
Bankamat tizimining beckent qismi
1. Balans ko'rish
2. Pul qo'yish
3. Pul yechish
"""


class Bankomat:
    def __init__(self, balans=0):
        self.balans = balans

    def balans_korish(self):
        print(f"Sizning balansingiz {self.balans} so'm 😁👍")

    def pull_qoyish(self, summ):
        self.balans += summ
        print(f" Qo'shilgan summa = {summ}\n"
              f"Hozirgi balansingiz = {self.balans}")

    def pull_yechish(self, summ):
        self.balans -= summ + summ * 0.02
        if summ > self.balans:
            print("Balansingizda kerakli summma yo'q "
                  "Qaytadan urinib ko'rish ")
        else:
            print(f"Yechilgan summa = {summ}\n"
                  f"Hozirgi balansingiz = {self.balans}")


bankamat = Bankomat(1000000)

while True:
    print("""
    ----- M E N Y U -----
    
    1. Balansni ko'rish 📋
    2. Pull qo'yish 💰
    3. Pull yechish 💵
    4. Chiqish 📌
    """)

    tanlov = input("Tanlang (1-4) = ")
    if tanlov == "1":
        bankamat.balans_korish()
    elif tanlov == "2":
        summ = int(input("Qo'yiladigon Summani kiriting = "))
        bankamat.pull_qoyish(summ)
    elif tanlov == "3":
        summ = int(input("Yechib olmoqchi bo'lgan summangizni kiriting : "))
        bankamat.pull_yechish(summ)
    elif tanlov == "4":
        print("Chiqilmoqda ..... Hayr")
        break
    else:
        print("Bunday buyruq yo'q")
