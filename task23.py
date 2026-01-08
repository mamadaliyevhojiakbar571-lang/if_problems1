# if23. Koordinata o'qlariga parallel ravishda to giri to'rtburchakning uchta uchi berilgan, to'rtinchi uchi
# koordinatasini aniglansin.
x1, y1 = float(input("x1: ")), float(input("y1: "))
x2, y2 = float(input("x2: ")), float(input("y2: "))
x3, y3 = float(input("x3: ")), float(input("y3: "))
if x1 == x2:
    x4 = x3
    if y1 == y3:
        y4 = y2
    else:
        y4 = y1
elif x1 == x3:
    x4 = x2
    if y1 == y2:
        y4 = y3
    else:
        y4 = y1
else:
    x4 = x1
    if y2 == y3:
        y4 = y1
    else:
        y4 = y2
print("To'rtinchi nuqta koordinatalari: (", x4, ",", y4, ")")