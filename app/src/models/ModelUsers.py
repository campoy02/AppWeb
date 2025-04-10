from .entities.users import User

# Lo que hace esta aplicacion .py es convertir la tabla "users" de la base de datos en un objeto # 
# El retorno de el metodo login retorna la informacion completa de el usuario recibiendo solo el username y contraseña #

# El retorno de el metodo get_by_id regresa la informacion de usuario completa con solo su id #
# Ambos metodos reciben db como parametros, Para el caso de este proyecto, ese parametro siempre debe ponerse como "db" cada que llames el metodo en app.py #

class ModelUsers():
    #Metodo para verificar las credenciales para el inicio de sesion
    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            cursor.execute(
                "call sp_verifyIdentity(%s, %s)",
                (user.username, user.password)
            )
            row = cursor.fetchone()
            if row[0] != None:
                user = User(row[0], row[1], row[2], row[4], row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    # Metodo para obtener informacion de un usuario a traves de su ID
    @classmethod
    def get_by_id(cls, db, id):
        try:
            cursor = db.connection.cursor()
            cursor.execute(
                "SELECT * FROM users WHERE id = %s", (id,)
            )
            row = cursor.fetchone()
            if row is not None:
                return User(row[0], row[1], row[2], row[4], row[3])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    # Metodo para registrar nuevos usuarios
    @classmethod
    def registrar(self, db, user):
        try:
            cursor = db.connection.cursor()
            cursor.execute(
                "call sp_AddUser(%s, %s, %s, %s, %s)",
                (user.username, user.password,user.fullname, 0, user.email)
            )
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)