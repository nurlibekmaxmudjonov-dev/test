# a = open('malumot.txt', 'r')
# k = a.readlines()
# for i in k:
#     print(i.title())
# # print(k)
# a.close()


#
#
# with open('malumot.txt', 'a') as f:
#     file = f.write('\nAhvolingiz yaxshimi')
#

#
# for i in range(10, 1, -1):
#     if i % 2 == 0:
#         with open("juft,txt", 'w') as f:
#             a = str(i)
#             file = f.write(a)
#     else:
#         with open("toq.txt", 'w') as f:
#             a = str(i)
#             s = f.write(a)

with open('juft.txt', 'w') as f, \
        open('toq.txt', 'w') as a, \
        open('jami.txt', 'w') as u:
    for i in range(1, 100):
        u.write(str(f"{i}\n"))
        if i % 2 == 0:
            f.write(f"{i}\n")
        else:
            a.write(f"{i}\n")
print("juft va toq sonlar alohida va umumiy"
      "qiib yozib qoyildi")
