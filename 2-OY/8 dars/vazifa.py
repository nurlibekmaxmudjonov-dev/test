#
# "Faylni o‘qish uchun ochish"
# file = open('file.txt', 'r')
#
# "Faylni yozish uchun ochish"
# file = open('file.txt', 'w')
#
# "Faylni qo‘shish (append) rejimida ochish"
# file = open('file.txt', 'a')
#
# # 4. Faylga yozish
# file = open('file.txt', 'w')
# file.write('Salom')
# file.close()
#
# "Faylni o‘qib chiqarish"
# file = open('file.txt', 'r')
# print(file.read())
# file.close()
#
# "Faylni mavjud bo‘lmasa yaratib yozish"
# file = open('file.txt', 'x')
#
# "Faylni ochib, qatorma-qator o‘qish"
# file = open('file.txt', 'r')
# for line in file:
#     print(line)
# file.close()
#
# "Faylga bir nechta qatordan yozish"
# file = open('file.txt', 'w')
# file.writelines(['salom\n', 'dunyo\n'])
# file.close()
#
# "Faylga yangi qator qo‘shish"
# file = open('file.txt', 'a')
# file.write('\nYangi qator')
# file.close()
#
# "Faylni binar holatda ochish"
# file = open('file.txt', 'rb')
#
# "Faylni binar yozish uchun ochish"
# file = open('file.txt', 'wb')
#
# "Faylni yangilash"
# file = open('file.txt', 'r+')
# file.write('Yangilandi')
# file.close()
#
# "Faylni mavjudligini tekshirish"
# try:
#     file = open('file.txt', 'r')
# except FileNotFoundError:
#     print("Fayl topilmadi")
#
# "Faylni ochib, birinchi qatordan faqat o‘qish"
# file = open('file.txt', 'r')
# print(file.readline())
# file.close()
#
# "Fayl ochish va darhol yopish"
# file = open('file.txt', 'w'); file.close()

