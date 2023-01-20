# import finder as m_find


def create(num_id = '-', name = 'none', surname = 'none', birthday = 'none', work = '-',\
           home_phone = '-', work_phone = '-', self_phone = '-'):
    xml = '<xml>\n'
    xml += '    <num_id units = "id">%s</num_id>\n' \
           % (num_id)
    xml += '    <name units = "name">%s</name>\n' \
           % (name)
    xml += '    <surname units = "surname">%s</surname>\n' \
           % (surname)
    xml += '    <birthday units = "birthday">%s</birthday>\n' \
           % (birthday)
    xml += '    <work units = "work">%s</work>\n' \
           % (work)
    home_phone = home_phone.split() if home_phone != '-' else ['', '-']
    xml += '    <home_phone units = "home phone">%s</home_phone>\n' \
           % (home_phone[1])
    work_phone = work_phone.split() if work_phone != '-' else ['', '-']
    xml += '    <work_phone units = "work phone">%s</work_phone>\n' \
           % (work_phone[1])
    self_phone = self_phone.split() if self_phone != '-' else ['', '-']
    xml += '    <self_phone units = "self phone">%s</self_phone>\n' \
           % (self_phone[1])
    xml += '</xml>'

    with open('view_person.xml', 'w') as page:
        page.write(xml)


    return xml

