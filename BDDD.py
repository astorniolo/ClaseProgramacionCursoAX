#para hacerlo modulo, creo carpeta "aseguradora" dentro meto el modulo
#o sea este archivo
#y creo uno que se llama __init__.py



from ast import Str

import pymysql


class Database:
    # Genero la apertura y cierre con la Base de Datos 
    def __init__(self) :
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='Simoncito#44',
            db='aseguradora'
        )
        self.cursor=self.connection.cursor()
        print("Coneccion establecida")

    def close(self):
        self.connection.close()


class Auto(Database):
    def __init__(self):
        super().__init__()

    
    def getUnAuto(self, matricula):
        sql="SELECT * FROM aseguradora.AUTO where MATRICULA='{}'".format(matricula)
        print (sql)

        self.cursor.execute(sql)
        return self.cursor.fetchone()
      
    def getTodos(self):
        sql="SELECT * FROM aseguradora.auto"
        

        self.cursor.execute(sql)
        return self.cursor.fetchall()   

    def insertAuto (self, matricula, modelo, año):
        sql="INSERT INTO aseguradora.auto VALUES('{}','{}',{})".format(matricula, modelo, año)
        self.cursor.execute(sql)
        self.connection.commit()

    def updateAuto(self, matricula, modelo, año):
        sql="UPDATE aseguradora.auto SET  AUTO_MODELO='{}', AUTO_AÑO={} WHERE matricula='{}'".format( modelo, año, matricula)
        self.cursor.execute(sql)
        self.connection.commit()

    def borrarAuto(self, matricula):
        sql="DELETE FROM aseguradora.auto WHERE MATRICULA='{}'".format(matricula)
        self.cursor.execute(sql)
        self.connection.commit()

#############OTROS MÉTODOS
    def tuvoAccidente(self, matricula):
        sql="SELECT * FROM persona_has_auto_has_informeaccidente WHERE persona_has_auto_auto_matricula='{}'".format(matricula)
        self.cursor.execute(sql)
        lista= self.cursor.fetchall
        return lista !=()
    
    def siniestrosDeUnAuto(self, matricula):
        sql="SELECT InformeAccidenteFecha, InformeAccidenteLugar, ImporteDaño FROM aseguradora.persona        "
        self.cursor.execute(sql)
        return self.cursor.fetchall()





#############MAITN#################

TablaAutos=Auto()
autoSuzuki=TablaAutos.getUnAuto("ABC123")
# print(autoSuzuki.MATRICULA,autoSuzuki.AUTO_MODELO, autoSuzuki.AUTO_AÑO)
print (autoSuzuki)
todos=TablaAutos.getTodos()
print(todos)
# TablaAutos.insertAuto("bee628", "Renault", 1998)
# todos=TablaAutos.getTodos()
print(todos)
TablaAutos.updateAuto("bee628", "Ford", 2000)
todos=TablaAutos.getTodos()
print(todos)
TablaAutos.borrarAuto("bee628")
todos=TablaAutos.getTodos()
print(todos)







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
        sql="INSERT INTO aseguradora.informe_accidente VALUES({},'{}','{}')".format(idInformeAccidente, InformeAccidenteFecha, InformeAccidenteLugar)
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



class Persona(Database):
    def __init__(self):
        super().__init__()


    def getUnaPersona(self, idPersona):
        sql="SELECT * FROM aseguradora.persona WHERE idPERSONA='{}'".format(idPersona)
        print (sql)

        self.cursor.execute(sql)
        return self.cursor.fetchone()
      
    def getTodos(self):
        sql="SELECT * FROM aseguradora.persona"
        

        self.cursor.execute(sql)
        return self.cursor.fetchall()   

    def insertPersona (self, id, carnet, nombre, direccion):
        sql="INSERT INTO aseguradora.persona VALUES({},'{}','{}','{}')".format(id, carnet, nombre, direccion)
        self.cursor.execute(sql)
        self.connection.commit()

    def updatePersona(self, id, carnet, nombre, direccion):
        sql="UPDATE aseguradora.persona SET  PERSONA_CARNET_CONDUCIR='{}', PERSONA_NOMBRE='{}', PERSONA_DIRECCION='{}' WHERE idPERSONA={}".format( carnet, nombre, direccion, id)
        self.cursor.execute(sql)
        self.connection.commit()

    def borrarPersona(self, id):
        sql="DELETE FROM aseguradora.PERSONA WHERE idPERSONA='{}'".format(id)
        self.cursor.execute(sql)
        self.connection.commit()




