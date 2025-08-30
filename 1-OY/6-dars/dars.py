

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
    print("Manfiy son kiritish mumkin emas !!!!!")
