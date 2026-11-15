# Avance 3 : main.py
#Dante Ramos 
# Sistema de Gestión de Inventario y Ventas para una tienda.
# Nos permite registrar productos generales y productos de la categoría de 
# electrodomésticos, controlando el stock y los precios de forma sencilla

#Llamado de las Clases para crear Objetos y utilizar los métodos


# Importación de las clases desde el archivo modelos.py 
from modelos import Proveedor, Producto, Electrodomestico

#  Creación de Objetos Auxiliares (Proveedores)
proveedor_higiene = Proveedor("Kimberly-Clark", "55-1234-5678")
proveedor_hogar = Proveedor("Fabricas de Francia", "55-8765-4321")

# Creación de Objetos Principales
cepillo = Producto("Cepillo para Cabello", "Cuidado Personal", 10, 50, proveedor_higiene)
microondas = Electrodomestico("Horno de Microondas", "Electrodoméstico de Cocina", 20, 1000, "Samsung", 12, proveedor_hogar)
licuadora = Electrodomestico("Licuadora de Vidrio", "Electrodoméstico de Cocina", 15, 650, "Oster", 6, proveedor_hogar)

print("======== Mostrar Información ========")
cepillo.mostrar_informacion()
microondas.mostrar_informacion()
licuadora.mostrar_informacion()

print("======== Cambio de Precio ========")
# Intento de asignar un precio negativo (tiene que ser rechazado)
cepillo.cambiar_precio(-30)
# Cambio a un precio válido 
cepillo.cambiar_precio(70)
# Consulta del precio
print(f"El precio actual de '{cepillo.nombre}' es: ${cepillo.obtener_precio()}")

# Intento de asignar una cantidad negativa en almacén (tiene que ser rechazado)
microondas.cambiar_cantidad_almacen(-5)
# Cambio a una cantidad válida
microondas.cambiar_cantidad_almacen(18)

print("======== Independencia de los Objetos ========")
cepillo.realizar_venta(3)
microondas.realizar_venta(2)
licuadora.extender_garantia(6)

print("======== Delegación de métodos - (Llamada a Proveedor) ========")
# Solicitamos reabastecimiento
cepillo.solicitar_reabastecimiento(5)
licuadora.solicitar_reabastecimiento(10)
# Intento de reabastecimiento inválido (tiene ser rechazado)
microondas.solicitar_reabastecimiento(-4)
print("==================================================")

print("======== Comprobación final del estado ========")
cepillo.mostrar_informacion()
microondas.mostrar_informacion()
licuadora.mostrar_informacion()
print("==================================================")
