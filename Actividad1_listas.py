productos = ["Lapicero", "Cuaderno", "Borrador", "Regla", "Mochila", "Calculadora", "Tijeras", "Pegamento"]
precios = [1500, 3000, 1500, 2500, 60000, 25000, 3000, 2500]
cantidades = [10, 5, 20, 15, 3, 7, 12, 8]
cantidad_productos = len(productos)

print("\nInventario de la tienda escolar:"
      "\nproductos: ", productos,
      "\nprecios: ", precios,
      "\ncantidades: ", cantidades,
      "\ncantidad_productos: ", cantidad_productos)

print(f"'producto: {productos[0]}, tiene un precio de: {precios[0]}, y una cantidad de: {cantidades[0]}'")
print(f"'producto: {productos[1]}, tiene un precio de: {precios[1]}, y una cantidad de: {cantidades[1]}'")
print(f"'producto: {productos[2]}, tiene un precio de: {precios[2]}, y una cantidad de: {cantidades[2]}'")
print(f"'producto: {productos[3]}, tiene un precio de: {precios[3]}, y una cantidad de: {cantidades[3]}'")
print(f"'producto: {productos[4]}, tiene un precio de: {precios[4]}, y una cantidad de: {cantidades[4]}'")
print(f"'producto: {productos[5]}, tiene un precio de: {precios[5]}, y una cantidad de: {cantidades[5]}'")

print(type(productos))
print(type(productos[0]))

