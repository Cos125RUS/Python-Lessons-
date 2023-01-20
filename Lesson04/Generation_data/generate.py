from random import randint

def name():
    with open('name.txt', 'r') as names:
        lists = names.readlines()
        n = randint(0, len(lists))
        new_name = lists[n].replace('\n', '')
    return new_name

# print(name(), end = ' ')

def surname():
    with open('surnames.txt', 'r') as surnames:
        lists = surnames.readlines()
        n = randint(0, len(lists))
        new_surname = lists[n].replace('\n', '')

    return new_surname

# print(surname())

def birthday():
    year = str(randint(1950, 2005))
    month = ('%2.2s'%randint(1, 13)).replace(' ','0')
    day = ('%2.2s'%randint(1, 29)).replace(' ','0')
    date = f'{day}.{month}.{year}'
    return date

# print(birthday())

def work_place():
    with open('companies.txt', 'r') as companies:
        lists = companies.readlines()
        n = randint(0, len(lists))
        new_company = lists[n].replace('\n', '')

    return f'"{new_company}"'

# print(work_place())


def phone_numbers(i):
    phone = '+7(9' + ('%2.2s'%randint(0, 100)).replace(' ', '0') + ')'\
            + ('%3.3s'%randint(0, 1000)).replace(' ', '0') + '-'\
            + ('%2.2s'%randint(0, 100)).replace(' ', '0') + '-'\
            + ('%2.2s'%randint(0, 100)).replace(' ', '0')
    return phone

# print(phone_numbers(0))

