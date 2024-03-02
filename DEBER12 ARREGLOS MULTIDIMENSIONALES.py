temperaturas = [[[28, 30, 29, 27, 26, 25, 24],
                 [27, 29, 28, 26, 25, 26, 23],
                 [30, 31, 31, 30, 29, 28, 27]],
                [[25, 26, 24, 23, 25, 28, 27],
                 [28, 27, 29, 30, 31, 30, 29],
                 [26, 27, 25, 24, 23, 22, 21]],
                [[32, 31, 30, 29, 28, 27, 26],
                 [26, 28, 30, 31, 32, 33, 34],
                 [27, 28, 29, 30, 31, 32, 33]]]

ciudades = ["Ciudad A", "Ciudad B", "Ciudad C"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

for i, ciudad in enumerate(ciudades):
    for j, semana in enumerate(temperaturas[i]):
        promedio = sum(semana) / len(semana)
        print(f"El promedio de temperaturas para la Ciudad {ciudad} en la semana {j+1} es: {promedio}")
