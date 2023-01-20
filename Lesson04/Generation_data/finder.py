import open_list as ol
import xml_file as f

def question():
    return list(ol.opening(int(input("Enter member id what you want to find: "))).split(';'))


def creat_xml():
    f.create(*question()[0:-1])

creat_xml()