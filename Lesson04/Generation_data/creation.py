import peaple_creator as pc
import logger as log
import add_member as member

def do_create():
    data = pc.new_peaple_create()
    log.creation_new_person(data)
    member.add_new_member_csv(data)
    member.add_new_member_doc(data)
    print('New member was creation\n')
    return data

# print(*do_create())