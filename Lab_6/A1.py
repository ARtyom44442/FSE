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


print(get_stats(load_users_data(), load_workouts_data()))


