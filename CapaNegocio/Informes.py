from ast import Str

import pymysql
from .DataBase import Database

class Informe(Database):
    def __init__(self):
        super().__init__()


    def getUnInforme(self, idInformeAccidente):
        sql="SELECT * FROM aseguradora.informe_accidente where idInformeAccidente='{}'".format(idInformeAccidente)
        print (sql)

        self.cursor.execute(sql)
        return self.cursor.fetchone()
      
    def getTodos(self):
        sql="SELECT * FROM aseguradora.informe_accidente"
        

        self.cursor.execute(sql)
        return self.cursor.fetchall()   

    def insertInforme (self, idInformeAccidente, InformeAccidenteFecha, InformeAccidenteLugar):
        sql='''INSERT INTO aseguradora.informe_accidente VALUES({},,'{}')'''.format(idInformeAccidente, InformeAccidenteFecha, InformeAccidenteLugar)
        self.cursor.execute(sql)
        self.connection.commit()

    def updateInforme(self, idInformeAccidente, InformeAccidenteFecha, InformeAccidenteLugar):
        sql="UPDATE aseguradora.informe_accidente SET  InformeAccidenteFecha='{}', InformeAccidenteLugar='{}' WHERE idInformeAccidente={}".format( InformeAccidenteFecha, InformeAccidenteLugar, idInformeAccidente)
        self.cursor.execute(sql)
        self.connection.commit()

    def borrarInforme(self, idInformeAccidente):
        sql="DELETE FROM aseguradora.informe_accidente WHERE idInformeAccidente='{}'".format(idInformeAccidente)
        self.cursor.execute(sql)
        self.connection.commit()