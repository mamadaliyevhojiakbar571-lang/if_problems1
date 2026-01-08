# if21. Koordinatalar tekisligida butun son berilgan. Agar nuqta koordinata boshida yotsa, O chigarilsin.
# Agar nugta OX yoki OY o'glarida joylashsa mos holda 1 va 2 chigarilsin. Agar nugta koordinata o'gida
# joylashmasa 3 chigarilsin.
x = int(input("x = "))
y = int(input("y = "))
if x == 0 and y == 0:
    print(0)
elif x == 0:
    print(1)
elif y == 0:
    print(2)
else:
    print(3)
