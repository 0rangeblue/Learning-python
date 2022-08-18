contador_externo = 0
contador_interno = 0

while contador_externo < 6:
    while contador_interno < 5:
        print(contador_externo, contador_interno)

        contador_interno += 1
        contador_externo += 1
    contador_externo += 1