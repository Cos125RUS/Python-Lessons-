import generate as gen
import id_counter as id_count
from random import randint

def new_peaple_create():
    new_id = id_count.create_id()
    name = gen.name()
    surname = gen.surname()
    birthday = gen.birthday()
    work_place = gen.work_place()
    phones = [gen.phone_numbers(i) for i in range(randint(1, 4))]

    return (new_id, name, surname, birthday, work_place, *phones)

print(new_peaple_create())