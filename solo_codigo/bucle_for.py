menu = int(input(f"""\n
Welcome to this script of tables of multiplication tables, this script has 2 modes:

1.-Only one
2.-Infinite Tables

Chooise an option: """))

if menu == 1:
    number = int(input('Enter a positive number: '))
    if number > 0:
        print(f'\nTABLE OF {number}')
        for i in range(1, 11):
            print(f"{number} x {i} = {number*i}")
    else:
        print('choise an correct option')
elif menu == 2:
    print('hi')
else:
    text = 1
    while text <= 35:
        print(f'{text}: Enter a correct option.')
        text += 1
