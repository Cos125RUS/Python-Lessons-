import open_list as ol
import xml_file as f
import card as c

def question():
    return list(ol.opening(int(input("Enter member id what you want to find: "))).split(';'))


def create():
    choice = int(input("Are you want card (pass '1') or xml (pass '2')? "))
    if choice == 1:
        return f.create(*question()[0:-1])
    elif choice == 2:
        return c.create(*question()[0:-1])
    else:
        print('Incorrect value\nTry again')
        return create()


