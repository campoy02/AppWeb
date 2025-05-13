-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: tiendarecetitas
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `recetas`
--

DROP TABLE IF EXISTS `recetas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recetas` (
  `idReceta` smallint unsigned NOT NULL AUTO_INCREMENT,
  `nombre` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `autor` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `cantidadpersonas` int DEFAULT NULL,
  `tiempo` int DEFAULT NULL,
  `dificultad` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `ingredientes` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `tips` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `preparacion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `rutaimg` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `rutaimgapoyo` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `idUser` smallint unsigned NOT NULL,
  `estrellas` int DEFAULT NULL,
  `votos_totales` int DEFAULT '0',
  PRIMARY KEY (`idReceta`),
  KEY `idUser` (`idUser`),
  CONSTRAINT `recetas_ibfk_1` FOREIGN KEY (`idUser`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recetas`
--

LOCK TABLES `recetas` WRITE;
/*!40000 ALTER TABLE `recetas` DISABLE KEYS */;
INSERT INTO `recetas` VALUES (8,'Chilaquiles','El Mismisimo',4,15,'Intermedio','24 tortillas de maíz dejadas secar al aire durante la noche\r\nAceite vegetal\r\n\r\n4 chiles guajillos\r\n1 tomate ciruela grande (Roma)\r\n4 dientes de ajo\r\n1/4 cucharadita de comino molido\r\n1 cubito de caldo de pollo, triturado\r\nSal, al gusto\r\n\r\n2 tazas de pechuga de pollo cocida desmenuzada\r\n1 taza de cebolla blanca finamente picada\r\n1 taza de Crema Mexicana (7 oz) Old El Paso™\r\n1 taza de queso mexicano desmoronado','Ponga atencion','1 Corta las tortillas en triángulos, extiéndelas en una bandeja para que se sequen unos minutos más mientras preparas el aceite de tu freidora. Fríe los triángulos de tortilla en una sartén o freidora hasta que estén dorados. Usa toallas de papel para eliminar el exceso de grasa y ponlas en un recipiente.\r\n\r\n2 Para preparar la salsa roja, agrega 2 tazas de agua y todos los ingredientes para la salsa de chile en una cacerola mediana. Lleva a ebullición; reduce el fuego y cocine a fuego lento hasta que el tomate esté suave y los chiles tiernos, aproximadamente 8 minutos. Retira los chiles, el tomate y el ajo y ponlos en la licuadora o procesadora de alimentos. Agrega 1 taza del líquido de cocción y procesa hasta que quede suave. Cola a través de un colador de malla fina en un bol. Sazona con sal. La salsa debe estar rica y picante.\r\n\r\n3 Para preparar los chilaquiles, coloca una capa de totopos fritos en un plato para servir y agrega el pollo y la cebolla encima. Vierte la salsa roja picante encima y termina con la crema mexicana y el queso desmenuzado ecima. Los chilaquiles se deben servir inmediatamente para mantener los totopos lo más crujientes posible.','../../static/uploads/1493.jpeg','../../static/uploads/1493apoyo.jpg',3,14,3),(16,'Imagen de un caballo','Fan de los cabalalos',1,1,'Facil','Esto no es comida \r\n','Es una foto de un caballo\r\n','Mirar la foto','../../static/uploads/6433.jpg','../../static/uploads/6433apoyo.jpg',3,15,5),(17,'Prueba 120525','Ary',2,2,'Facil','2 imagenes\r\ntexto','Usa imagenes referentes a la receta','Escribe tu preparacion aqui','../../static/uploads/7062.jpg','../../static/uploads/7062apoyo.jpg',2,9,2),(18,'Chili de preparación rápida','Ary',4,120,'Intermedio','    1/2 libra de carne molida de res 90% magra\r\n    1 lata de frijoles rojos bajos en sodio (15.5 onzas, con todo y caldo)\r\n    1 taza de salsa de tomate baja en sodio\r\n    1 cucharada de cebolla (instantánea, finamente picada)\r\n    1 1/2 cucharadas de chile (ají) en polvo\r\n','Lávese las manos con agua y jabón.','Cueza bien la carne en una sartén hasta dorar (a una temperatura interna de 160 ºF). No la deje a medio cocer. Lávese bien las manos y cualquier superficie que haya entrado en contacto con la carne cruda.\r\nEscurra la grasa en un recipiente.\r\nIntegre los frijoles rojos con todo y caldo, la salsa de tomate, la cebolla y el chile (ají) en polvo.\r\nPonga a hervir. Reduzca la llama, tape y cocine a fuego lento durante 10 minutos.\r\nRefrigere o congele lo que sobre no más de 2 horas después de preparar. Consuma las sobras refrigeradas antes de 4 días.','../../static/uploads/892.jpg','../../static/uploads/892apoyo.jpg',2,9,2),(19,'Receta de pan de ajo: no lo harás de otra manera','Liliana Fuchs',5,15,'Facil','\r\n    Una barra de pan baguette\r\n    50 gramos de mantequilla\r\n    2 ajos pequeños\r\n    Media cucharadita de ajo en polvo\r\n    Un poquito de pimienta molida\r\n    Perejil fresco\r\n','Le podéis poner un poquito de queso parmesano por encima de la mantequilla de ajo y a la hora de de meter al horno se va a quedar gratinado y va a quedar genial.\r\n','  Comenzaremos triturando los ajos junto con la mantequilla, el perejil fresco y el ajo en polvo. Salpimentamos.\r\n    Cortamos rebanadas como de 2 centímetros de pan baguette.\r\n    Untamos la mantequilla de ajo en la rebanada de pan y las introducimos al horno a 180 grados hasta que se tueste el pan. Así de sencillo.\r\n','../../static/uploads/6456.jpg','../../static/uploads/6456apoyo.jpg',6,5,1);
/*!40000 ALTER TABLE `recetas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-13 10:44:11
