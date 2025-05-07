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
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recetas`
--

LOCK TABLES `recetas` WRITE;
/*!40000 ALTER TABLE `recetas` DISABLE KEYS */;
INSERT INTO `recetas` VALUES (8,'Chilaquiles','El Mismisimo',4,15,'Intermedio','24 tortillas de maíz dejadas secar al aire durante la noche\r\nAceite vegetal\r\n\r\n4 chiles guajillos\r\n1 tomate ciruela grande (Roma)\r\n4 dientes de ajo\r\n1/4 cucharadita de comino molido\r\n1 cubito de caldo de pollo, triturado\r\nSal, al gusto\r\n\r\n2 tazas de pechuga de pollo cocida desmenuzada\r\n1 taza de cebolla blanca finamente picada\r\n1 taza de Crema Mexicana (7 oz) Old El Paso™\r\n1 taza de queso mexicano desmoronado','Ponga atencion','1 Corta las tortillas en triángulos, extiéndelas en una bandeja para que se sequen unos minutos más mientras preparas el aceite de tu freidora. Fríe los triángulos de tortilla en una sartén o freidora hasta que estén dorados. Usa toallas de papel para eliminar el exceso de grasa y ponlas en un recipiente.\r\n\r\n2 Para preparar la salsa roja, agrega 2 tazas de agua y todos los ingredientes para la salsa de chile en una cacerola mediana. Lleva a ebullición; reduce el fuego y cocine a fuego lento hasta que el tomate esté suave y los chiles tiernos, aproximadamente 8 minutos. Retira los chiles, el tomate y el ajo y ponlos en la licuadora o procesadora de alimentos. Agrega 1 taza del líquido de cocción y procesa hasta que quede suave. Cola a través de un colador de malla fina en un bol. Sazona con sal. La salsa debe estar rica y picante.\r\n\r\n3 Para preparar los chilaquiles, coloca una capa de totopos fritos en un plato para servir y agrega el pollo y la cebolla encima. Vierte la salsa roja picante encima y termina con la crema mexicana y el queso desmenuzado ecima. Los chilaquiles se deben servir inmediatamente para mantener los totopos lo más crujientes posible.','../../static/uploads/1493.jpeg','../../static/uploads/1493apoyo.jpg',3,14,3),(9,'Camotes enmielados','Doña Camote',4,30,'Facil','1 1/2 kilo camote\r\n4 piloncillos\r\n1/2 vara de canela\r\n2 clavos de olor\r\n1 taza agua','Cuida que no se le acabe el agua a los camotes','1 Lavamos y pelamos nuestros camotes.\r\n\r\n2 Ponemos nuestra cazuela con los camotes, el agua, el piloncillo la media vara de canela y los clavos de olor.\r\n\r\n3 Dejamos así hasta que se ablanden los camotes a fuego medio.\r\n\r\n4 Una vez que están retiramos del fuego y nos los servimos, a mí me encantan con 1 vaso de leche de vaca recién hervida.','../../static/uploads/8493.jpg','../../static/uploads/8493apoyo.jpg',3,14,3),(14,'Reprobados al mojo de ajo','Carlos',4,60,'Dificil','4 Alumnos\r\n1 Proyecto','Estudien','Preguntales lo que menos esperan','../../static/uploads/6792.jpg','../../static/uploads/6792apoyo.jpg',2,0,0);
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

-- Dump completed on 2025-05-06 19:19:05
