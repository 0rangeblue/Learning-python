def run():
    mi_diccionario = {
        "llave 1": 1,
        "llave 2": 2,
        "llave 3": 3
    }

    # print(mi_diccionario["llave 1"])
    # print(mi_diccionario["llave 2"])
    # print(mi_diccionario["llave 3"])

    poblacion_paises = {
        "Mexico": 131_573_970,
        "Brasil": 210_147_125,
        "Colombia": 50_372_424
    }

    # print(poblacion_paises["Mexico"])

    # for pais in poblacion_paises.key():
    #     print(pais)

    # for pais in poblacion_paises.values():
    #     print(pais)

    for pais, poblacion in poblacion_paises.items():
        print(pais + " tiene " + str(poblacion) + " habitantes")


if __name__ == "__main__":
    run()