def run():
    txt = 1
    num = 1
    for txt in range(1, 11):
        lista = [
            {f'{txt}': f'al cuadrado es = {num**2}'},
            {f'{txt}': f'al cuadrado es = {num**2}'},
            {f'{txt}': f'al cuadrado es = {num**2}'},
            {f'{txt}': f'al cuadrado es = {num**2}'},
            {f'{txt}': f'al cuadrado es = {num**2}'},
            {f'{txt}': f'al cuadrado es = {num**2}'},
            {f'{txt}': f'al cuadrado es = {num**2}'},
            {f'{txt}': f'al cuadrado es = {num**2}'}    
        ]
    
for values in lista:
    for key, value in values.items():
        print(key, value)

if __name__ == '__main__':
    run()