CREATE DATABASE  IF NOT EXISTS `ssis_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `ssis_db`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: ssis_db
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `courses`
--

DROP TABLE IF EXISTS `courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `courses` (
  `Course Code` varchar(8) NOT NULL,
  `Course` varchar(50) NOT NULL,
  PRIMARY KEY (`Course Code`),
  UNIQUE KEY `Course` (`Course`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courses`
--

LOCK TABLES `courses` WRITE;
/*!40000 ALTER TABLE `courses` DISABLE KEYS */;
INSERT INTO `courses` VALUES ('BAP','BA in Psycho'),('BSCE','BS in Civil Engineering'),('BSCA','BS in Computer Application'),('BSCS','BS in Computer Science'),('BSEE','BS in Electrical Eng'),('BSIS','BS in Info System'),('BSIT','BS in Info Tech'),('BSME','BS in Mech Eng'),('BSP','BS in Pysch'),('BSST','BS in Stat'),('bfdb','fbdbbfdb'),('gggg','gggg'),('fdhh','hgdrg'),('jjj','jjjj'),('lllll','lllll');
/*!40000 ALTER TABLE `courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_info`
--

DROP TABLE IF EXISTS `student_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_info` (
  `Student ID` varchar(10) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Gender` enum('Male','Female','Non-binary','Transgender','Prefer not to say','Not listed') NOT NULL,
  `Year Level` int NOT NULL,
  `Course Code` varchar(8) NOT NULL,
  PRIMARY KEY (`Student ID`),
  KEY `Course Code_idx` (`Course Code`),
  CONSTRAINT `Course Code` FOREIGN KEY (`Course Code`) REFERENCES `courses` (`Course Code`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_info`
--

LOCK TABLES `student_info` WRITE;
/*!40000 ALTER TABLE `student_info` DISABLE KEYS */;
INSERT INTO `student_info` VALUES ('2019-0545','Rey','Not listed',4,'BSME'),('2020-0765','Marie','Non-binary',5,'BSIT'),('2021-0036','Romeo','Male',2,'BSCS'),('2021-0321','Juliet','Prefer not to say',3,'BSCE'),('2021-0654','John Cena','Male',1,'BSCA'),('2021-1265','Joanna','Female',2,'BSCS'),('2021-1812','Elias','Transgender',4,'BSCS'),('2021-2362','Rhea','Female',2,'BSCS'),('dsad','dsad','Male',1,'BSCA'),('rhea','2021-2362','Female',5,'BAP');
/*!40000 ALTER TABLE `student_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-17  1:29:29
