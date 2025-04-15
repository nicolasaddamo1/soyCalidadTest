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

menu_principal()