import creation as create
import finder as find

def menu():
    options = [create.do_create, find.create]
    choice = int
    while (choice != 0):
        choice = -1
        while (choice != 1 and choice != 2 and choice != 0):
            choice = int(input('Press "1" to create new member\nPress "2" to find member\nPress "0" to exit\n'))
        if choice == 1 or choice == 2:
            options[choice-1]()
