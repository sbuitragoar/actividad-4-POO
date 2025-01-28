class Inmueble:

    def __init__(self, identificador_inmobiliario, área, dirección):
        self.identificador_inmobiliario = identificador_inmobiliario
        self.área = área
        self.dirección = dirección
        self.precio_venta = 0.0 

    def calcular_precio_venta(self, valor_area):
        self.precio_venta = self.área * valor_area
        return self.precio_venta

    def imprimir(self):
        print(f"Identificador inmobiliario = {self.identificador_inmobiliario}")
        print(f"Área = {self.área}")
        print(f"Dirección = {self.dirección}")
        print(f"Precio de venta = ${self.precio_venta}")
        
class InmuebleVivienda(Inmueble):

    def __init__(self, identificador_inmobiliario, área, dirección, número_habitaciones, número_baños):
        super().__init__(identificador_inmobiliario, área, dirección)
        self.número_habitaciones = número_habitaciones
        self.número_baños = número_baños

    def imprimir(self):
        super().imprimir()
        print(f"Número de habitaciones = {self.número_habitaciones}")
        print(f"Número de baños = {self.número_baños}")
        
class Casa(InmuebleVivienda):

    def __init__(self, identificador_inmobiliario, área, dirección, número_habitaciones, número_baños, número_pisos):
        super().__init__(identificador_inmobiliario, área, dirección, número_habitaciones, número_baños)
        self.número_pisos = número_pisos

    def imprimir(self):
        super().imprimir()
        print(f"Número de pisos = {self.número_pisos}")
        
class Apartamento(InmuebleVivienda):

    def __init__(self, identificador_inmobiliario, área, dirección, número_habitaciones, número_baños):
        super().__init__(identificador_inmobiliario, área, dirección, número_habitaciones, número_baños)

    def imprimir(self):
        super().imprimir()
        
class CasaRural(Casa):
    valor_area = 1500000  
    def __init__(self, identificador_inmobiliario, área, dirección, número_habitaciones, número_baños, número_pisos, distancia_cabecera, altitud):
        super().__init__(identificador_inmobiliario, área, dirección, número_habitaciones, número_baños, número_pisos)
        self.distancia_cabecera = distancia_cabecera
        self.altitud = altitud

    def imprimir(self):
        super().imprimir()
        print(f"Distancia a la cabecera municipal = {self.distancia_cabecera} km.")
        print(f"Altitud sobre el nivel del mar = {self.altitud} metros.")
        print()


class CasaUrbana(Casa):

    def __init__(self, identificador_inmobiliario, área, dirección, número_habitaciones, número_baños, número_pisos):
        super().__init__(identificador_inmobiliario, área, dirección, número_habitaciones, número_baños, número_pisos)

    def imprimir(self):
        super().imprimir()
        
class ApartamentoFamiliar(Apartamento):
    valor_area = 2000000 

    def __init__(self, identificador_inmobiliario, área, dirección, número_habitaciones, número_baños, valor_administración):
        super().__init__(identificador_inmobiliario, área, dirección, número_habitaciones, número_baños)
        self.valor_administración = valor_administración

    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración = ${self.valor_administración}")
        print()

class Apartaestudio(Apartamento):
    valor_area = 1500000  
    
    def __init__(self, identificador_inmobiliario, área, dirección, número_habitaciones, número_baños):
        super().__init__(identificador_inmobiliario, área, dirección, 1, 1)

    def imprimir(self):
        super().imprimir()
        print()

class CasaConjuntoCerrado(CasaUrbana):
    valor_area = 2500000  

    def __init__(self, identificador_inmobiliario, área, dirección, número_habitaciones, número_baños,
                 número_pisos, valor_administración, tiene_piscina, tiene_campos_deportivos):
        super().__init__(identificador_inmobiliario, área, dirección, número_habitaciones, número_baños, número_pisos)
        self.valor_administración = valor_administración
        self.tiene_piscina = tiene_piscina
        self.tiene_campos_deportivos = tiene_campos_deportivos

    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración = ${self.valor_administración}")
        print(f"Tiene piscina? = {self.tiene_piscina}")
        print(f"Tiene campos deportivos? = {self.tiene_campos_deportivos}")
        print()

class CasaIndependiente(CasaUrbana):
    valor_area = 3000000

    def __init__(self, identificador_inmobiliario, área, dirección, número_habitaciones, número_baños, número_pisos):
        super().__init__(identificador_inmobiliario, área, dirección, número_habitaciones, número_baños, número_pisos)

    def imprimir(self):
        super().imprimir()
        print()

class Local(Inmueble):
    class Tipo:
        INTERNO = "INTERNO"
        CALLE = "CALLE"

    def __init__(self, identificador_inmobiliario, área, dirección, tipo_local):
        super().__init__(identificador_inmobiliario, área, dirección)
        self.tipo_local = tipo_local

    def imprimir(self):
        super().imprimir()
        print(f"Tipo de local = {self.tipo_local}")

class LocalComercial(Local):
    valor_area = 3000000  

    def __init__(self, identificador_inmobiliario, área, dirección, tipo_local, centro_comercial):
        super().__init__(identificador_inmobiliario, área, dirección, tipo_local)
        self.centro_comercial = centro_comercial

    def imprimir(self):
        super().imprimir()
        print(f"Centro comercial = {self.centro_comercial}")
        print()

class Oficina(Local):
    valor_area = 3500000 

    def __init__(self, identificador_inmobiliario, área, dirección, tipo_local, es_gobierno):
        super().__init__(identificador_inmobiliario, área, dirección, tipo_local)
        self.es_gobierno = es_gobierno

    def imprimir(self):
        super().imprimir()
        print(f"Es oficina gubernamental = {self.es_gobierno}")
        print()

class Prueba:
    @staticmethod
    def main():
        apto1 = ApartamentoFamiliar(103067, 120, "Avenida Santander 45-45", 3, 2, 200000)
        print("Datos apartamento")
        apto1.calcular_precio_venta(apto1.valor_area)
        apto1.imprimir()

        print("Datos apartamento")
        aptestudio1 = Apartaestudio(12354, 50, "Avenida Caracas 30-15", 1, 1)
        aptestudio1.calcular_precio_venta(aptestudio1.valor_area)
        aptestudio1.imprimir()

if __name__ == "__main__":
    Prueba.main()
