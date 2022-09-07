from ast import Str


import pymysql

from CapaNegocio.DataBase import Database
#from CapaNegocio.DataBase import Database


class Siniestro (Database):
    def __init__(self):
        super().__init__()


    def getInforme(self, IdInforme):
        sql="SELECT * FROM aseguradora.informe_accidente WHERE idINFORME_ACCIDENTE={}".format(IdInforme)
        print (sql)
        self.cursor.execute(sql)
        return self.cursor.fetchone()



    def getTodosInformes(self):
        sql="SELECT * FROM aseguradora.informe_accidente"
        self.cursor.execute(sql)
        return self.cursor.fetchall() 

    def InsertarInforme(self, IdInforme, InformeFecha, InformeLugar):
        sql="INSERT INTO aseguradora.informe_accidente (idINFORME_ACCIDENTE,INFORME_ACCIDENTE_FECHA,INFORME_ACCIDENTE_LUGAR) VALUES({},{} ,'{}')".format( IdInforme, InformeFecha, InformeLugar)
        self.cursor.execute(sql)
        print(sql)
        self.connection.commit()
        return "Informe Insertado exitosamente"
        
    def getUnInformeLista(self):
        pass    


    def DeleteInforme(self, IdInforme):
        sql="DELETE FROM aseguradora.informe_accidente={}".format(IdInforme)
        self.cursor.execute(sql)
        self.connection.commit()

    def UpdateInforme(self,IdInforme, InformeFecha, InformeLugar):
        sql="UPDATE aseguradora.informe_accidente SET  INFORME_ACCIDENTE_FECHA={}, INFORME_ACCIDENTE_LUGAR='{}' WHERE idINFORME_ACCIDENTE={}".format( InformeFecha, InformeLugar, IdInforme)
        self.cursor.execute(sql)
        self.connection.commit()