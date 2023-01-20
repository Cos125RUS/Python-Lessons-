from datetime import datetime as dt

def creation_new_person(data):
    time = dt.now().strftime('%H:%M:%S %d/%m/%Y')
    print(time)
    with open('log.csv', 'a') as file:
        file.write('{};create;{}\n'
                    .format(time, data))

# creation_new_person(0)


