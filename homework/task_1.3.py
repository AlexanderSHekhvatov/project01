month_number = input('Введите номер месяца: ')

if month_number.isdigit() and 1 <= int(month_number) <= 12:
    month_number = int(month_number)
    days_in_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    month_name = {
        1: 'январь',
        2: 'февраль',
        3: 'март',
        4: 'апрель',
        5: 'май',
        6: 'июнь',
        7: 'июль',
        8: 'август',
        9: 'сентябрь',
        10: 'октябрь',
        11: 'ноябрь',
        12: 'декабрь'
    }
    print(f'Вы ввели {month_name[month_number]}. {days_in_month[month_number]} дней')
else:
    print('Такого месяца нет!')