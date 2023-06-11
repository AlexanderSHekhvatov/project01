# Задача 1.2.
# Пункт A.
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
import random # Пункт C.
import datetime # Пункт D.

my_favorite_songs = [
['Waste a Moment', 3.03],
['New Salvation', 4.02],
['Staying Alive', 3.40],
['Out of Touch', 3.03],
['A Sorta Fairytale', 5.28],
['Easy', 4.15],
['Beautiful Day', 4.04],
['Nowhere to Run', 2.58],
['In This World', 4.02],
]

# Выбираем три случайные песни из списка
random_songs = random.sample(my_favorite_songs, 3)

# Суммируем длительности песен
total_duration = sum(song[1] for song in random_songs)

# Конвертируем секунды в формат времени
total_time = datetime.timedelta(seconds=total_duration)

# Выводим результат в формате HH:MM:SS
print(f"Три песни звучат {total_time}")

# Пункт B.
# Есть словарь песен
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.
my_favorite_songs_dict = {
'Waste a Moment': 3.03,
'New Salvation': 4.02,
'Staying Alive': 3.40,
'Out of Touch': 3.03,
'A Sorta Fairytale': 5.28,
'Easy': 4.15,
'Beautiful Day': 4.04,
'Nowhere to Run': 2.58,
'In This World': 4.02,
}

# Выбираем три случайные песни из словаря
random_songs_dict = random.sample(list(my_favorite_songs_dict.values()), 3)

# Суммируем длительности песен
total_duration_dict = sum(random_songs_dict)

# Конвертируем секунды в формат времени
total_time_dict = datetime.timedelta(seconds=total_duration_dict)

# Выводим результат в формате HH:MM:SS
print(f"Три песни звучат {total_time_dict}")