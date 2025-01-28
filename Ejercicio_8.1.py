import tkinter as tk
from tkinter import messagebox

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.lista = ListaPersonas() 
        self.inicio()
        self.title("Personas")  
        self.geometry("270x350")  
        self.resizable(False, False)  

    def inicio(self):
        self.nombre_label = tk.Label(self, text="Nombre:")
        self.nombre_label.place(x=20, y=20)
        self.campo_nombre = tk.Entry(self)
        self.campo_nombre.place(x=105, y=20, width=135)

        self.apellidos_label = tk.Label(self, text="Apellidos:")
        self.apellidos_label.place(x=20, y=50)
        self.campo_apellidos = tk.Entry(self)
        self.campo_apellidos.place(x=105, y=50, width=135)

        self.telefono_label = tk.Label(self, text="Teléfono:")
        self.telefono_label.place(x=20, y=80)
        self.campo_telefono = tk.Entry(self)
        self.campo_telefono.place(x=105, y=80, width=135)

        self.direccion_label = tk.Label(self, text="Dirección:")
        self.direccion_label.place(x=20, y=110)
        self.campo_direccion = tk.Entry(self)
        self.campo_direccion.place(x=105, y=110, width=135)

        self.añadir_button = tk.Button(self, text="Añadir", command=self.añadir_persona)
        self.añadir_button.place(x=105, y=150)

        self.eliminar_button = tk.Button(self, text="Eliminar", command=self.eliminar_nombre)
        self.eliminar_button.place(x=20, y=280)

        self.borrar_lista_button = tk.Button(self, text="Borrar Lista", command=self.borrar_lista)
        self.borrar_lista_button.place(x=120, y=280)

        self.lista_nombres = tk.Listbox(self)
        self.lista_nombres.place(x=20, y=190, width=220, height=80)

    def añadir_persona(self):
        persona = Persona(self.campo_nombre.get(), self.campo_apellidos.get(), 
                          self.campo_telefono.get(), self.campo_direccion.get())
        self.lista.añadir_persona(persona)

        texto_persona = f"{self.campo_nombre.get()} - {self.campo_apellidos.get()} - {self.campo_telefono.get()} - {self.campo_direccion.get()}"
        self.lista_nombres.insert(tk.END, texto_persona)

        self.campo_nombre.delete(0, tk.END)
        self.campo_apellidos.delete(0, tk.END)
        self.campo_telefono.delete(0, tk.END)
        self.campo_direccion.delete(0, tk.END)

    def eliminar_nombre(self):
        try:
            selected_index = self.lista_nombres.curselection()[0]
            self.lista.eliminar_persona(selected_index)
            self.lista_nombres.delete(selected_index)
        except IndexError:
            messagebox.showerror("Error", "Debe seleccionar un elemento")

    def borrar_lista(self):
        self.lista.borrar_lista()
        self.lista_nombres.delete(0, tk.END)

class Persona:
    def __init__(self, nombre, apellidos, telefono, direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.direccion = direccion

class ListaPersonas:
    def __init__(self):
        self.personas = []

    def añadir_persona(self, persona):
        self.personas.append(persona)

    def eliminar_persona(self, indice):
        if 0 <= indice < len(self.personas):
            del self.personas[indice]

    def borrar_lista(self):
        self.personas.clear()
        
class ListaPersonas:
    def __init__(self):
        self.lista_personas = []  

    def añadir_persona(self, persona):
        self.lista_personas.append(persona)  

    def eliminar_persona(self, indice):
        if 0 <= indice < len(self.lista_personas):
            del self.lista_personas[indice] 

    def borrar_lista(self):
        self.lista_personas.clear()  

class Persona:
    def __init__(self, nombre, apellidos, telefono, direccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.direccion = direccion
from tkinter import Tk

class Principal:
    @staticmethod
    def main():
        mi_ventana_principal = VentanaPrincipal()
        mi_ventana_principal.mainloop()

if __name__ == "__main__":
    Principal.main()
