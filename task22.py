# if22. OX va OY koordinata o'qlarida yotmaydigan nuqta berilgan. Nuqta joylashgan koordinata choragi
# anilansin.
x = int(input("x = "))
y = int(input("y = "))
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)