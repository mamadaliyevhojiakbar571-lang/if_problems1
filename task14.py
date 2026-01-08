# if14. Uchta son berilgan. Shu sonlarni aval kichigini keyin kattasini ekranga chiqaruvchi programma
# tuzilsin.
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a < b and a < c:
    print(a)
    if b > c:
        print(b)
    else:
        print(c)
elif b < a and b < c:
    print(b)
    if a > c:
        print(a)
    else:
        print(c)
else:
    print(c)
    if a > b:
        print(a)
    else:
        print(b)