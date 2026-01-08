# if15. Uchta son berilgan, Shu sonlarning yig indisi eng katta bo'ladigan ikkitasini ekranga chigaruvchi
# programma tuzilsin.
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a + b >= a + c and a + b >= b + c:
    print(a, b)
elif a + c >= a + b and a + c >= b + c:
    print(a, c)
else:
    print(b, c)