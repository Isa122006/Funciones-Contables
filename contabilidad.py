#precio neto
# es el precio sin iva, es quien regleja los impuestos  

#encontrar el precio neto

def precioNeto(iva,precio_bruto):
    resultado = precio_bruto / iva
    return resultado 


#botella de agua 
precio_bruto = 5 
IVA = 0.12
precio_neto = precioNeto(IVA,precio_bruto)

#ejemplo
# Datos del producto par de zapatos
producto = "par de zapatos" 
precio_bruto = 50
IVA = 1.12
precio_neto = precioNeto(IVA,precio_bruto)
print(f"producto:{producto} producto_bruto:Q{precio_bruto} precio neto:Q{precio_neto}")

def calcular_iva(precio_neto, IVA):
    precio_bruto = precio_neto / IVA
    iva_incluido = precio_neto - precio_bruto
    return iva_incluido

# Datos del producto par de zapatos
producto = "par de zapatos" 
precio_bruto = 50
IVA = 1.12
precio_neto = precio_bruto * IVA

# Calcular el IVA del precio neto
iva_incluido = calcular_iva(precio_neto, IVA)

print(f"Producto: {producto}")
print(f"Precio bruto: Q{precio_bruto}")
print(f"Precio neto: Q{precio_neto}")
print(f"IVA incluido en el precio neto: Q{iva_incluido}")

