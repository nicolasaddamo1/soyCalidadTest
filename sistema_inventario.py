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

def main():
    while True:
        mostrar_productos()
        opcion = menu_principal()
        
        if opcion == "4":
            print("Gracias por usar el programa. ¡Hasta pronto!")
            break
        elif opcion == "1":
            print("Funcionalidad de agregar en desarrollo...")
        elif opcion == "2":
            print("Funcionalidad de eliminar en desarrollo...")
        elif opcion == "3":
            print("Funcionalidad de actualizar en desarrollo...")
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()