informacion_personal = { "nombre": "David Magarisca", "edad": 42, "ciudad": "Guayaquil", "profesion": "Militar" }

informacion_personal["ciudad"] = "Guayaquil"

informacion_personal["profesion"] = "Militar"

if "telefono" not in informacion_personal: informacion_personal["telefono"] = "960071286"

del informacion_personal["edad"]

print(informacion_personal)
