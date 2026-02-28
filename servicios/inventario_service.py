import json
import os
from modelos.producto import Producto


class InventarioService:
    def __init__(self):
        self._productos = {}

        # Ruta absoluta correcta del proyecto
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self._ruta_archivo = os.path.join(base_dir, "datos", "inventario.json")

    # -------------------------
    # CRUD
    # -------------------------

    def agregar_producto(self, producto):
        if producto.get_id() in self._productos:
            print("❌ El producto ya existe.")
        else:
            self._productos[producto.get_id()] = producto
            print("✅ Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self._productos:
            del self._productos[id_producto]
            print("🗑 Producto eliminado.")
        else:
            print("❌ Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self._productos:
            if cantidad is not None:
                self._productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self._productos[id_producto].set_precio(precio)
            print("🔄 Producto actualizado.")
        else:
            print("❌ Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        resultados = [
            p for p in self._productos.values()
            if nombre.lower() in p.get_nombre().lower()
        ]

        if resultados:
            for p in resultados:
                print(f"{p.get_id()} | {p.get_nombre()} | {p.get_cantidad()} | ${p.get_precio()}")
        else:
            print("❌ No se encontraron productos.")

    def mostrar_todos(self):
        if not self._productos:
            print("📦 Inventario vacío.")
        else:
            for p in self._productos.values():
                print(f"{p.get_id()} | {p.get_nombre()} | {p.get_cantidad()} | ${p.get_precio()}")

    # -------------------------
    # Persistencia
    # -------------------------

    def guardar(self):
        os.makedirs("datos", exist_ok=True)

        with open(self._ruta_archivo, "w") as archivo:
            json.dump(
                {id: p.to_dict() for id, p in self._productos.items()},
                archivo,
                indent=4
            )

        print("💾 Inventario guardado correctamente.")

    def cargar(self):
        if not os.path.exists(self._ruta_archivo):
            return

        with open(self._ruta_archivo, "r") as archivo:
            datos = json.load(archivo)

            for id_producto, info in datos.items():
                producto = Producto(
                    info["id"],
                    info["nombre"],
                    info["cantidad"],
                    info["precio"]
                )
                self._productos[id_producto] = producto