x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))
x2 = int(input("Введите x2: "))
y2 = int(input("Введите у2: "))

if x1 > 0 and y1 > 0 and x2 > 0 and y2 > 0:
    print("Yes, I")
elif x1 < 0 and y1 > 0 and x2 < 0 and y2 > 0:
    print("Yes, II")
elif x1 < 0 and y1 < 0 and x2 < 0 and y2 < 0:
    print("Yes, III")
elif x1 > 0 and y1 < 0 and x2 > 0 and y2 < 0:
    print("Yes, IV")
else:
    print("NO")