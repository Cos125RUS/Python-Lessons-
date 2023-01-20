from datetime import datetime as dt

def creation_new_person(data):
    time = dt.now().strftime('%H:%M:%S %d/%m/%Y')
    print(time)
    with open('log.csv', 'a') as file:
        file.write(f'{time}; create; {data}\n')

# creation_new_person(0)


