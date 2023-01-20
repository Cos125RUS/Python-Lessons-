import peaple_creator as pc
import logger as log
import add_member as member

def view_create():
    data = pc.new_peaple_create()
    log.creation_new_person(data)
    member.add_new_member_csv(data)
    member.add_new_member_doc(data)
    return data

print(*view_create())