from ast import Str


from .DataBase import Database

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
        sql="INSERT INTO aseguradora.auto VALUES('{}','{}',{})".format(matricula.upper(), modelo.upper(), año)
        self.cursor.execute(sql)
        self.connection.commit()

    def updateAuto(self, matricula, modelo, año):
        sql="UPDATE aseguradora.auto SET  AUTO_MODELO='{}', AUTO_AÑO={} WHERE matricula='{}'".format( modelo.upper(), año, matricula.upper())
        self.cursor.execute(sql)
        self.connection.commit()

    def borrarAuto(self, matricula):
        sql="DELETE FROM aseguradora.auto WHERE MATRICULA='{}'".format(matricula.upper())
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