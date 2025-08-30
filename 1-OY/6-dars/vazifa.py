"""
2
"""

baho = int(input("Bahoni kiriting: "))
if baho == 1:
    print("Bahoingiz  = F")
elif baho == 2:
    print("Bahoingiz  = D")
elif baho == 3:
    print("Bahoingiz  = C")
elif baho == 4:
    print("Bahoingiz  = B")
elif baho == 5:
    print("Bahoingiz  = A")
else:
    print("Bahoingiz  = Noto'g'ri baho kiritdingiz!")


"""
3
"""

son = int(input("Istalgan sonni kiriting: "))

if son > 0:
    print("Son musbat")
elif son < 0:
    print("Son manfiy")
else:
    print("0 ga teng son kiritdingiz")

"""
16
"""

a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
c = int(input("3-sonni kiriting: "))

if a + b > c and a + c > b and b + c > a:
    print("Uchburchak hosil bo'ladi")
else:
    print("Uchburchak hosil bo'lmaydi")


"""
22
"""
oy = int(input("Oyni kiriting: "))

if 2 < oy < 6:
    print("Bahor")
elif 5 < oy < 9:
    print("Yoz")
elif 8 < oy < 12:
    print("Kuz")
elif oy == 12 or oy == 1 or oy == 2:
    print("Qish")
else:
    print("Noto'g'ri oy kiritdingiz!")

"""
30
"""

chastota = int(input("Chastotani kiriting: "))

if 0 < chastota < 20:
    print("Infratovush")
elif 20 <= chastota < 20000:
    print("Auditoriya tovushi")
elif 20000 <= chastota < 20000000:
    print("Ultratovush")
elif 20000000 <= chastota < 20000000000:
    print("Chastotani tovushi")
else:
    print("Manfoy son kiritish mumkin emas !!!!!")

