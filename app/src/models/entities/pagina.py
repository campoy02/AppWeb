class pagina():
    def __init__(self, idReceta, nombre, autor, cantidadpersonas, tiempo, dificultad, ingredientes, tips, preparacion, rutaimg, rutaimgapoyo, idUser, estrellas, votos_totales) -> None:
        self.idReceta = idReceta
        self.nombre = nombre
        self.autor = autor
        self.cantidadpersonas = cantidadpersonas
        self.tiempo = tiempo 
        self.dificultad = dificultad
        self.ingredientes = ingredientes
        self.tips = tips
        self.preparacion = preparacion
        self.rutaimg = rutaimg
        self.rutaimgapoyo = rutaimgapoyo
        self.idUser = idUser
        self.estrellas = estrellas
        self.votos_totales = votos_totales