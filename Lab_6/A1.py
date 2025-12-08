import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

def load_users_data():
    try:
        users_tree = ET.parse('users.xml')
        users = []
        for user_elem in users_tree.getroot().findall('user'):
            user = {
                    'user_id': int(user_elem.find('user_id').text),
                    'name': user_elem.find('name').text,
                    'age': int(user_elem.find('age').text),
                    'weight': int(user_elem.find('weight').text),
                    'fitness_level': user_elem.find('fitness_level').text,
                    'workouts': []
            }
            users.append(user)
        return users
    except FileNotFoundError:
        print("Файл не найден")
        return []


def load_workouts_data():
    try:
        workouts_tree = ET.parse('workouts.xml')
        workouts = []
        for workout_elem in workouts_tree.getroot().findall('workout'):
            workout_type = workout_elem.find('type').text
            if workout_type == 'силовая тренировка':
                workout_distance = 0
            else:
                workout_distance = float(workout_elem.find('distance').text)
            workout = {
                'workout_id': int(workout_elem.find('workout_id').text),
                'user_id': int(workout_elem.find('user_id').text),
                'date':workout_elem.find('date').text,
                'type': workout_elem.find('type').text,
                'duration': int(workout_elem.find('duration').text),
                'distance': workout_distance,
                'calories': int(workout_elem.find('calories').text),
                'avg_heart_rate': int(workout_elem.find('avg_heart_rate').text),
                'intensity': workout_elem.find('intensity').text,
            }
            workouts.append(workout)
        return workouts
    except FileNotFoundError:
        print("Не найдено")
        return []


def get_stats(users, workouts):
    try:
        total_workouts = len(workouts)
        all_users = len(users)
        total_calories = sum(workout['calories'] for workout in workouts)
        all_time = sum(workout['duration'] for workout in workouts)/60
        total_distance = sum(workout['distance'] for workout in workouts)
        result = f"""ОБЩАЯ СТАТИСТИКА
===========================
Всего тренировок: {total_workouts}
Всего пользователей: {all_users}
Общее количество калорий: {total_calories}
Общее время тренировок (часы): {all_time:.1f}
Общее расстояние: {total_distance}"""
        return result
    except FileNotFoundError:
        print("Не найдено")
        return []


def analyze_user_activity(users, workouts):
    user_stats = {}
    for user in users:
        user_id = [user['user_id']]
        user_workouts = [workout for workout in workouts if workout['user_id'] == user_id]
        total_workouts = len(user_workouts)
        total_calories = sum(w['calories'] for w in user_workouts)
        total_time = sum(w['duration'] for w in user_workouts) / 60
        user_stats[user['name']] = {
            'fitness_level': user['fitness_level'],
            'total_workouts': total_workouts,
            'total_calories': total_calories,
            'total_time': total_time,
            'workouts': user_workouts
        }
    sorted_users = sorted(user_stats.items(),
                          key=lambda x: x[1]['total_workouts'],
                          reverse=True)
    print("ТОП-3 АКТИВНЫХ ПОЛЬЗОВАТЕЛЕЙ:")
    print("=" * 50)

    for i, (name, stats) in enumerate(sorted_users[:3], 1):
        print(f"{i}. {name} ({stats['fitness_level']}):")
        print(f"   Тренировок: {stats['total_workouts']}")
        print(f"   Калорий: {stats['total_calories']}")
        print(f"   Время: {stats['total_time']:.1f} часов")
        print()

    return user_stats


def analyze_workout_types(workouts):
    workouts_by_type = {}
    for workout in workouts:
        workout_type = workout['type']
        if workout_type not in workouts_by_type:
            workouts_by_type[workout_type] = {
                'count': 0,
                'total_duration': 0,
                'total_calories': 0,
                'workouts': []
            }

        workouts_by_type[workout_type]['count'] += 1
        workouts_by_type[workout_type]['total_duration'] += workout['duration']
        workouts_by_type[workout_type]['total_calories'] += workout['calories']
        workouts_by_type[workout_type]['workouts'].append(workout)
        total_workouts = len(workouts)
        print("РАСПРЕДЕЛЕНИЕ ПО ТИПАМ ТРЕНИРОВОК:")
        print("=" * 50)
        for workout_type, stats in workouts_by_type.items():
            percentage = (stats['count'] / total_workouts) * 100
            avg_duration = stats['total_duration'] / stats['count']
            avg_calories = stats['total_calories'] / stats['count']

            print(f"{workout_type}: {stats['count']} тренировок ({percentage:.1f}%)")
            print(f"  Средняя длительность: {avg_duration:.0f} мин")
            print(f"  Средние калории: {avg_calories:.0f} ккал")

        return workouts_by_type


def find_user_workouts(users, workouts, user_name):
    user_f = None
    for user in users:
        if user['name'].lower() == user_name.lower():
            user_f = user
            break

    if not user_f:
        print(f"Пользователь с именем '{user_name}' не найден")
        return []
    user_workouts = [w for w in workouts if w['user_id'] == user['user_id']]

    return user_workouts


def analyze_user(users, workouts, user_name):
    user_f = None
    for user in users:
        if user['name'].lower() == user_name.lower():
            user_f = user
            break

    if not user_f:
        print(f"Пользователь с именем '{user_name}' не найден")
        return
    user_workouts = [workout for workout in workouts if workout['user_id'] == user_f['user_id']]

    if not user_workouts:
        print(f"У пользователя '{user_name}' нет тренировок")
        return
    total_workouts = len(user_workouts)
    total_calories = sum(workout['calories'] for workout in user_workouts)
    total_time = sum(workout['duration'] for workout in user_workouts) / 60
    total_distance = sum(workout['distance'] for workout in user_workouts)
    avg_calories_per_workout = total_calories / total_workouts


    workout_types = [workout['type'] for workout in user_workouts]
    if not workout_types:
        favorite_type = "нет данных"
    else:
        type_counts = {}

        for workout_type in workout_types:
            if workout_type in type_counts:
                type_counts[workout_type] += 1
            else:
                type_counts[workout_type] = 1

        favorite_type = max(type_counts, key=type_counts.get)


    print(f"ДЕТАЛЬНЫЙ АНАЛИЗ ДЛЯ ПОЛЬЗОВАТЕЛЯ: {user_f['name']}")
    print("=" * 60)
    print(f"Возраст: {user_f['age']} лет, Вес: {user_f['weight']} кг")
    print(f"Уровень: {user_f['fitness_level']}")
    print(f"Тренировок: {total_workouts}")
    print(f"Сожжено калорий: {total_calories}")
    print(f"Общее время: {total_time:.1f} часов")
    print(f"Пройдено дистанции: {total_distance:.1f} км")
    print(f"Средние калории за тренировку: {avg_calories_per_workout:.0f}")
    print(f"Любимый тип тренировки: {favorite_type}")
    print()

    return {
        'user': user_f,
        'total_workouts': total_workouts,
        'total_calories': total_calories,
        'total_time': total_time,
        'total_distance': total_distance,
        'avg_calories_per_workout': avg_calories_per_workout,
        'favorite_type': favorite_type,
        'workouts': user_workouts
    }

def circle(workouts):
    sizes = []
    run = 0
    for workout in workouts:
        if "бег" == workout['type']:
            run += 1
    run_percent = run * 100 / len(workouts)
    sizes.append(run_percent)

    strength = 0
    for workout in workouts:
        if "силовая тренировка" == workout['type']:
            strength += 1
    strength_percent = strength * 100 / len(workouts)
    sizes.append(strength_percent)

    bicycle = 0
    for workout in workouts:
        if "велосипед" == workout['type']:
            bicycle += 1
    bicycle_percent = bicycle * 100 / len(workouts)
    sizes.append(bicycle_percent)

    swimming = 0
    for workout in workouts:
        if "плавание" == workout['type']:
            swimming += 1
    swimming_percent = swimming * 100 / len(workouts)
    sizes.append(swimming_percent)

    walking = 0
    for workout in workouts:
        if "ходьба" == workout['type']:
            walking += 1
    walking_percent = walking * 100 / len(workouts)
    sizes.append(walking_percent)

    labels = ['Бег', 'Силовая тренировка', 'Велосипед', 'Плавание', 'Ходьба']
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title("Распределение типов тренировок")
    plt.show()
