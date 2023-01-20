import creation as create

def menu():
    options = [create.do_create]
    chois = int
    while (chois != 0):
        chois = -1
        while (chois != 1 and chois != 2 and chois != 0):
            print('Press "1" to create new member\nPress "2" to print xml-file\nPress "0" to exit\n')
            chois = int(input())
        if chois == 1 or chois == 2:
            options[chois-1]()
