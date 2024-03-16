def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

monto1 = 100
descuento1 = calcular_descuento(monto1)
print(f"El descuento aplicado al monto de {monto1} es de {descuento1}")

monto2 = 200
porcentaje_descuento2 = 20
descuento2 = calcular_descuento(monto2, porcentaje_descuento2)
print(f"El descuento aplicado al monto de {monto2} con un {porcentaje_descuento2}% de descuento es de {descuento2}")