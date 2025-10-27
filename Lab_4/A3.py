def analyze_packets():
    packets = input("Введите последовательность пакетов (0 и 1): ")

    if len(packets) < 5:
        print("Ошибка: длина последовательности должна быть не менее 5")
        return

    if not all(char in '01' for char in packets):
        print("Ошибка: последовательность должна содержать только 0 и 1")
        return

    total_packets = len(packets)
    lost_packets = packets.count('0')
    max_lost_streak = 0
    current_streak = 0
    arbuz = 0
    max_win_streak = 0

    for packet in packets:
        if packet == '0':
            current_streak += 1
            max_lost_streak = max(max_lost_streak, current_streak)
        else:
            current_streak = 0

    loss_percentage = (lost_packets / total_packets) * 100

    if loss_percentage <= 1:
        quality = "Отличное качество"
    elif loss_percentage <= 5:
        quality = "Хорошее качество"
    elif loss_percentage <= 10:
        quality = "Удовлетворительное качество"
    elif loss_percentage <= 20:
        quality = "Плохое качество"
    else:
        quality = "Критическое состояние сети"

    print(f"Общее количество пакетов: {total_packets}")
    print(f"Количество потерянных пакетов: {lost_packets}")
    print(f"Длина самой длинной последовательности потерянных пакетов: {max_lost_streak}")
    print(f"Процент потерь: {loss_percentage:.1f}%")
    print(f"Качество связи: {quality}")

analyze_packets()

