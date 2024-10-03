from sqlalchemy import text
from .entities.usuario import User

class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            
            consulta = text("SELECT * FROM usuario WHERE usuario = :usuario")
            result = db.session.execute(consulta, {"usuario": user.usuario}).fetchone()
            #user = db.session.execute(f"SELECT * FROM usuario WHERE usuario = '{user.usuario}'").fetchone()
            if result is not None:
                user = User(result[0], result[1])
                return user
            else:
                print("No existe")
                return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def RegistroUsuario(self, db, user):
        procedimiento = None
        try:
            consulta = text("CALL proc_Registro_Usuario(:nombre, :password)")
            result = db.session.execute(consulta, {'nombre': user.usuario, 'password': user.password})
            #print(user.usuario, user.password) 
            #procedimiento = db.cursor()
            db.session.commit()
            exito = self.login(db, user)
            print("Registro exitoso", "success")
            return exito
        except Exception as ex:
            raise Exception(ex)

