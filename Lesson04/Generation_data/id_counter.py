def create_id():
    with open('id.txt', 'r') as num:
        new_id = int(num.read()) + 1
    with open('id.txt', 'w') as num:
        num.write(str(new_id))

    return new_id

# print(create_id())