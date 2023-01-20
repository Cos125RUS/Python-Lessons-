import generate as gen
import id_counter as id_count
from random import randint

def phones_location(i):
    dic = {0: 'home', 1: 'work', 2: 'self'}
    return dic[i]

def new_peaple_create():
    new_id = id_count.create_id()
    name = gen.name()
    surname = gen.surname()
    birthday = gen.birthday()
    work_place = gen.work_place()
    phones = [gen.phone_numbers(phones_location(i)) for i in range(randint(1, 3))]

    return (new_id, name, surname, birthday, work_place, *phones)

