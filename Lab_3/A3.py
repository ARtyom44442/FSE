previous = int(input())
current = int(input())
if current >= previous:
    used_gas = current - previous
else:
    used_gas = 10000 - previous + current
if used_gas <= 300:
    bill = 21.0
elif used_gas <= 600:
    bill = 21 + (used_gas - 300) * 0.06
elif used_gas <= 800:
    bill = 21 + 300 * 0.06 + (used_gas - 600) * 0.04
else:
    bill = 21 + 300 * 0.06 + 200 * 0.04 + (used_gas - 800) * 0.025
if used_gas > 0:
    average_price = bill / used_gas
else:
    average_price = 0
bill = round(bill, 2)
average_price = round(average_price, 2)
print("Предыдущее Текущее Использовано К оплате Ср. цена m^3")
print(f"{previous} {current} {used_gas} {bill:.2f} {average_price:.2f}")