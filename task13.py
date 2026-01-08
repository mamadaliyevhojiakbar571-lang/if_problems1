# if13. Uchta son berilgan. Shu sonlarni o'ratachasi (ya'ni katta va kichik sonlar orasidagi son) ni
# anıglovchi programma tuzilsin.
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))  
if a > b and a > c:
    if b > c:
        print(b)
    else:
        print(c)
elif b > a and b > c:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if a > b:
        print(a)
    else:
        print(b)