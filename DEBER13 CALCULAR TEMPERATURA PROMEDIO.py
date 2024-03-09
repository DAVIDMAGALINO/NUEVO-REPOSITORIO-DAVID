def temperatura_promedio(datos):
    promedios = {}

    for ciudad, semanas in datos.items():
        total_temperaturas = 0
        cantidad_dias = 0

        for semana in semanas:
            total_temperaturas += sum(semana)
            cantidad_dias += len(semana)

        promedio = total_temperaturas / cantidad_dias
        promedios[ciudad] = promedio

    return promedios


# Datos de temperaturas de ejemplo (ciudad: [temperaturas de cada semana])
datos = {
    'Ciudad A': [[20, 25, 22, 24, 23, 21, 26], [22, 24, 23, 26, 27, 25, 23]],
    'Ciudad B': [[15, 18, 16, 20, 18], [19, 21, 22, 20, 23]],
    'Ciudad C': [[25, 26, 27, 28, 29, 25, 30], [24, 23, 25, 26, 28, 27, 29]]
}

resultados = temperatura_promedio(datos)
for ciudad, promedio in resultados.items():
    print(f"La temperatura promedio en {ciudad} es: {promedio}")