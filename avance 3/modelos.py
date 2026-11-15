# Avance 3 : modelos.py
#Dante Ramos 
# Sistema de Gestión de Inventario y Ventas para una tienda.
# Nos permite registrar productos generales y productos de la categoría de 
# electrodomésticos, controlando el stock y los precios de forma sencilla

# Declaración de Clases y Métodos

# Creación de la clase auxiliar ("Tiene-un")
class Proveedor:
    def __init__(self, nombre_empresa, telefono):
        self.nombre_empresa = nombre_empresa
        self.telefono = telefono

    def obtener_datos_proveedor(self):
        return f"{self.nombre_empresa} (Tel: {self.telefono})"


    def enviar_mercancia(self, nombre_producto, cantidad):
        print(f"- La distribuidora '{self.nombre_empresa}' ha enviado {cantidad} unidades de '{nombre_producto}'.")


# Creación de la clase base
class Producto:
    def __init__(self, nombre, uso, cantidad_en_almacen, precio, proveedor):
        self.nombre = nombre
        self.uso = uso
        # Atributo protegido para que las subclases puedan acceder
        self._cantidad_en_almacen = cantidad_en_almacen
        # Atributo privado para proteger el precio y evitar cambios no autorizados
        self.__precio = precio
        self.proveedor = proveedor

    # Encapsulamiento (Getters y Setters)
      
    # Consultar el __precio
    def obtener_precio(self):
        return self.__precio

    # Modificar el atributo privado __precio
    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
            print(f"[Cambio Realizado con Éxito] El nuevo precio de '{self.nombre}' es de: ${self.__precio}")
        else:
            print(f"[Ha ocurrido un Error] La Operación ha sido rechazada para '{self.nombre}': El precio debe ser mayor a $0 (se intentó asignar: ${nuevo_precio}).")

    # Consultar la cantidad en almacén
    def obtener_cantidad_almacen(self):
        return self._cantidad_en_almacen

    # Modificar la cantidad en almacén 
    def cambiar_cantidad_almacen(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self._cantidad_en_almacen = nueva_cantidad
            print(f"[INVENTARIO] La cantidad actualizada de '{self.nombre}' en almacén es de: {self._cantidad_en_almacen} unidades.")
        else:
            print(f"[ERROR] No se puede asignar una cantidad negativa ({nueva_cantidad}) al almacén para '{self.nombre}'.")

    # Método de la clase base

    def mostrar_informacion(self):
        print("======== Información del Producto ========")
        print(f"Nombre del Producto : {self.nombre}")
        print(f"Tipo de Producto    : {self.uso}")
        print(f"Cantidad en Almacén : {self._cantidad_en_almacen} unidades")
        print(f"Precio del Producto : ${self.__precio}")
        print(f"Proveedor Asignado  : {self.proveedor.obtener_datos_proveedor()}")
        print("===========================================")

    def realizar_venta(self, cantidad_vendida):
        if cantidad_vendida <= 0:
            print(f"[Error] La cantidad a vender de '{self.nombre}' debe ser mayor a 0.")
        elif cantidad_vendida <= self._cantidad_en_almacen:
            self._cantidad_en_almacen = self._cantidad_en_almacen - cantidad_vendida
            total_venta = cantidad_vendida * self.__precio
            print(f"[Venta] Se han vendido {cantidad_vendida} unidades de '{self.nombre}' a ${self.__precio} c/u (Total: ${total_venta}). Quedan {self._cantidad_en_almacen} existencias en almacén.")
        else:
            print(f"[Error] Stock insuficiente en el almacen de '{self.nombre}'. Se han Solicitado: {cantidad_vendida}, Cantidad Disponible: {self._cantidad_en_almacen}.")

    # Método que llama al objeto Proveedor
    def solicitar_reabastecimiento(self, cantidad_solicitada):
        if cantidad_solicitada > 0:
            self.proveedor.enviar_mercancia(self.nombre, cantidad_solicitada)
            self._cantidad_en_almacen = self._cantidad_en_almacen + cantidad_solicitada
            print(f"[Inventario] Se ha actualizado la cantidad de '{self.nombre}', ahora hay {self._cantidad_en_almacen} unidades disponibles en el almacén.")
        else:
            print(f"[Error] La cantidad a solicitar al proveedor debe ser mayor a 0.")

class Electrodomestico(Producto):
    def __init__(self, nombre, uso, cantidad_en_almacen, precio, marca, meses_garantia, proveedor):
        # Llamada al constructor del padre
        super().__init__(nombre, uso, cantidad_en_almacen, precio, proveedor)
        # Atributos  de esta subclase 
        self.marca = marca
        self.meses_garantia = meses_garantia

    # Sobrescritura de métodos
    
    # Modificación del método 
    def mostrar_informacion(self):
        print("======== Información ========")
        print(f"Electrodoméstico    : {self.nombre} (Marca: {self.marca})")
        print(f"Categoría / Uso     : {self.uso}")
        print(f"Cantidad en Almacén : {self._cantidad_en_almacen} unidades")
        print(f"Precio Unitario     : ${self.obtener_precio()}")
        print(f"Garantía    : {self.meses_garantia} meses")
        print(f"Proveedor Asignado  : {self.proveedor.obtener_datos_proveedor()}")
        print("==================================================")

    # Método adicional 
    def extender_garantia(self, meses_extra):
        if meses_extra > 0:
            self.meses_garantia = self.meses_garantia + meses_extra
            print(f"[GARANTÍA] La garantía de '{self.nombre}' ({self.marca}) se extendió a {self.meses_garantia} meses en total.")
        else:
            print(f"[ERROR] Los meses adicionales de garantía deben ser mayores a 0.")
