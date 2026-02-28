from servicios.inventario_service import InventarioService
from modelos.producto import Producto


def menu():
    print("\n===== SISTEMA AVANZADO DE INVENTARIO =====")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar por nombre")
    print("5. Mostrar todos")
    print("6. Guardar")
    print("7. Salir")


def pedir_float(mensaje):
    while True:
        try:
            valor = input(mensaje).replace("$", "").strip()
            return float(valor)
        except ValueError:
            print("❌ Ingrese un número válido.")


def pedir_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("❌ Ingrese un número entero válido.")


def main():
    inventario = InventarioService()
    inventario.cargar()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = pedir_int("Cantidad: ")
            precio = pedir_float("Precio: ")

            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("ID a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID a actualizar: ")
            cantidad = pedir_int("Nueva cantidad: ")
            precio = pedir_float("Nuevo precio: ")
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar()

        elif opcion == "7":
            inventario.guardar()
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()