from abc import ABC, abstractmethod
from enum import Enum
class StockInsuficienteError(Exception):
    """Excepción lanzada cuando la cantidad pedida supera el stock disponible."""
    pass

class Ubicacion(Enum):
    ENDOR = "Endor"
    CUMULO_RAIMOS = "Cúmulo Raimos"
    NEBULOSA_KALIIDA = "Nebulosa Kaliida"

class ClaseNave(Enum):
    EJCUTOR = "Ejecutor"
    ECLIPSE = "Eclipse"
    SOBERANO = "Soberano"

class UnidadCombate:
    def __init__(self, id_combate: str, clave_transmision: int):
        self.id_combate = id_combate
        self.clave_transmision = clave_transmision

class Nave(ABC):
    def __init__(self, nombre:str, catalogo_repuestos: list):
        self.nombre = nombre
        self.catalogo_repuestos = catalogo_repuestos

    @abstractmethod
    def mostrar_info(self):
        pass

class EstacionEspacial(Nave):
    def __init__(self, nombre:str, catalogo: list, tripulacion: int, pasaje: int, lugar: Ubicacion):
        super().__init__(nombre, catalogo)
        self.tripulacion = tripulacion
        self.pasaje = pasaje
        self.lugar = lugar

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Ubicación: {self.lugar.value}")

class CazaEstelar(Nave, UnidadCombate):
    def __init__(self, nombre:str, catalogo: list, dotacion: int, id_combate: str, clave: int):
        Nave.__init__(self, nombre, catalogo)
        UnidadCombate.__init__(self, id_combate, clave)
        self.dotacion = dotacion

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"ID Combate: {self.id_combate}")
        print(f"Dotación: {self.dotacion}")

class Repuesto:
    def __init__(self, nombre:str, proveedor:str, cantidad:int, precio:float):
        self.nombre = nombre
        self.proveedor = proveedor
        self.__cantidad = cantidad
        self.precio = precio
    
    @property
    def cantidad(self):
        return self.__cantidad

    def extraer_repuesto(self, unidades:int):
        if unidades > self.__cantidad: 
            raise StockInsuficienteError(f"Stock insuficiente para el repuesto {self.nombre}. Cantidad disponible: {self.__cantidad}")
        self.__cantidad -= unidades
        return True
    
# codigo de prueba
if __name__ == "__main__":
    print("--- INICIANDO SISTEMA MILIMPERIO ---")
    
    # Instanciación correcta
    caza = CazaEstelar("TIE Fighter", ["Motor Iónico", "Láser"], 1, "TIE-001", 12345)
    estacion = EstacionEspacial("Estrella de la Muerte", ["Panel", "Reactor"], 342953, 843342, Ubicacion.ENDOR)
    motor = Repuesto("Motor Iónico", "Sienar", 5, 2500.50)
    
    # Impresión en pantalla
    caza.mostrar_info()
    estacion.mostrar_info()
    
    print("\n--- PRUEBA DE ADQUISICIÓN DE REPUESTOS ---")
    try:
        print("Intentando extraer 3 motores...")
        motor.extraer_repuesto(3)
        print(f"Éxito. Stock restante: {motor.cantidad}")
        
        print("Intentando extraer 10 motores...")
        motor.extraer_repuesto(10) # Esto desencadena el error
    except StockInsuficienteError as e:
        # Capturamos y tratamos la excepción
        print(f"EXCEPCIÓN CAPTURADA: {e}")

       