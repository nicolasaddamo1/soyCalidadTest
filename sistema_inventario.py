Productos = {1: 'Pantalones', 2: 'Camisas', 3: 'Corbatas', 4: 'Casacas'}
Precios = {1: 200.00, 2: 120.00, 3: 50.00, 4: 350.00}
Stock = {1: 50, 2: 45, 3: 30, 4: 15}

def mostrar_productos():
    print("=" * 20)
    print("Lista de Productos:")
    print("=" * 20)
    for codigo in Productos:
        print(f"{codigo} {Productos[codigo]} {Precios[codigo]} {Stock[codigo]}")
    print("=" * 20)

def menu_principal():
    print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")
    return input("Elija opción: ")
def eliminar_producto():
    print("\n--- Eliminar producto ---")
    
    if not Productos:
        print("No hay productos en el inventario para eliminar.")
        return
    
    while True:
        try:
            codigo = int(input("Ingrese el código del producto a eliminar: "))
            if codigo not in Productos:
                print("El código ingresado no existe. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Ingrese un valor numérico para el código.")
    
    print(f"Producto a eliminar: {codigo} - {Productos[codigo]} - Precio: {Precios[codigo]} - Stock: {Stock[codigo]}")
    confirmacion = input("¿Está seguro de eliminar este producto? (s/n): ").lower()
    if confirmacion == 's':
        nombre = Productos[codigo]
        del Productos[codigo]
        del Precios[codigo]
        del Stock[codigo]
        print(f"Producto '{nombre}' eliminado con éxito.\n")
    else:
        print("Operación cancelada.\n")

def actualizar_producto():
    print("\n--- Actualizar producto ---")
    
    if not Productos:
        print("No hay productos en el inventario para actualizar.")
        return
    
    while True:
        try:
            codigo = int(input("Ingrese el código del producto a actualizar: "))
            if codigo not in Productos:
                print("El código ingresado no existe. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Ingrese un valor numérico para el código.")
    
    print(f"Información actual: {codigo} - {Productos[codigo]} - Precio: {Precios[codigo]} - Stock: {Stock[codigo]}")
    
    print("Ingrese los nuevos datos:")
    
    nuevo_nombre = input(f"Nombre [{Productos[codigo]}]: ")
    if nuevo_nombre:
        Productos[codigo] = nuevo_nombre
    
    while True:
        nuevo_precio = input(f"Precio [{Precios[codigo]}]: ")
        if not nuevo_precio:
            break
        try:
            precio_float = float(nuevo_precio)
            if precio_float <= 0:
                print("El precio debe ser mayor que cero.")
                continue
            Precios[codigo] = precio_float
            break
        except ValueError:
            print("Ingrese un valor numérico para el precio.")
    
    while True:
        nuevo_stock = input(f"Stock [{Stock[codigo]}]: ")
        if not nuevo_stock:
            break
        try:
            stock_int = int(nuevo_stock)
            if stock_int < 0:
                print("El stock no puede ser negativo. Intente nuevamente.")
                continue
            Stock[codigo] = stock_int
            break
        except ValueError:
            print("Ingrese un valor entero para el stock.")
    
    print(f"Producto con código {codigo} actualizado con éxito.\n")

def agregar_producto():
    print("\n--- Agregar nuevo producto ---")
    
    nuevo_codigo = max(Productos.keys()) + 1
    
    nombre = input("Nombre del producto: ")
    
    while True:
        try:
            precio = float(input("Precio del producto: "))
            if precio <= 0:
                print("El precio debe ser mayor que cero. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Ingrese un valor numérico para el precio.")
    
    while True:
        try:
            cantidad = int(input("Cantidad en stock: "))
            if cantidad < 0:
                print("El stock no puede ser negativo. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("PIngrese un valor entero para el stock.")
    
    Productos[nuevo_codigo] = nombre
    Precios[nuevo_codigo] = precio
    Stock[nuevo_codigo] = cantidad
    
    print(f"Producto '{nombre}' agregado con éxito con código {nuevo_codigo}.\n")

def main():
    while True:
        mostrar_productos()
        opcion = menu_principal()
        
        if opcion == "4":
            print("Se ha cerrado el programa.")
            break
        elif opcion == "1":
            agregar_producto()
        elif opcion == "2":
            eliminar_producto()
        elif opcion == "3":
            actualizar_producto()
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()

