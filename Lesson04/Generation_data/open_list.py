def opening(id_num):
    with open('members.csv', 'r') as members_list:
        member = members_list.read().split('\n')
        return member[id_num]

