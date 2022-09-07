from ast import Str
import pymysql
from CapaNegocio.Autos import Auto
from CapaNegocio.Siniestro import Siniestro

from CapaNegocio.Personas import Persona

from .DataBase import Database




class Vincular(Database):
    def __init__(self):
        super().__init__()

    def vincularPersonaAuto(self, Id, IdAuto):
        #verificar que la persona existe en la base de datos
        #lo mismo para auto
        #insertar en en la tabla correspondiente
        tpersona=Persona()
        tauto=Auto()
        if tpersona.ExistePersona(Id):
            if tauto.getUnAuto(IdAuto):
                sql="INSERT INTO aseguradora.persona_has_auto VALUES ({},'{}')".format(Id, IdAuto)
                self.cursor.execute(sql)
                self.cursor.commit()
                return "Se insertó exitosamente"
            else:
                return "La matrícula ingresada No Existe "
        else:
            return "El Id persona ingresado NO Existe"

    def VincularAutoInforme(self, IdAuto, IdInforme, Importedaño):
        
        #verificar si existe el auto
        #traer la persona asociada a esa persona
        #insertar en la tabla correspondiente
        tpersona=Persona()
        tauto=Auto()
        tinformes=Siniestro()
        if tauto.getUnAuto(IdAuto):
            idPersona=self.traerIdConductor(IdAuto)
            if idPersona!=None:          
                if tinformes.getInforme(IdInforme):
                    sql="INSERT INTO aseguradora.informe_accidente_has_persona_has_auto VALUES ({},{},'{}', {})".format(IdInforme, idPersona, IdAuto, Importedaño)
                    self.cursor.execute(sql)
                    self.cursor.commit()
                    return "Se insertó exitosamente"
                else:
                    return "El informe No Existe "
            else:
                return "El auto no tiene conductor asignado"
        else:
            return "El auto ingresado NO Existe"


    def TraerIdConductor(self, IdAuto):
        sql="SELECT PERSONA_idPERSONA FROM aseguradora.persona_has_auto WHERE AUTO_MATRICULA='{}'".format(IdAuto)
        self.cursor.execute(sql)
        self.cursor.commit()
        return self.cursor.fetchone()