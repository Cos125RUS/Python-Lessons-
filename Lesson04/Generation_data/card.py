def create(num_id = '-', name = 'none', surname = 'none', birthday = 'none', work = '-',\
           home_phone = '-', work_phone = '-', self_phone = '-'):
    home_phone = home_phone.split() if home_phone != '-' else ['', '-']
    work_phone = work_phone.split() if work_phone != '-' else ['', '-']
    self_phone = self_phone.split() if self_phone != '-' else ['', '-']
    card = f"\n\nID# {num_id}\nName: {name}\nSurname: {surname}\nBirthday: {birthday}\nWork place: {work}\n"\
            f"Home phone: {home_phone[1]}\nWork phone: {work_phone[1]}\nSelf phone: {self_phone[1]}\n\n\nCharacteristic: "

    with open('card_person.doc', 'w') as page:
        page.write(card)

    print("Card was create")
    return card