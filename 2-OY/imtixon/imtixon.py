# """
# 1. Python’da fayl ochish uchun qaysi funksiyadan foydalaniladi?
# javob: open funksiyasi.
# 2. 'r' rejimi nima maqsadda ishlatiladi?
# javob:faylni o'qish uchun ishlatiladi
# 3. 'w' rejimi faylga yozishda qanday ishlaydi?
# javob: faylga yozish uchun ishlatiladi
# 4. with open() nima vazifani bajaradi?
# javob: faylni aftomatik ravishda yopadi
# 5. file.read() metodi qanday ishlaydi?
# javob:butun matnni bitta string sifatida  o‘qib beradi.
#  6. file.write() metodi nimaga xizmat qiladi
#  javob : matn yoki ma’lumotni faylga yozish
#   7. Faylni yopish uchun qaysi metoddan foydalaniladi?
#   javob : closs meotidan
#  8. readline() va readlines() o‘rtasidagi farqni tushuntiring.
#  javob: faylni faqat bitta qatorni o‘qiydi. Fayldagi barcha qatorlarni o‘qib, ularni ro'yxat (list) shaklida qaytaradi
#  9. Python’da fayl ochishda encoding='utf-8' nima uchun kerak?
#  javob: fayldagi belgilar notog'ri chiqmasligi uchun
#  10. Agar fayl mavjud bo‘lmasa va siz uni o‘qimoqchi bo‘lsangiz, qanday xatolik yuz  beradi?
#  javob: faylni topalmaydi va fayl yoq deydi
# """

#
# """
# 11
# """
# with open("hello.txt", "w", ) as fayl:
#     fayl.write("Salom dunyo!")
#
# """
# 12
# """
# f=open("data.txt",'r')
# print(f.read())
# f.close()
#
# """
# 13
# """
# ism = input("Ismingizni kiriting: ")
#
# with open("ism.txt", "w") as fayl:
#     fayl.write(ism)
# """
# 14
# """
# f = open("open.txt",'r')
# print(f.readline())
# f.close()
# """
# 15
# """
# with open("ism_fayli.txt", 'r', ) as fayl:
#     satrlar = fayl.readlines()
#
# print("Fayldagi satrlar ro'yxati:")
# print(satrlar)
# """
# 16
# """
# with open("raqamlar.txt", "w") as fayl:
#     for raqam in range(1, 6):
#         fayl.write(f"{raqam}\n")
# """
# 17
# """
# with open("input.txt", "r", ) as fayl:
#     matn = fayl.read()
#
# sozlar = matn.split()
# sozlar_soni = len(sozlar)
#
# print("So‘zlar soni:", sozlar_soni)
# """
# 18
# """
#
# with open("with.txt",'r') as f:
#     matn = f. read()
#     print(matn)
# """
# 19
# """
# with open("python.txt", "w") as fayl:
#     for i in range(5):
#         fayl.write("Python\n")
# """
# 20
# """
#  try:
#     with open("malumot.txt", "r") as fayl:
#         mazmun = fayl.read()
#         print(mazmun)
# except FileNotFoundError:
#     print("Fayl topilmadi")