from ast import Str

import pymysql
from .DataBase import Database



class Persona(Database):
    def __init__(self):
        super().__init__()


    def getUnaPersona(self, idPersona):
        sql="SELECT * FROM aseguradora.persona WHERE PERSONA_CARNET_CONDUCTOR='{}'".format(idPersona)
        print (sql)

        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def getUnId(self, idPersona):
        sql="SELECT * FROM aseguradora.persona WHERE idPERSONA='{}'".format(idPersona)
        print (sql)

        self.cursor.execute(sql)
        return self.cursor.fetchone()
      
    def getTodos(self):
        sql="SELECT * FROM aseguradora.persona"
        

        self.cursor.execute(sql)
        return self.cursor.fetchall()   

    def insertPersona (self, carnet, nombre, direccion):

        sql="INSERT INTO aseguradora.persona (PERSONA_CARNET_CONDUCTOR, PERSONA_NOMBRE, PERSONA_DIRECCION ) VALUES('{}','{}','{}')".format( carnet, nombre, direccion)
        self.cursor.execute(sql)
        self.connection.commit()

    def updatePersona(self, id, carnet, nombre, direccion):
        sql="UPDATE aseguradora.persona SET  PERSONA_CARNET_CONDUCTOR='{}', PERSONA_NOMBRE='{}', PERSONA_DIRECCION='{}' WHERE idPERSONA={}".format( carnet, nombre, direccion, id)
        self.cursor.execute(sql)
        self.connection.commit()

    def borrarPersona(self, id):
        sql="DELETE FROM aseguradora.PERSONA WHERE idPERSONA='{}'".format(id)
        self.cursor.execute(sql)
        self.connection.commit()

    def ExistePersona(self, idPersona):
        sql="SELECT * FROM aseguradora.persona WHERE idPERSONA='{}'".format(idPersona)
        persona=self.cursor.fetchone()
        return persona!=None




