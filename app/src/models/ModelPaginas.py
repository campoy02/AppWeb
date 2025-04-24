from .entities.pagina import pagina

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
        cursor.execute("SELECT * FROM recetas ORDER BY idReceta")  
        results = cursor.fetchall()  
        cursor.close()
        return results  

    @classmethod
    def eliminar(cls, db, id):
        try:
            cursor = db.connection.cursor()
            cursor.execute("DELETE FROM recetas WHERE idReceta = %s", (id,))  
            db.connection.commit()
            cursor.close()
            return True
        except Exception as ex:
            raise Exception(ex)
    
    # Para sacar informacion de una pagina en especifico
    @classmethod
    def RecetaPorID(cls,db, id):
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM recetas where idReceta = %s", (id,))  
        row = cursor.fetchone()
        if row != None:
            PaginaRe = pagina(row[0],row[1], row[2], row[3] ,row[4] ,row[5] ,row[6], row[7],row[8],row[9],row[10],row[11],row[12],row[13])
            return PaginaRe
        else: 
            return None
        
    @classmethod
    def ActualizarVotos(cls,db,estrellas,id):
        cursor = db.connection.cursor()
        cursor.execute("UPDATE recetas SET estrellas = estrellas+%s WHERE idReceta = %s;", (estrellas,id))  
        cursor.execute("UPDATE recetas SET votos_totales = votos_totales+1 WHERE idReceta = %s;", (id))  
        db.connection.commit()
        cursor.close
        return True