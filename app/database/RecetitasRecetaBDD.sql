use tiendarecetitas;

CREATE TABLE recetas (
idReceta smallint unsigned NOT NULL AUTO_INCREMENT primary key,
nombre varchar(30) NOT NULL,
autor varchar(30),
cantidadpersonas int,
tiempo int,
dificultad varchar(25),
ingredientes text,
tips text,
preparacion text,
rutaimg text,
rutaimgapoyo text,
idUser smallint unsigned not null,
FOREIGN KEY (idUser) REFERENCES Users(id),
estrellas int
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

alter table recetas add estrellas int;

drop table recetas;
DELIMITER //
CREATE PROCEDURE sp_AddReceta(
IN pnombre varchar(30), IN pautor varchar(30), IN pcantidadpersonas int, ptiempo int, pdificultad varchar(25), pingredientes text, ptips text, ppreparacion text, prutaimg text, prutaimgapoyo text, pidUser smallint unsigned, pestrellas int
)
BEGIN
INSERT INTO recetas (nombre, autor, cantidadpersonas, tiempo, dificultad, ingredientes, tips, preparacion, rutaimg, rutaimgapoyo, idUser, estrellas)
VALUES (pnombre, pautor, pcantidadpersonas, ptiempo, pdificultad, pingredientes, ptips, ppreparacion, prutaimg, prutaimgapoyo, pidUser, pestrellas);
END //
DELIMITER ;

select * from recetas;