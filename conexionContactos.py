import mysql.connector
# Esta línea importa el módulo MySQL Connector
# Python en su programa para que pueda usar la
# API de este módulo para conectar MySQL.
from mysql.connector import Error
# El objeto de error del conector mysql se usa para
# mostrarnos un error cuando no pudimos conectar las
# bases de datos o si se produjo algún otro error de
# la base de datos al trabajar con la base de datos.
# Ejemplo ERROR DE ACCESO DENEGADO cuando el nombre
# de usuario o la contraseña son incorrectos.


class ConexionContactos:
    def __init__(self, database="agenda", host="localhost", username="root", password=""):
        self.database = database
        self.host = host
        self.username = username
        self.password = password

    def get_conexion(self):
        la_conexion = None

        try:
            la_conexion = mysql.connector.connect(
                host=self.host,                                                 
                database=self.database,
                user=self.username,
                passwd=self.password
            )
        except (Exception, Error) as error:
            print("Error al abrir la Base de Datos: {}".format(error))
        return la_conexion

    def cerrar_conexion(self, la_conexion):
        if la_conexion:
            la_conexion.close()

    def abrir(self):
        la_conexion = None

        try:
            la_conexion = mysql.connector.connect(
                host=self.host,                                                 
                database=self.database,
                user=self.username,
                passwd=self.password
            )

        except (Exception, Error) as error:
            print("Error al abrir la Base de Datos: {}".format(error))

        return la_conexion



    def alta(self, los_datos):

        try:
            la_conexion = self.abrir()
            el_cursor = la_conexion.cursor()
            consulta_sql = "INSERT INTO contactos(nombre,apellido,telefono,mail,direccion) VALUES (%s,%s,%s,%s,%s)"
            el_cursor.execute(consulta_sql, los_datos)
            la_conexion.commit()
            el_cursor.close()
            la_conexion.close()
        except (Exception, Error) as error:
            print("Error al hacer el alta: {}".format(error))

    
    def alta_prueba(self, parametros, los_datos):

        try:
            la_conexion = self.abrir()
            el_cursor = la_conexion.cursor()
            consulta_sql = "INSERT INTO contactos({}) VALUES (%s,%s,%s,%s,%s)".format(parametros)
            el_cursor.execute(consulta_sql, los_datos)
            la_conexion.commit()
            el_cursor.close()
            la_conexion.close()
        except (Exception, Error) as error:
            print("Error al hacer el alta: {}".format(error))

    def consulta_prueba(self, parametro1,los_datos):
        respuesta = []
        try:
            la_conexion = self.abrir()
            el_cursor = la_conexion.cursor()
            consulta_sql = "SELECT {} FROM contactos WHERE nombre=%s".format(parametro1)
            el_cursor.execute(consulta_sql, los_datos)
            respuesta = el_cursor.fetchall()
        except (Exception, Error) as error:
            print("Error al hacer la consulta: {}".format(error))
        finally:
            if la_conexion.is_connected():
                el_cursor.close()
                la_conexion.close()
        return respuesta


    def consulta(self, parametro1,los_datos):
        respuesta = []
        try:
            la_conexion = self.abrir()
            el_cursor = la_conexion.cursor()
            consulta_sql = "SELECT id_contacto,nombre,apellido,telefono,mail,direccion FROM contactos WHERE {}=%s".format(parametro1)
            el_cursor.execute(consulta_sql, los_datos)
            respuesta = el_cursor.fetchall()
        except (Exception, Error) as error:
            print("Error al hacer la consulta: {}".format(error))
        finally:
            if la_conexion.is_connected():
                el_cursor.close()
                la_conexion.close()
        return respuesta

    def recuperar_todos(self):
        respuesta = []
        try:
            la_conexion = self.abrir()
            el_cursor = la_conexion.cursor()
            consulta_sql = "SELECT id_contacto, nombre,apellido,telefono,mail,direccion FROM contactos"
            el_cursor.execute(consulta_sql)
            respuesta = el_cursor.fetchall()
        except (Exception, Error) as error:
            print("Error al recuperar los datos: {}".format(error))
        finally:
            if la_conexion.is_connected():
                el_cursor.close()
                la_conexion.close()
        return respuesta
        # fetchall() recupera todas las filas del resultado de una consulta.
        # Devuelve todas las filas como una lista de tuplas.
        # Se devuelve una lista vacía si no hay registros para recuperar.

    def baja(self, los_datos):
        respuesta = 0
        try:
            la_conexion = self.abrir()
            el_cursor = la_conexion.cursor()
            consulta_sql = "DELETE from contactos WHERE id_contacto=%s"
            el_cursor.execute(consulta_sql, los_datos)
            respuesta = el_cursor.rowcount
            la_conexion.commit()
            # retornamos la cantidad de filas borradas

        except (Exception, Error) as error:
            print("Error al eliminar los datos: {}".format(error))
        finally:
            if la_conexion.is_connected():
                el_cursor.close()
                la_conexion.close()
        return respuesta

    def modificacion(self, los_datos):
        respuesta = 0
        try:
            la_conexion = self.abrir()
            el_cursor = la_conexion.cursor()
            consulta_sql = "UPDATE contactos set nombre=%s,apellido=%s,telefono=%s,mail=%s,direccion=%s WHERE codigo=%s"
            el_cursor.execute(consulta_sql, los_datos)
            la_conexion.commit()
            # retornamos la cantidad de filas modificadas
            respuesta = el_cursor.rowcount
        except (Exception, Error) as error:
            print("Error al modificar los datos: {}".format(error))
        finally:
            if la_conexion.is_connected():
                el_cursor.close()
                la_conexion.close()
        return respuesta

    def alta_grupal(self, lista_con_los_datos):
        try:
            la_conexion = self.abrir()
            el_cursor = la_conexion.cursor(prepared=True)
            consulta_sql = "INSERT INTO contactos(nombre,apellido,telefono,mail,direccion) VALUES (%s,%s,%s,%s,%s)"

            for los_datos in lista_con_los_datos:
                el_cursor.execute(consulta_sql, los_datos)

            la_conexion.commit()
        except (Exception, Error) as error:
            print("Error al hacer el alta grupal: {}".format(error))
        finally:
            if la_conexion.is_connected():
                el_cursor.close()
                la_conexion.close()



def main():
    db = ConexionContactos()
    resultado = db.consulta("nombre",("Javier",))
    print(resultado)

if __name__ == "__main__":
    main() 