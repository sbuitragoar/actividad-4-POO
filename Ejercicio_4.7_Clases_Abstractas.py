from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, sonido, alimentos, habitat, nombre_cientifico):
        self.sonido = sonido
        self.alimentos = alimentos
        self.habitat = habitat
        self.nombre_cientifico = nombre_cientifico

    @abstractmethod
    def get_nombre_cientifico(self):
        pass

    @abstractmethod
    def get_sonido(self):
        pass

    @abstractmethod
    def get_alimentos(self):
        pass

    @abstractmethod
    def get_habitat(self):
        pass

class Canido(Animal, ABC):
    def __init__(self):
        super().__init__("Sonido genérico", "Alimentos genéricos", "Hábitat genérico", "Nombre científico genérico")

class Perro(Canido):
    def __init__(self):
        super().__init__()
        self.sonido = "Ladrido"
        self.alimentos = "Carnívoro"
        self.habitat = "Doméstico"
        self.nombre_cientifico = "Canis lupus familiaris"

    def get_sonido(self):
        return self.sonido

    def get_alimentos(self):
        return self.alimentos

    def get_habitat(self):
        return self.habitat

    def get_nombre_cientifico(self):
        return self.nombre_cientifico

class Lobo(Canido):
    def __init__(self):
        super().__init__()
        self.sonido = "Aullido"
        self.alimentos = "Carnívoro"
        self.habitat = "Bosque"
        self.nombre_cientifico = "Canis lupus"

    def get_sonido(self):
        return self.sonido

    def get_alimentos(self):
        return self.alimentos

    def get_habitat(self):
        return self.habitat

    def get_nombre_cientifico(self):
        return self.nombre_cientifico

class Felino(Animal):
    def __init__(self):
        super().__init__("Sonido genérico", "Alimentos genéricos", "Hábitat genérico", "Nombre científico genérico")

class Leon(Felino):
    def __init__(self):
        super().__init__()
        self.sonido = "Rugido"
        self.alimentos = "Carnívoro"
        self.habitat = "Praderas"
        self.nombre_cientifico = "Panthera leo"

    def get_sonido(self):
        return self.sonido
    
    def get_alimentos(self):
        return self.alimentos
    
    def get_habitat(self):
        return self.habitat
    
    def get_nombre_cientifico(self):
        return self.nombre_cientifico

class Gato(Felino):
    def __init__(self):
        super().__init__()
        self.sonido = "Maullido"
        self.alimentos = "Ratones"
        self.habitat = "Doméstico"
        self.nombre_cientifico = "Felis silvestris catus"

    def get_sonido(self):
        return self.sonido
    
    def get_alimentos(self):
        return self.alimentos
    
    def get_habitat(self):
        return self.habitat
    
    def get_nombre_cientifico(self):
        return self.nombre_cientifico

class Prueba:
    def main(self):
        animales = [Gato(), Perro(), Lobo(), Leon()] 
        for animal in animales:
            print(animal.get_nombre_cientifico())
            print("Sonido:", animal.get_sonido())
            print("Alimentos:", animal.get_alimentos())
            print("Hábitat:", animal.get_habitat())
            print()

prueba = Prueba()
prueba.main()
