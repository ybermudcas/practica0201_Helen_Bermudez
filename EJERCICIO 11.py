producto = input("Escribe el nombre del producto")
precio = float(input("Escribe el precio unitario"))
unidades = int(input("Escribe el número de unidades"))
print('{producto}: {unidades:3d} "unidades x" {precio:9.2f}"€ =" {total:11.2f}€'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))
