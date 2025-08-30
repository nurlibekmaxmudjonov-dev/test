try:
    fayl = open("yoqfayl.txt", "r")
    with fayl as f:
        print(f.read())
except FileNotFoundError:
    print("Fayl topilmadi.")
fayl = open("example1.txt", "w")
with fayl as f:
    f.write("Salom, bu with misolidir.")

data = {"ism": "Ali", "yosh": 25}
f = open("data.json", "w")
json.dump(data, f)
f.close()


f = open("file1.txt", "w")
f.write("Salom, dunyo!")
f.close()

f = open("file1.txt", "r")
print(f.read())
f.close()

f = open("file1.txt", "a")
f.write("\nYangi qator")
f.close()

try:
    f = open("file2.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Fayl topilmadi!")

f = open("list.txt", "w")
for i in range(5):
    f.write(f"{i}\n")
f.close()

f = open("list.txt", "r")
for line in f:
    print(line.strip())
f.close()

f = open("binary.dat", "wb")
f.write(b"12345")
f.close()

f = open("binary.dat", "rb")
data = f.read()
print(data)
f.close()

f = open("rewrite.txt", "w")
f.write("Bu yangi matn.")
f.close()

import json

data = {"ism": "Ali", "yosh": 25}
f = open("data.json", "w")
json.dump(data, f)
f.close()
