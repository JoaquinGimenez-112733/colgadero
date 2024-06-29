def generar_particiones(string):
    resultados = []

    def generar_particiones_rec(particion_actual, indice):
        if indice == len(string):
            resultados.append(particion_actual[:])
            return

        for longitud in range(1, len(string) - indice + 1):
            particion_actual.append(string[indice : indice + longitud])
            generar_particiones_rec(particion_actual, indice + longitud)
            particion_actual.pop()

    generar_particiones_rec([], 0)

    return resultados
