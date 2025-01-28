from abc import ABC, abstractmethod

class Equipo:
    total_tiempo = 0 

    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais
        Equipo.total_tiempo = 0  
        self.lista_ciclistas = [] 

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_pais(self):
        return self.pais

    def set_pais(self, pais):
        self.pais = pais

    def añadir_ciclista(self, ciclista):
        self.lista_ciclistas.append(ciclista)  

    def listar_equipo(self):
        for ciclista in self.lista_ciclistas:
            print(ciclista.get_nombre())  

    def buscar_ciclista(self):
        nombre_ciclista = input("Introduce el nombre del ciclista a buscar: ")
        for ciclista in self.lista_ciclistas:
            if ciclista.get_nombre() == nombre_ciclista:
                print(ciclista.get_nombre())

    def calcular_total_tiempo(self):
        for ciclista in self.lista_ciclistas:
            Equipo.total_tiempo += ciclista.get_tiempo_acumulado()  

    def imprimir(self):
        print(f"Nombre del equipo = {self.nombre}")
        print(f"País = {self.pais}")
        print(f"Total tiempo del equipo = {Equipo.total_tiempo}")

class Ciclista(ABC):
    def __init__(self, identificador, nombre):
        self.identificador = identificador
        self.nombre = nombre
        self.tiempo_acumulado = 0 

    @abstractmethod
    def imprimir_tipo(self):
        pass

    def get_identificador(self):
        return self.identificador

    def set_identificador(self, identificador):
        self.identificador = identificador

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_posicion_general(self, posicion_general):
        return posicion_general

    def set_posicion_general(self, posicion_general):
        self.posicion_general = posicion_general

    def get_tiempo_acumulado(self):
        return self.tiempo_acumulado

    def set_tiempo_acumulado(self, tiempo_acumulado):
        self.tiempo_acumulado = tiempo_acumulado

    def imprimir(self):
        print(f"Identificador = {self.identificador}")
        print(f"Nombre = {self.nombre}")
        print(f"Tiempo Acumulado = {self.tiempo_acumulado}")

class Velocista(Ciclista):
    def __init__(self, identificador, nombre, potencia_promedio, velocidad_promedio):
        super().__init__(identificador, nombre)
        self.potencia_promedio = potencia_promedio
        self.velocidad_promedio = velocidad_promedio

    def get_potencia_promedio(self):
        return self.potencia_promedio

    def set_potencia_promedio(self, potencia_promedio):
        self.potencia_promedio = potencia_promedio

    def get_velocidad_promedio(self):
        return self.velocidad_promedio

    def set_velocidad_promedio(self, velocidad_promedio):
        self.velocidad_promedio = velocidad_promedio

    def imprimir(self):
        super().imprimir()  
        print(f"Potencia promedio = {self.potencia_promedio}")
        print(f"Velocidad promedio = {self.velocidad_promedio}")

    def imprimir_tipo(self):
        return "Es un velocista"

class Escalador(Ciclista):
    def __init__(self, identificador, nombre, aceleracion_promedio, grado_rampa):
        super().__init__(identificador, nombre)
        self.aceleracion_promedio = aceleracion_promedio
        self.grado_rampa = grado_rampa

    def get_aceleracion_promedio(self):
        return self.aceleracion_promedio

    def set_aceleracion_promedio(self, aceleracion_promedio):
        self.aceleracion_promedio = aceleracion_promedio

    def get_grado_rampa(self):
        return self.grado_rampa

    def set_grado_rampa(self, grado_rampa):
        self.grado_rampa = grado_rampa

    def imprimir(self):
        super().imprimir()  
        print(f"Aceleración promedio = {self.aceleracion_promedio}")
        print(f"Grado de rampa = {self.grado_rampa}")

    def imprimir_tipo(self):
        return "Es un escalador"
    
class Contrarrelojista(Ciclista):
    def __init__(self, identificador, nombre, velocidad_maxima):
        super().__init__(identificador, nombre)
        self.velocidad_maxima = velocidad_maxima

    def get_velocidad_maxima(self):
        return self.velocidad_maxima

    def set_velocidad_maxima(self, velocidad_maxima):
        self.velocidad_maxima = velocidad_maxima

    def imprimir(self):
        super().imprimir()  
        print(f"Velocidad máxima = {self.velocidad_maxima}")

    def imprimir_tipo(self):
        return "Es un contrarrelojista"

def main():
    equipo1 = Equipo("Sky", "Estados Unidos")
    velocista1 = Velocista(123979, "Geraint Thomas", 320, 25)
    escalador1 = Escalador(123980, "Egan Bernal", 25, 10)
    contrarrelojista1 = Contrarrelojista(123981, "Jonathan Castroviejo", 120)

    equipo1.añadir_ciclista(velocista1)
    equipo1.añadir_ciclista(escalador1)
    equipo1.añadir_ciclista(contrarrelojista1)

    velocista1.set_tiempo_acumulado(365)
    escalador1.set_tiempo_acumulado(385)
    contrarrelojista1.set_tiempo_acumulado(370)

    equipo1.calcular_total_tiempo()
    equipo1.imprimir()
    equipo1.listar_equipo()

if __name__ == "__main__":
    main()
