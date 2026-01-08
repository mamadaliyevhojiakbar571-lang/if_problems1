# if20. Sonlar o qida uchta A, B, C nuqtalar berilgan. A nuqtaga eng yaqin nuqta va ular orasidagi masofa
# topilsin.
a = float(input("A nuqta koordinatasi: "))
b = float(input("B nuqta koordinatasi: "))
c = float(input("C nuqta koordinatasi: "))
if a < b and a < c:
    if b < c:
        print("A nuqtaga eng yaqin nuqta B nuqta, ular orasidagi masofa:", b - a)
    else:
        print("A nuqtaga eng yaqin nuqta C nuqta, ular orasidagi masofa:", c - a)

