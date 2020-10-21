from tkinter import *
from tkinter import ttk
import tkinter as tk
import agenda

class Aplicacion():
    def __init__(self):
        self.raiz = tk.Tk()
        self.raiz.geometry("600x400")
        
        self.ingresar_opcion1 = ttk.Button(self.raiz,text="LISTAR TODO",command=self.listar)
        self.ingresar_opcion1.grid(sticky="W",column=0,row=0)

        self.numero_buscar = tk.StringVar()
        self.casillero = ttk.Entry(self.raiz,textvariable=self.numero_buscar)
        self.casillero.grid(column=1,row=0)

        self.ingresar_opcion2 = ttk.Button(self.raiz,text="BUSCAR",command=self.buscar)
        self.ingresar_opcion2.grid(sticky="W",column=2,row=0)


    def buscar(self):
        agenda_nueva = agenda.db.ConexionContactos()
        lista_contactos = agenda_nueva.consulta("nombre",(self.numero_buscar.get(),))
        self.etiqueta2_id = tk.Label(self.raiz,text="ID")         
        self.etiqueta2_id.grid(sticky="W",column=0,row=1)

        self.etiqueta2_nombre = tk.Label(self.raiz,text="NOMBRE")         
        self.etiqueta2_nombre.grid(sticky="W",column=1,row=1)

        self.etiqueta2_apellido = tk.Label(self.raiz,text="APELLIDO")         
        self.etiqueta2_apellido.grid(sticky="W",column=2,row=1)

        self.etiqueta2_telefono = tk.Label(self.raiz,text="TELEFONO")         
        self.etiqueta2_telefono.grid(sticky="W",column=3,row=1)

        self.etiqueta2_mail = tk.Label(self.raiz,text="MAIL")         
        self.etiqueta2_mail.grid(sticky="W",column=4,row=1)

        self.etiqueta2_direccion = tk.Label(self.raiz,text="DIRECCION")         
        self.etiqueta2_direccion.grid(sticky="W",column=5,row=1)

        for x in range(len(lista_contactos)):
            self.etiqueta_id = tk.Label(self.raiz,text=lista_contactos[x][0])         
            self.etiqueta_id.grid(sticky="W",column=0,row=x+2)

            self.etiqueta_nombre = tk.Label(self.raiz,text=lista_contactos[x][1])         
            self.etiqueta_nombre.grid(sticky="W",column=1,row=x+2)

            self.etiqueta_apellido = tk.Label(self.raiz,text=lista_contactos[x][2])         
            self.etiqueta_apellido.grid(sticky="W",column=2,row=x+2)

            self.etiqueta_telefono = tk.Label(self.raiz,text=lista_contactos[x][3])         
            self.etiqueta_telefono.grid(sticky="W",column=3,row=x+2)

            self.etiqueta_mail = tk.Label(self.raiz,text=lista_contactos[x][4])         
            self.etiqueta_mail.grid(sticky="W",column=4,row=x+2)

            self.etiqueta_direccion = tk.Label(self.raiz,text=lista_contactos[x][5])         
            self.etiqueta_direccion.grid(sticky="W",column=5,row=x+2)



    def listar(self):
        agenda_nueva = agenda.Agenda()
        lista_contactos = agenda_nueva.devolver_contactos()
        self.etiqueta2_id = tk.Label(self.raiz,text="ID")         
        self.etiqueta2_id.grid(sticky="W",column=0,row=1)

        self.etiqueta2_nombre = tk.Label(self.raiz,text="NOMBRE")         
        self.etiqueta2_nombre.grid(sticky="W",column=1,row=1)

        self.etiqueta2_apellido = tk.Label(self.raiz,text="APELLIDO")         
        self.etiqueta2_apellido.grid(sticky="W",column=2,row=1)

        self.etiqueta2_telefono = tk.Label(self.raiz,text="TELEFONO")         
        self.etiqueta2_telefono.grid(sticky="W",column=3,row=1)

        self.etiqueta2_mail = tk.Label(self.raiz,text="MAIL")         
        self.etiqueta2_mail.grid(sticky="W",column=4,row=1)

        self.etiqueta2_direccion = tk.Label(self.raiz,text="DIRECCION")         
        self.etiqueta2_direccion.grid(sticky="W",column=5,row=1)

        for x in range(len(lista_contactos)):
            self.etiqueta_id = tk.Label(self.raiz,text=lista_contactos[x].id_contacto)         
            self.etiqueta_id.grid(sticky="W",column=0,row=x+2)

            self.etiqueta_nombre = tk.Label(self.raiz,text=lista_contactos[x].nombre)         
            self.etiqueta_nombre.grid(sticky="W",column=1,row=x+2)

            self.etiqueta_apellido = tk.Label(self.raiz,text=lista_contactos[x].apellido)         
            self.etiqueta_apellido.grid(sticky="W",column=2,row=x+2)

            self.etiqueta_telefono = tk.Label(self.raiz,text=lista_contactos[x].telefono)         
            self.etiqueta_telefono.grid(sticky="W",column=3,row=x+2)

            self.etiqueta_mail = tk.Label(self.raiz,text=lista_contactos[x].mail)         
            self.etiqueta_mail.grid(sticky="W",column=4,row=x+2)

            self.etiqueta_direccion = tk.Label(self.raiz,text=lista_contactos[x].direccion)         
            self.etiqueta_direccion.grid(sticky="W",column=5,row=x+2)

            

        
    def iniciar(self):
        self.raiz.mainloop()

def main():
    Aplicacion().iniciar()

main()