import peaple_creator as pc

def add_new_member_csv(data):
    with open('members.csv', 'a') as members:
        for i in data:
            members.write(str(i) + ';')
        members.write('\n')


def add_new_member_doc(data):
    with open('members.doc', 'a') as members:
        for i in data[1:]:
            members.writelines(str(i) + '\n')
        members.write('\n')