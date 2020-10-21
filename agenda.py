import conexionContactos as db
import os



#************************************************************
#CLASE SELECTOR
#************************************************************

class Selector:
    def __init__(self, opciones):
        self.opciones = opciones.split(",")

    def selec(self):
        largo = self.largoLinea() + 10
        # os.system("CLS")
        print("-"*largo)
        print(self.opciones[0])  # TITULO
        print("-"*largo)
        ult = 0
        for x in range(1, len(self.opciones)):
            print("(" + str(x) + ")       "+self.opciones[x])
            ult = x
        print("-"*largo)
        print("("+str(ult+1) + ")    SALIR")
        print("-"*largo)
        rta = int(input("INGRESE UNA OPCION: "))
        if rta == ult+1:
            return 99

        return rta

    def largoLinea(self):
        mayor = -1
        for palabra in self.opciones:
            if len(palabra) > mayor:
                mayor = len(palabra)
        return mayor


#************************************************************
#CLASE CONTACTO
#************************************************************
class Contacto:
    def __init__(self,codigo=0,nombre="",apellido="",telefono="",mail="",direccion=""):
        self.id_contacto=codigo
        self.nombre=nombre
        self.apellido=apellido
        self.telefono=telefono
        self.mail=mail
        self.direccion=direccion

    def __str__(self):
        return "{:3d} {:10s} {:10s} {:10s} {:10s} {:10s}".format(self.id_contacto,self.nombre,
                                                 self.apellido,self.direccion,
                                                 self.telefono,self.mail,
                                                 self.direccion)
    def __repr__(self):
        return "{:3d} {:10s} {:10s} {:10s} {:10s} {:10s}".format(self.id_contacto,self.nombre,
                                                 self.apellido,self.direccion,
                                                 self.telefono,self.mail,
                                                 self.direccion)

    

        
    
#************************************************************
#CLASE AGENDA
#************************************************************    
class Agenda(object):
    def __init__(self):
        self.contacto = Contacto()

    def leer_contacto(self):   
        print("INGRESO DE UN CONTACTO")
        self.nombre = input("Nombre: ")
        self.apellido=input("Apellido: ")
        self.telefono=input("Telefono: ")
        self.mail=input("Mail: ")
        self.direccion=input("Dirección: ")

        return (self.nombre,self.apellido,self.telefono,self.mail,self.direccion)

    def alta_contacto(self):
        contacto=self.leer_contacto()
        conn=db.ConexionContactos()
        conn.alta(contacto)

    def listar_todos_contactos(self):
        conn=db.ConexionContactos()
        contactos = conn.recuperar_todos()
        print("{:3s} {:10s} {:10s} {:10s} {:10s} {:10s}".format("ID","NOMBRE","APELLIDO","TELEFONO","MAIL","DIRECCION"))
        for contacto in contactos:
            print(Contacto(contacto[0],contacto[1],contacto[2],contacto[3],contacto[4],contacto[5]))

    def listar_contactos(self,contactos):
        print("{:3s} {:10s} {:10s} {:10s} {:10s} {:10s}".format("ID","NOMBRE","APELLIDO","TELEFONO","MAIL","DIRECCION"))
        for contacto in contactos:
            print(Contacto(contacto[0],contacto[1],contacto[2],contacto[3],contacto[4],contacto[5]))

    def eliminar_contacto(self,id):
        conn=db.ConexionContactos()
        conn.baja((id,))
    
    def devolver_contactos(self):
        conn=db.ConexionContactos()
        contactos = conn.recuperar_todos()
        lista_contactos = []
        for contacto in contactos:
            lista_contactos.append(Contacto(contacto[0],contacto[1],contacto[2],contacto[3],contacto[4],contacto[5]))
        return lista_contactos
        

    def eliminar_contactos(self):
        opcion_busqueda=Selector("ELIMINAR POR,NOMBRE,APELLIDO,TELEFONO,MAIL,DIRECCION")
        opcion = opcion_busqueda.selec()
        if opcion == 1:
            nombre_buscar = str(input("Ingrese el nombre a buscar: "))
            contacto = db.ConexionContactos()
            resultado = contacto.consulta("nombre",(nombre_buscar,))
            self.listar_contactos(resultado)
            eliminar_id = int(input("Ingrese el ID del contacto a eliminar: "))
            self.eliminar_contacto(eliminar_id)
        if opcion == 2:
            apellido_buscar = str(input("Ingrese el apellido a buscar: "))
            contacto = db.ConexionContactos()
            resultado = contacto.consulta("apellido",(apellido_buscar,))
            self.listar_contactos(resultado)
            eliminar_id = int(input("Ingrese el ID del contacto a eliminar: "))
            self.eliminar_contacto(eliminar_id)
        if opcion == 3:
            telefono_buscar = str(input("Ingrese el telefono a buscar: "))
            contacto = db.ConexionContactos()
            resultado = contacto.consulta("telefono",(telefono_buscar,))
            self.listar_contactos(resultado)
            eliminar_id = int(input("Ingrese el ID del contacto a eliminar: "))
            self.eliminar_contacto(eliminar_id)
        if opcion == 4:
            mail_buscar = str(input("Ingrese el mail a buscar: "))
            contacto = db.ConexionContactos()
            resultado = contacto.consulta("mail",(mail_buscar,))
            self.listar_contactos(resultado)
            eliminar_id = int(input("Ingrese el ID del contacto a eliminar: "))
            self.eliminar_contacto(eliminar_id)
        if opcion == 5:
            direccion_buscar = str(input("Ingrese el direccion a buscar: "))
            contacto = db.ConexionContactos()
            resultado = contacto.consulta("direccion",(direccion_buscar,))
            self.listar_contactos(resultado)
            eliminar_id = int(input("Ingrese el ID del contacto a eliminar: "))
            self.eliminar_contacto(eliminar_id)
    
    def buscar_contacto(self):
        os.system("CLS")
        opcion_busqueda=Selector("BUSCAR POR,NOMBRE,APELLIDO,TELEFONO,MAIL,DIRECCION")
        terminar = False
        resultado = []
        while not terminar:
            opcion = opcion_busqueda.selec()            
            if opcion == 1:
                nombre_buscar = str(input("Ingrese el nombre a buscar: "))
                contacto = db.ConexionContactos()
                resultado = contacto.consulta("nombre",(nombre_buscar,))
                self.listar_contactos(resultado)
            if opcion == 2:
                apellido_buscar = str(input("Ingrese el apellido a buscar: "))
                contacto = db.ConexionContactos()
                resultado = contacto.consulta("apellido",(apellido_buscar,))
                self.listar_contactos(resultado)
            if opcion == 3:
                telefono_buscar = str(input("Ingrese el telefono a buscar: "))
                contacto = db.ConexionContactos()
                resultado = contacto.consulta("telefono",(telefono_buscar,))
                self.listar_contactos(resultado)
            if opcion == 4:
                mail_buscar = str(input("Ingrese el mail a buscar: "))
                contacto = db.ConexionContactos()
                resultado = contacto.consulta("mail",(mail_buscar,))
                self.listar_contactos(resultado)
            if opcion == 5:
                direccion_buscar = str(input("Ingrese el direccion a buscar: "))
                contacto = db.ConexionContactos()
                resultado = contacto.consulta("direccion",(direccion_buscar,))
                self.listar_contactos(resultado)
            if opcion == 99:
                terminar = True
        return terminar

    def inicio(self):
        menu = Selector("AGENDA,LISTAR CONTACTOS,AGREGAR,BUSCAR,ELIMINAR")
        terminar = False
        while not terminar:
            opcion = menu.selec()
            if opcion == 1:
                self.listar_todos_contactos()
            if opcion == 2:
                self.alta_contacto()
            if opcion == 3:
                self.buscar_contacto()
            if opcion == 4:
                self.eliminar_contactos()
            if opcion == 99:
                terminar = True
        return terminar   

#************************************************************
#PROGRAMA PRINCIPAL
#************************************************************
def main():
    Agenda().inicio()

if __name__ == "__main__":
    main() 


