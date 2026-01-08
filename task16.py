# if16. A, B, C haqiqiy sonlari berilgan. Agar berilgan sonlar o'sish tartibida berilgan bo'lsa, sonlarni
# ikkilantiring, aks holda sonlarni ishorasi o'zgartirilsin. A, B, C ning qiymatlari ekranga chigarilsin.
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a < b and b < c:
    print(a * 2, b * 2, c * 2)
else:
    print(-a, -b, -c)