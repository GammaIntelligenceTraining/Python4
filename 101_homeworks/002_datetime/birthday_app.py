import datetime
'''Домашнее задание:
Пользователь вводит день своего рождения (месяц, число).
Программа выводит:

1. сколько дней осталось до его следующего дня рождения.
2. сколько дней прошло с его дня рождения
3. возраст пользователя (в идеале программа должна учитывать был ли день рождения в этом году или нет)


В качестве тренировки циклов, предлагаю следующее задание:
Написать гене ратор лоттерейных билетов:
За основу возьмём Viking Loto
5 номеров от 1 до 48 включительно + 2 номера от 1 до 5 включительно
Можно дать пользователю выбрать сколько билетов сгенерировать.'''

def enter_date():
    year, month, day = input('Please enter year, month and day of your birth: ').split(', ')
    birth_date = datetime.datetime(int(year), int(month), int(day))
    print(return_next_bd(birth_date))
    print(return_last_bd(birth_date))
    print(return_age(birth_date))


def return_next_bd(birth_date):
    today = datetime.date.today()
    bd_this_year = datetime.date(today.year, birth_date.month, birth_date.day)
    if today > bd_this_year:
        mod = 1
    elif today < bd_this_year:
        mod = 0
    else:
        mod = 0
    next_bd = datetime.date(today.year + mod, birth_date.month, birth_date.day)
    difference = next_bd - today
    if difference.days == 0:
        return f'Your birthday is today'
    else:
        return f'Your next birthday will be in {difference.days} days'


def return_last_bd(birth_date):
    today = datetime.date.today()
    bd_this_year = datetime.date(today.year, birth_date.month, birth_date.day)
    if today > bd_this_year:
        mod = 0
    else:
        mod = 1
    last_bd = datetime.date(today.year - mod, birth_date.month, birth_date.day)
    difference = today - last_bd
    return f'Your last birthday was {difference.days} days ago'


def return_age(birth_date):
    today = datetime.date.today()
    bd_this_year = datetime.date(today.year, birth_date.month, birth_date.day)
    if today >= bd_this_year:
        mod = 0
    else:
        mod = 1
    age = today.year - mod - birth_date.year
    return f'You are {age} years old.'


enter_date()