use tiendarecetitas;

DELIMITER //
CREATE PROCEDURE sp_verifyIdentity(IN pUsername VARCHAR(20), IN pPlainTextPassword VARCHAR(20))
BEGIN
DECLARE storedPassword VARCHAR(255);
SELECT password INTO storedPassword FROM users
WHERE username = pUsername COLLATE utf8mb4_unicode_ci;
IF storedPassword IS NOT NULL AND storedPassword = SHA2(pPlainTextPassword, 256) THEN
SELECT id, username, storedPassword, fullname, usertype FROM users
WHERE username = pUserName COLLATE utf8mb4_unicode_ci;
ELSE
SELECT NULL;
END IF;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_AddUser(IN pUserName VARCHAR(20), IN pPassword VARCHAR(102), IN pFullName
VARCHAR(50), in pUserType tinyint)
BEGIN
DECLARE hashedPassword VARCHAR(255);
SET hashedPassword = SHA2(pPassword, 256); -- Utiliza SHA-256 para hashear la contraseña.
INSERT INTO users (username, password, fullname, usertype )
VALUES (pUserName, hashedPassword, pFullName, pUserType);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE sp_AddReceta(
IN pnombre varchar(30), IN pautor varchar(30), IN pcantidadpersonas int, ptiempo int, pdificultad varchar(25), pingredientes text, ptips text, ppreparacion text, prutaimg text, prutaimgapoyo text, pidUser smallint unsigned, pestrellas int
)
BEGIN
INSERT INTO recetas (nombre, autor, cantidadpersonas, tiempo, dificultad, ingredientes, tips, preparacion, rutaimg, rutaimgapoyo, idUser, estrellas)
VALUES (pnombre, pautor, pcantidadpersonas, ptiempo, pdificultad, pingredientes, ptips, ppreparacion, prutaimg, prutaimgapoyo, pidUser, pestrellas);
END //
DELIMITER ;