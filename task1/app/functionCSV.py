import csv
def function_csv():
    cont = []
    with open('inflation_russia.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            element_list = row['Год;Янв;Фев;Мар;Апр;Май;Июн;Июл;Авг;Сен;Окт;Ноя;Дек;Суммарная'].split(';')
            cont.append(element_list)
    return cont


def function_csv2():
    elem_list = function_csv()
    empty_list = []
    empty_list2 = []
    for element in elem_list:
        for el in element:
            if el == '':
                el = '-'
            empty_list.append(el)
        empty_list2.append(empty_list)
        empty_list = []
    return empty_list2


def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


def dict_list():
    list_of_list = function_csv2()
    content = []
    for element in list_of_list:
        moth_dict = {}
        moth_dict['Year'] = element[0]
        moth_dict['January'] = element[1]
        moth_dict['February'] = element[2]
        moth_dict['March'] = element[3]
        moth_dict['April'] = element[4]
        moth_dict['May'] = element[5]
        moth_dict['June'] = element[6]
        moth_dict['July'] = element[7]
        moth_dict['August'] = element[8]
        moth_dict['September'] = element[9]
        moth_dict['October'] = element[10]
        moth_dict['November'] = element[11]
        moth_dict['December'] = element[12]
        moth_dict['Summ'] = element[13]
        content.append(moth_dict)
        moth_dict = {}
    return content



def function_csv33():
    cont = []
    with open('inflation_russia.csv', newline='', encoding='utf-8',) as csvfile:
        reader = csv.DictReader(csvfile,delimiter=';')
        for row in reader:
            print(row)

function_csv33()