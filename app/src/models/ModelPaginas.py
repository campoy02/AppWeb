from .entities import pagina

class ModelPagina:
    # Método para registrar nuevos usuarios
    @classmethod
    def agregar(cls, db, pagina):
        try:
            cursor = db.connection.cursor()
            cursor.execute(
                "call sp_AddReceta(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (pagina.nombre, pagina.autor, pagina.cantidadpersonas, pagina.tiempo, pagina.dificultad,
                 pagina.ingredientes, pagina.tips, pagina.preparacion, pagina.rutaimg, pagina.rutaimgapoyo,
                 pagina.idUser , pagina.estrellas)
            )
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def obtenerrecetas(cls, db):
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM recetas ORDER BY idReceta")  # Ajusta la consulta según sea necesario
        results = cursor.fetchall()  # Fetch all recipes
        cursor.close()
        return results  # Return the list of recipes

    @classmethod
    def eliminar(cls, db, id):
        try:
            cursor = db.connection.cursor()
            cursor.execute("DELETE FROM recetas WHERE idReceta = %s", (id,))  # Asegúrate de que el nombre de la columna sea correcto
            db.connection.commit()
            cursor.close()
            return True
        except Exception as ex:
            raise Exception(ex)