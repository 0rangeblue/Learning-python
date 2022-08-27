def run():
    super_list = [
        {'Firstname': 'Natanael', 'Lastname': 'Cano'},
        {'Firstname': 'Juan', 'Lastname': 'Guarnizo'},
        {'Firstname': 'Victor', 'Lastname': 'Calderon'},
        {'Firstname': 'Roberto', 'Lastname': 'Cein'},
        {'Firstname': 'Diego', 'Lastname': 'Barca'},
    ]

    for value in super_list:
        print(value['Firstname'], '-', value['Lastname'])
        

    # super_dict = {
    #     'normal_nums': [1, 2, 3, 4],
    #     'negative_nums': [-1, -2, -3, -4],
    #     'floating_nums': [1.2, 2.3, 3.4, 4.5]
    # }

    # for value in super_dict.values():
    #     print(value)

if __name__ == '__main__':
    run()