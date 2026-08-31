producto = {
    "codigo":"P001",
    "nombre":"Teclado mecanico",
    "precio":45.99,
    "stock":20,
    "disponible":True
}

#Podemos consultar el nombre del producto:
print(producto["nombre"])

#Cmabiar la disponibilidad del producto y el stock a 0
producto["stock"] =0
producto["disponible"] = False
print(producto["disponible"])