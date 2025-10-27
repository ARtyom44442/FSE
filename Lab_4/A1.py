import random
import time

N = int(input("Введите количество примеров: "))
total_time = 0
correct_task = 0

for i in range(N):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    correct_answer = a * b

    while True:
        try:
            start_time = time.time()
            answer = int(input(f"{a} × {b} = "))
            time_spend = time.time() - start_time
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")

    if answer == correct_answer:
        print(f"Верно! (Время: {time_spend: .1f} сек)")
        correct_task += 1
    else:
        print(f"Неверно! Правильно: {correct_answer} (Время: {time_spend:.1f} сек)")

    total_time += time_spend

print("\n--- СТАТИСТИКА ---")
print(f"Общее время: {total_time:.1f} секунд")
print(f"Среднее время на вопрос: {total_time / N:.1f} сек")
print(f"Правильных ответов: {correct_task}/{N}")
print(f"Процент правильных: {correct_task / N * 100:.1f}%")