a = int(input("Введите числj "))
if  0 < a and a > 1000 :
    print("Неверное число")
    exit(0)
b = int(input("b "))
if 0 < b and b > 1000 :
    print("Неверное число")
    exit(0)

result = "Числа равны" if a == b else "Числа не равны"
print(result)
result2 = [a, b][a <= b]
print("Наибольшее число ", result2)