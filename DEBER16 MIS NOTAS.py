# Crear un nuevo archivo llamado my_notes.txt y escribir notas personales
with open("my_notes.txt", "w") as file:
    file.write("1. Recordar comprar leche en el supermercado.\n")
    file.write("2. Llamar a mi amigo para coordinar un encuentro.\n")
    file.write("3. Hacer ejercicio por la tarde.\n")

# Abrir el archivo my_notes.txt en modo lectura
with open("my_notes.txt", "r") as file:
    # Leer el contenido del archivo línea por línea
    for line in file:
        # Mostrar en la consola cada línea leída
        print(line.strip())

# Cerrar el archivo my_notes.txt
file.close()
