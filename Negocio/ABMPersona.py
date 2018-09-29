from DBase import PersonaDB
from DBase import UsuarioDB


class ABMPersona():
    def __init__(self):
        self.perDB = PersonaDB.PersonaDB()
        self.usuDB = UsuarioDB.UsuarioDB()

    def altaPersona(self,per,us):
        pers=self.buscarPersonaPorDni(per)
        usus=self.usuDB.buscarUsuario(us)
        if(pers==None and usus==None):
            guardado = self.perDB.alta(per,us)
            return guardado
        else:
            return False

    def listarPersonas(self):
        return self.perDB.listar()

    def buscarPersonaPorDni(self,per):
        return self.perDB.buscarPersonaPorDni(per)

    def buscarPersonaPorID(self,id):
        return self.perDB.buscarPersonaPorID(id)

    def actualizarPersona(self,per):
        pers=self.buscarPersonaPorDni(per)
        if(pers==None or pers.idpersona==per.idpersona):
            return self.perDB.actualizarPersona(per)
        else:
            return False
