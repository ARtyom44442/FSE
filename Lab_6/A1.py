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
                workout_distance = int(workout_elem.find('distance').text)
            workout = {
                'workout_id': int(workout_elem.find('workout_id').text),
                'user_id': int(workout_elem.find('user_id').text),
                'date':workout_elem.find('date').text,
                'type': workout_elem.find('type').text,
                'duration': int(workout_elem.find('duration').text),
                'distance': workout_distance,




            }
            workouts.append(workout)
        return workouts
    except FileNotFoundError:
        print("Не найдено")
        return []



print(load_workouts_data())
