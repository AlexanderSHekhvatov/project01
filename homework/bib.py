# print(f"Население города {​​population[1][0]}​​ - {​​population[1][1]}​​ человек")
# Вариант 1
# total_sum = population[0][1] + population[1][1] + population[2][1]
# Вариант 2
total_sum = 0
for i in population:
    total_sum += i[1]
print(f"Итого размер населения - {​​total_sum}​​ человек")
# Вариант 3
total_sum = 0
for city, people in population:
    print(f"Население города {​​city}​​ - {​​people}​​ человек")
    total_sum += people
print(f"Итого размер населения - {​​total_sum}​​ человек")

# Поиск самых высокооплачиваемых работников с помощью спискового включения
 
# нужно найти всех сотрудников, 
# зарабатывающих по крайней мере 100 000 долларов в год
 
employees = {'Alice' : 100000,
    'Bob' : 99817,
    'Carol' : 122908,
    'Frank' : 88123,
    'Eve' : 93121}
 