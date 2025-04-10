from .entities import pagina

class ModelPagina():
    # Metodo para registrar nuevos usuarios
    @classmethod
    def agregar(self, db, pagina):
        try:
            cursor = db.connection.cursor()
            cursor.execute(
                "call sp_AddReceta(%s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)",
                (pagina.nombre, pagina.autor, pagina.cantidadpersonas, pagina.tiempo,pagina.dificultad,pagina.ingredientes,
                 pagina.tips,pagina.preparacion, pagina.rutaimg, pagina.rutaimgapoyo, pagina.idUser, pagina.estrellas)
            )
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def obtenerrecetas(self, db):
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM recetas ORDER BY idReceta")  # Adjust the query as needed
        results = cursor.fetchall()  # Fetch all recipes
        cursor.close()
        return results  # Return the list of recipes