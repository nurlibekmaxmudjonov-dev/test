file = open('masalan.txt', 'r')
print(file.read())
file.close()


a = open('test.txt', 'r')
print(a.readline())
a.close()

file = open('test.txt', 'w')
file.write('salom yaxshimiz \n')
file.write("Abdulaziz hoz turasa")
file.close()


test = open('test.txt', 'a')
test.write('\nBU appent rejimi ')
test.close()







with open('test.txt', 'w') as f:
    f.write('Salom\n')
    f.write('Oddiku qiyinmas')