-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: 10.73.100.101    Database: vansplanning
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `agents`
--

DROP TABLE IF EXISTS `agents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `agents` (
  `id` int NOT NULL AUTO_INCREMENT,
  `matrr` varchar(50) NOT NULL,
  `firstName` varchar(50) DEFAULT NULL,
  `LastName` varchar(50) DEFAULT NULL,
  `CIN` varchar(50) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `grp` int DEFAULT NULL,
  `zone` varchar(45) DEFAULT NULL,
  `street` varchar(45) DEFAULT NULL,
  `pic` text,
  PRIMARY KEY (`id`),
  KEY `grp` (`grp`),
  CONSTRAINT `agents_ibfk_1` FOREIGN KEY (`grp`) REFERENCES `grps` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agents`
--

LOCK TABLES `agents` WRITE;
/*!40000 ALTER TABLE `agents` DISABLE KEYS */;
INSERT INTO `agents` VALUES (2,'GOT151','yassine','baghdadi','ZG141585','oujda doha',3,'Sidi Driss EL Kadi','HAY ALBOUSTANE','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/YassineBaghdadiHackathon.jpg?alt=media&token=e230e05d-8b62-4d8b-8b17-56d929d19d54'),(5,'MRT490','TAHA YASSINE','BOUCHAMA','F420185','HAY EL MOHAMMADI LOT EL OUAHDA',5,NULL,NULL,'https://images.pexels.com/photos/5032023/pexels-photo-5032023.jpeg'),(6,'IKI964','OUAFAE','ABDOUSSI','F596060','HAY MOHAMMADI RUE 202',6,NULL,NULL,'https://images.pexels.com/photos/6962008/pexels-photo-6962008.jpeg'),(7,'EOJ256','NOUHAYLA ','AHMIAN','f715988','565 BD AL MASSIRA NADOR',5,NULL,NULL,'https://images.pexels.com/photos/2078265/pexels-photo-2078265.jpeg'),(8,'OFN604','NADIA','AZZIMANI','F530757','RTE EL AOUNIA LOT TALHAOUI',6,NULL,NULL,'https://images.pexels.com/photos/6962008/pexels-photo-6962008.jpeg'),(9,'TKD479','EL MAHDI','NENAZZA','F447092','LOT JAWHARAT SAFAE BLOC 27',6,NULL,NULL,'https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg'),(10,'PEE743','LAMYAE','BOUALI','F646360','BD HASSAN2 LOT MOUKIF',6,NULL,NULL,'https://images.pexels.com/photos/7148620/pexels-photo-7148620.jpeg'),(11,'FCT154','ABOU SOUFIANE ','DRIOUCH','F540126','DHAR LAMHALLA LOT HAMDI',6,NULL,NULL,'https://images.pexels.com/photos/6962024/pexels-photo-6962024.jpeg'),(12,'ADK194','MERYEM','EL ARABI','F581299','HAY EL WAHDA RTE TAZA ',6,NULL,NULL,'https://images.pexels.com/photos/7013617/pexels-photo-7013617.jpeg'),(13,'BDG981','SOUFIANE ','JAZOULI','F427934','HAY MED BEN EL MADANI LOT KADA',1,NULL,NULL,'https://images.pexels.com/photos/6214874/pexels-photo-6214874.jpeg'),(14,'JDM290','YOUSRA ','KASMI','Z584254','28BLOC 3 HAY EL ANDALOUS',6,NULL,NULL,'https://images.pexels.com/photos/7654096/pexels-photo-7654096.jpeg'),(15,'ITD876','SAHAR','KIRRA','F539890','BD MOHAMED7 LOT BOUSTANE',6,NULL,NULL,'https://images.pexels.com/photos/6214874/pexels-photo-6214874.jpeg'),(16,'ESD437','NAZHA ','MBAREK','F570533','HAY TAKADOUM2 BLOC D',6,NULL,NULL,'https://images.pexels.com/photos/7013617/pexels-photo-7013617.jpeg'),(17,'GGM865','MANAL','SELMI','FA188214','RUE EL OUMAOUIYINE HAY EL QODS',5,NULL,NULL,'https://images.pexels.com/photos/2078265/pexels-photo-2078265.jpeg'),(18,'KHR455','ILYASS','HAMRI','F577257','HAY ZAITOUNE LMOT BELHOUCINE ',1,NULL,NULL,'https://images.pexels.com/photos/220453/pexels-photo-220453.jpeg'),(19,'FDB878','RIME','ZAHIRI','F652030','HAY SAADA RUE AL BATRIQ',1,NULL,NULL,'https://images.pexels.com/photos/7013617/pexels-photo-7013617.jpeg'),(20,'MPF174','test1','forhjghjg','asdasd','asdasd',1,'Oued Nachef Sidi Maafa','HAY HAKKOU','https://images.pexels.com/photos/6195663/pexels-photo-6195663.jpeg'),(21,'EMB411','ITgfgf','test','asad','asdasd',3,'Oued Nachef Sidi Maafa','LOT IRIS','https://images.pexels.com/photos/6962024/pexels-photo-6962024.jpeg'),(22,'KIP675','itt t','asdasd','asdasd','asdasd',6,NULL,NULL,'https://images.pexels.com/photos/4924538/pexels-photo-4924538.jpeg'),(23,'CHE267','test','thehg','Xh4542','asdasdasfdfsgfg',2,'Oued Nachef Sidi Maafa','LOTS SALAMA','https://images.pexels.com/photos/6962024/pexels-photo-6962024.jpeg'),(24,'NHF724','yassine for test','baghdadi it','asdasdasdasd','jhashdajshds',2,'Oued Nachef Sidi Maafa','HAY ALMANAR RTE AHFIR','https://images.pexels.com/photos/7148620/pexels-photo-7148620.jpeg'),(25,'IBI937','yassine','baghdasd','adsjfhaskd','asdasddaf',12,'Oued Nachef Sidi Maafa','hay ALOUAHDA RTE TAZA','https://images.pexels.com/photos/5032023/pexels-photo-5032023.jpeg'),(26,'geg515','Anass','kadda','S544125','agdal',5,'Oued Nachef Sidi Maafa','hay ALOUAHDA RTE TAZA','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/adorable-donkey-isolated-on-white-260nw-366694535.jpg?alt=media&token=e230e05d-8b62-4d8b-8b17-56d929d19d54');
/*!40000 ALTER TABLE `agents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drivers`
--

DROP TABLE IF EXISTS `drivers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drivers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `firstName` varchar(50) DEFAULT NULL,
  `LastName` varchar(50) DEFAULT NULL,
  `username` varchar(45) NOT NULL,
  `pass` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drivers`
--

LOCK TABLES `drivers` WRITE;
/*!40000 ALTER TABLE `drivers` DISABLE KEYS */;
INSERT INTO `drivers` VALUES (1,'najib','driver','najib','1234'),(2,'said','ghazouani','said','12345');
/*!40000 ALTER TABLE `drivers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grps`
--

DROP TABLE IF EXISTS `grps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grps` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `shift` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grps`
--

LOCK TABLES `grps` WRITE;
/*!40000 ALTER TABLE `grps` DISABLE KEYS */;
INSERT INTO `grps` VALUES (1,'TDE','08-17'),(2,'qye','08-17'),(3,'SIC','14-23'),(4,'QSDIV','13-22'),(5,'Altima','13-22'),(6,'MyAssure','09-18'),(11,'New Grp','09-18'),(12,'interviews','08-17');
/*!40000 ALTER TABLE `grps` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `logsfile`
--

DROP TABLE IF EXISTS `logsfile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `logsfile` (
  `id` int NOT NULL,
  `user` varchar(45) DEFAULT NULL,
  `query` varchar(500) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `descr` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logsfile`
--

LOCK TABLES `logsfile` WRITE;
/*!40000 ALTER TABLE `logsfile` DISABLE KEYS */;
/*!40000 ALTER TABLE `logsfile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trips`
--

DROP TABLE IF EXISTS `trips`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trips` (
  `id` int NOT NULL AUTO_INCREMENT,
  `van` int DEFAULT NULL,
  `driver` int DEFAULT NULL,
  `datetime` varchar(50) DEFAULT NULL,
  `ttype` varchar(5) DEFAULT NULL,
  `starttime` varchar(45) DEFAULT NULL,
  `startloc` varchar(45) DEFAULT NULL,
  `stoptime` varchar(45) DEFAULT NULL,
  `stoploc` varchar(45) DEFAULT NULL,
  `counterkm` varchar(45) DEFAULT NULL,
  `tracking` longtext,
  PRIMARY KEY (`id`),
  KEY `van` (`van`),
  KEY `driver` (`driver`),
  CONSTRAINT `trips_ibfk_1` FOREIGN KEY (`van`) REFERENCES `vans` (`id`),
  CONSTRAINT `trips_ibfk_2` FOREIGN KEY (`driver`) REFERENCES `drivers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=148 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trips`
--

LOCK TABLES `trips` WRITE;
/*!40000 ALTER TABLE `trips` DISABLE KEYS */;
INSERT INTO `trips` VALUES (1,1,1,'2021-08-23 08:45:22','IN','None','None','None','None','0 ','{}'),(3,1,1,'2021-08-25 14:00:00','IN','None','None','None','None','0 ','{}'),(5,1,1,'2021-08-25 23:00:00','OUT','None','None','None','None','0 ','{}'),(6,1,1,'2021-08-26 13:00:00','IN','None','None','None','None','0 ','{}'),(7,1,1,'2021-08-26 14:00:00','IN','None','None','None','None','0 ','{}'),(8,1,1,'2021-08-26 22:00:00','OUT','None','None','None','None','0 ','{}'),(9,1,1,'2021-08-26 23:00:00','OUT','None','None','None','None','0 ','{}'),(10,1,1,'2021-08-26 09:00:00','IN','None','None','None','None','0 ','{}'),(11,1,1,'2021-08-26 18:00:00','OUT','None','None','None','None','0 ','{}'),(12,1,1,'2021-08-26 08:00:00','IN','None','None','None','None','0 ','{}'),(13,1,1,'2021-08-26 17:00:00','OUT','None','None','None','None','0 ','{}'),(14,1,1,'2021-08-25 08:00:00','IN','12:45:05','34.7700818,-1.9366856','13:16:00','34.719319, -1.921540','14','{\'12:45:06\': \'34.768952, -1.937740\', \'12:45:07\': \'34.767780, -1.937333\', \'12:45:08\': \'34.767357, -1.938652\', \'12:45:09\': \'34.766810, -1.940433\', \'12:45:10\': \'34.766696, -1.940895\', \'12:45:11\': \'34.765532, -1.940272\', \'12:45:12\': \'34.761050, -1.938261\', \'12:45:13\': \'34.758782, -1.937411\', \'12:45:14\': \'34.755753, -1.935909\', \'12:45:15\': \'34.751439, -1.933937\', \'12:45:16\': \'34.746839, -1.931858\', \'12:45:17\': \'34.743847, -1.930856\', \'12:45:18\': \'34.740742, -1.930143\', \'12:45:19\': \'34.737837, -1.929476\', \'12:45:20\': \'34.737276, -1.929370\', \'12:45:21\': \'34.735730, -1.928945\', \'12:45:22\': \'34.731565, -1.926623\', \'12:45:23\': \'34.729408, -1.925015\', \'12:45:24\': \'34.726016, -1.922587\', \'12:45:25\': \'34.723185, -1.921950\', \'12:45:26\': \'34.719319, -1.921540\'}'),(15,1,1,'2021-08-25 09:00:00','IN','None','None','None','None','0 ','{}'),(16,1,1,'2021-08-25 17:00:00','OUT','None','None','None','None','0 ','{}'),(17,1,1,'2021-08-25 18:00:00','OUT','None','None','None','None','0 ','{}'),(18,1,1,'2021-08-27 08:00:00','IN','None','None','None','None','0 ','{}'),(19,1,1,'2021-08-27 09:00:00','IN','None','None','None','None','0 ','{}'),(20,1,1,'2021-08-27 13:00:00','IN','None','None','None','None','0 ',NULL),(21,1,1,'2021-08-27 14:00:00','IN','None','None','None','None','0 ',NULL),(22,1,1,'2021-08-27 17:00:00','OUT','None','None','None','None','0 ',NULL),(23,1,1,'2021-08-27 18:00:00','OUT','None','None','None','None','0 ',NULL),(24,1,1,'2021-08-27 22:00:00','OUT','None','None','None','None','0 ',NULL),(25,1,1,'2021-08-27 23:00:00','OUT','None','None','None','None','0 ',NULL),(26,1,1,'2021-08-30 08:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(27,1,1,'2021-08-30 09:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(28,1,1,'2021-08-30 13:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(29,1,1,'2021-08-30 14:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(30,1,1,'2021-08-30 17:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(31,1,1,'2021-08-30 18:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(32,1,1,'2021-08-30 22:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(33,1,1,'2021-08-30 23:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(34,1,1,'2021-08-31 08:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(35,1,1,'2021-08-31 09:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(36,1,1,'2021-08-31 13:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(37,1,1,'2021-08-31 14:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(38,1,1,'2021-08-31 17:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(39,1,1,'2021-08-31 18:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(40,1,1,'2021-08-31 22:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(41,1,1,'2021-08-31 23:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(42,1,1,'2021-09-01 08:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(43,1,1,'2021-09-01 09:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(44,1,1,'2021-09-01 13:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(45,1,1,'2021-09-01 14:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(46,1,1,'2021-09-01 17:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(47,1,1,'2021-09-01 18:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(48,1,1,'2021-09-01 22:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(49,1,1,'2021-09-01 23:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(50,1,1,'2021-09-02 08:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(51,1,1,'2021-09-02 09:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(52,1,1,'2021-09-02 13:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(54,1,1,'2021-09-02 17:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(55,1,1,'2021-09-02 18:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(56,1,1,'2021-09-02 22:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(58,1,1,'2021-09-02 14:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(59,1,1,'2021-09-02 23:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(60,1,1,'2021-09-03 08:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(61,1,1,'2021-09-03 09:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(62,1,1,'2021-09-03 13:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(63,1,1,'2021-09-03 14:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(64,1,1,'2021-09-03 17:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(65,1,1,'2021-09-03 18:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(66,1,1,'2021-09-03 22:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(67,1,1,'2021-09-03 23:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(68,1,1,'2021-09-06 08:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(69,1,1,'2021-09-06 09:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(70,1,1,'2021-09-06 13:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(71,1,1,'2021-09-06 14:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(72,1,1,'2021-09-06 17:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(73,1,1,'2021-09-06 18:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(74,1,1,'2021-09-06 22:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(75,1,1,'2021-09-06 23:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(77,1,1,'2021-09-04 11:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(78,1,1,'2021-09-07 08:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(79,1,1,'2021-09-07 09:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(80,1,1,'2021-09-07 13:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(81,1,1,'2021-09-07 14:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(82,1,1,'2021-09-07 17:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(83,1,1,'2021-09-07 18:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(84,1,1,'2021-09-07 22:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(85,1,1,'2021-09-07 23:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(86,1,2,'2021-09-06 15:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(87,1,1,'2021-09-08 08:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(88,1,1,'2021-09-08 09:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(89,1,1,'2021-09-08 13:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(90,1,1,'2021-09-08 14:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(91,1,1,'2021-09-08 17:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(92,1,1,'2021-09-08 18:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(93,1,1,'2021-09-08 22:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(94,1,1,'2021-09-08 23:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(98,1,1,'2021-09-09 09:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(99,1,1,'2021-09-09 13:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(100,1,1,'2021-09-09 14:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(101,1,1,'2021-09-09 17:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(102,1,1,'2021-09-09 18:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(103,1,1,'2021-09-09 22:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(104,1,1,'2021-09-09 23:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(108,1,1,'2021-09-09 08:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(114,1,1,'2021-09-13 08:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(115,1,1,'2021-09-13 09:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(116,1,1,'2021-09-13 13:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(117,1,1,'2021-09-13 14:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(118,1,1,'2021-09-13 18:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(119,1,1,'2021-09-13 22:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(120,1,1,'2021-09-13 23:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(121,1,1,'2021-09-14 08:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(122,1,1,'2021-09-14 09:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(123,1,1,'2021-09-14 13:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(124,1,1,'2021-09-14 14:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(125,1,1,'2021-09-14 17:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(126,1,1,'2021-09-14 18:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(127,1,1,'2021-09-14 22:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(128,1,1,'2021-09-14 23:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(132,1,1,'2021-09-17 18:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(133,1,2,'2021-09-24 13:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(134,2,2,'2021-09-29 13:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(135,2,2,'2021-09-21 14:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(136,1,1,'2021-09-15 17:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(137,1,2,'2022-09-15 17:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(138,2,2,'2021-10-05 17:00:00','OUT','None','None','None','None','0 ','{}'),(139,2,1,'2021-10-15 08:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(142,1,1,'2021-11-01 23:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(144,1,1,'2021-10-03 13:00:00','IN','None','None','None','None','0 ','{}'),(145,1,1,'2021-10-04 14:00:00','IN','None','None','None','None','0 ','{}'),(146,1,1,'2021-10-05 13:00:00','IN','None','None','None','None','0 ','{}'),(147,1,2,'2021-11-18 13:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `trips` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trips_history`
--

DROP TABLE IF EXISTS `trips_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trips_history` (
  `id` int NOT NULL AUTO_INCREMENT,
  `trip` int DEFAULT NULL,
  `agent` int DEFAULT NULL,
  `presence` varchar(50) DEFAULT NULL,
  `picktime` varchar(50) DEFAULT NULL,
  `pickloc` varchar(50) DEFAULT NULL,
  `droptime` varchar(50) DEFAULT NULL,
  `droploc` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `trip` (`trip`),
  KEY `agent` (`agent`),
  CONSTRAINT `trips_history_ibfk_1` FOREIGN KEY (`trip`) REFERENCES `trips` (`id`),
  CONSTRAINT `trips_history_ibfk_2` FOREIGN KEY (`agent`) REFERENCES `agents` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=857 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trips_history`
--

LOCK TABLES `trips_history` WRITE;
/*!40000 ALTER TABLE `trips_history` DISABLE KEYS */;
INSERT INTO `trips_history` VALUES (5,1,2,'','','','',''),(8,3,2,'','','','',''),(11,5,2,'','','','',''),(14,6,5,'','','','',''),(15,7,2,'','','','',''),(19,9,2,'','','','',''),(20,10,6,'','','','',''),(21,11,6,'','','','',''),(24,12,19,'','','','',''),(27,13,19,'','','','',''),(28,14,13,'','','','',''),(29,14,18,'','','','',''),(30,14,19,'','','','',''),(31,15,6,'','','','',''),(32,15,8,'','','','',''),(33,15,9,'','','','',''),(34,15,10,'','','','',''),(35,15,11,'','','','',''),(36,15,12,'','','','',''),(37,15,14,'','','','',''),(38,15,15,'','','','',''),(39,15,16,'','','','',''),(40,16,13,'','','','',''),(41,16,18,'','','','',''),(42,16,19,'','','','',''),(43,17,6,'','','','',''),(44,17,8,'','','','',''),(45,17,9,'','','','',''),(46,17,10,'','','','',''),(47,17,11,'','','','',''),(48,17,12,'','','','',''),(49,17,14,'','','','',''),(50,17,15,'','','','',''),(51,17,16,'','','','',''),(52,18,13,'','','','',''),(53,18,18,'','','','',''),(54,18,19,'','','','',''),(55,19,6,'','','','',''),(56,19,8,'','','','',''),(57,19,9,'','','','',''),(58,19,10,'','','','',''),(59,19,11,'','','','',''),(60,19,12,'','','','',''),(61,19,14,'','','','',''),(62,19,15,'','','','',''),(63,19,16,'','','','',''),(64,20,5,'','','','',''),(65,20,7,'','','','',''),(66,20,17,'','','','',''),(67,21,2,'','','','',''),(68,22,13,'','','','',''),(69,22,18,'','','','',''),(70,22,19,'','','','',''),(71,23,6,'','','','',''),(72,23,8,'','','','',''),(73,23,9,'','','','',''),(74,23,10,'','','','',''),(75,23,11,'','','','',''),(76,23,12,'','','','',''),(77,23,14,'','','','',''),(78,23,15,'','','','',''),(79,23,16,'','','','',''),(80,24,5,'','','','',''),(81,24,7,'','','','',''),(82,24,17,'','','','',''),(83,25,2,'','','','',''),(85,12,7,'','','','',''),(86,12,5,'','','','',''),(87,12,17,'','','','',''),(88,10,8,'','','','',''),(89,10,11,'','','','',''),(93,8,19,'','','','',''),(95,8,7,'','','','',''),(96,8,12,'','','','',''),(97,8,14,'','','','',''),(98,8,16,'','','','',''),(100,8,2,'','','','',''),(101,26,13,'','','','',''),(102,26,18,'','','','',''),(103,26,19,'','','','',''),(104,27,6,'','','','',''),(105,27,8,'','','','',''),(106,27,9,'','','','',''),(107,27,10,'','','','',''),(108,27,11,'','','','',''),(109,27,12,'','','','',''),(110,27,14,'','','','',''),(111,27,15,'','','','',''),(112,27,16,'','','','',''),(113,28,5,'','','','',''),(114,28,7,'','','','',''),(115,28,17,'','','','',''),(116,29,2,'','','','',''),(117,30,13,'','','','',''),(118,30,18,'','','','',''),(119,30,19,'','','','',''),(120,31,6,'','','','',''),(121,31,8,'','','','',''),(122,31,9,'','','','',''),(123,31,10,'','','','',''),(124,31,11,'','','','',''),(125,31,12,'','','','',''),(126,31,14,'','','','',''),(127,31,15,'','','','',''),(128,31,16,'','','','',''),(129,32,5,'','','','',''),(131,32,17,'','','','',''),(132,33,2,'','','','',''),(133,34,13,'','','','',''),(134,34,18,'','','','',''),(135,34,19,'','','','',''),(136,35,6,'','','','',''),(137,35,8,'','','','',''),(138,35,9,'','','','',''),(139,35,10,'','','','',''),(140,35,11,'','','','',''),(141,35,12,'','','','',''),(142,35,14,'','','','',''),(143,35,15,'','','','',''),(144,35,16,'','','','',''),(145,36,5,'','','','',''),(146,36,7,'','','','',''),(147,36,17,'','','','',''),(148,37,2,'','','','',''),(149,38,13,'','','','',''),(150,38,18,'','','','',''),(151,38,19,'','','','',''),(152,39,6,'','','','',''),(153,39,8,'','','','',''),(154,39,9,'','','','',''),(155,39,10,'','','','',''),(156,39,11,'','','','',''),(157,39,12,'','','','',''),(158,39,14,'','','','',''),(159,39,15,'','','','',''),(160,39,16,'','','','',''),(161,40,5,'','','','',''),(162,40,7,'','','','',''),(163,40,17,'','','','',''),(164,41,2,'','','','',''),(165,27,5,'','','','',''),(166,27,2,'','','','',''),(167,27,19,'','','','',''),(168,27,13,'','','','',''),(169,27,7,'','','','',''),(170,27,17,'','','','',''),(171,27,18,'','','','',''),(172,27,20,'','','','',''),(173,27,21,'','','','',''),(174,42,13,'','','','',''),(175,42,18,'','','','',''),(176,42,19,'','','','',''),(177,42,20,'','','','',''),(180,43,9,'','','','',''),(183,43,12,'','','','',''),(184,43,14,'','','','',''),(185,43,15,'','','','',''),(186,43,16,'','','','',''),(187,43,22,'','','','',''),(188,44,5,'','','','',''),(189,44,7,'','','','',''),(190,44,17,'','','','',''),(191,45,2,'','','','',''),(192,45,21,'','','','',''),(193,46,13,'','','','',''),(194,46,18,'','','','',''),(195,46,19,'','','','',''),(197,47,6,'','','','',''),(198,47,8,'','','','',''),(199,47,9,'','','','',''),(200,47,10,'','','','',''),(201,47,11,'','','','',''),(202,47,12,'','','','',''),(203,47,14,'','','','',''),(204,47,15,'','','','',''),(205,47,16,'','','','',''),(206,47,22,'','','','',''),(207,48,5,'','','','',''),(208,48,7,'','','','',''),(209,48,17,'','','','',''),(210,49,2,'','','','',''),(211,49,21,'','','','',''),(212,43,5,'','','','',''),(213,43,7,'','','','',''),(214,43,18,'','','','',''),(215,43,21,'','','','',''),(216,43,17,'','','','',''),(217,43,19,'','','','',''),(218,43,2,'','','','',''),(219,43,13,'','','','',''),(220,43,8,'','','','',''),(221,43,11,'','','','',''),(222,43,10,'','','','',''),(223,43,6,'','','','',''),(224,41,5,'','','','',''),(225,50,13,'','','','',''),(226,50,18,'','','','',''),(227,50,19,'','','','',''),(228,50,20,'','','','',''),(229,51,6,'','','','',''),(230,51,8,'','','','',''),(231,51,9,'','','','',''),(232,51,10,'','','','',''),(233,51,11,'','','','',''),(234,51,12,'','','','',''),(235,51,14,'','','','',''),(236,51,15,'','','','',''),(237,51,16,'','','','',''),(238,51,22,'','','','',''),(239,52,5,'','','','',''),(240,52,7,'','','','',''),(241,52,17,'','','','',''),(244,54,13,'','','','',''),(245,54,18,'','','','',''),(246,54,19,'','','','',''),(247,54,20,'','','','',''),(248,55,6,'','','','',''),(249,55,8,'','','','',''),(250,55,9,'','','','',''),(251,55,10,'','','','',''),(252,55,11,'','','','',''),(253,55,12,'','','','',''),(254,55,14,'','','','',''),(255,55,15,'','','','',''),(256,55,16,'','','','',''),(257,55,22,'','','','',''),(258,56,5,'','','','',''),(259,56,7,'','','','',''),(260,56,17,'','','','',''),(263,58,2,'','','','',''),(264,58,21,'','','','',''),(265,59,2,'','','','',''),(266,59,21,'','','','',''),(267,60,13,'','','','',''),(268,60,18,'','','','',''),(269,60,19,'','','','',''),(270,60,20,'','','','',''),(271,61,6,'','','','',''),(272,61,8,'','','','',''),(273,61,9,'','','','',''),(274,61,10,'','','','',''),(275,61,11,'','','','',''),(276,61,12,'','','','',''),(277,61,14,'','','','',''),(278,61,15,'','','','',''),(279,61,16,'','','','',''),(280,61,22,'','','','',''),(281,62,5,'','','','',''),(282,62,7,'','','','',''),(283,62,17,'','','','',''),(284,63,2,'','','','',''),(285,63,21,'','','','',''),(286,64,13,'','','','',''),(287,64,18,'','','','',''),(288,64,19,'','','','',''),(289,64,20,'','','','',''),(290,65,6,'','','','',''),(291,65,8,'','','','',''),(292,65,9,'','','','',''),(293,65,10,'','','','',''),(294,65,11,'','','','',''),(295,65,12,'','','','',''),(296,65,14,'','','','',''),(297,65,15,'','','','',''),(298,65,16,'','','','',''),(299,65,22,'','','','',''),(300,66,5,'','','','',''),(301,66,7,'','','','',''),(302,66,17,'','','','',''),(303,67,2,'','','','',''),(304,67,21,'','','','',''),(305,68,13,'','','','',''),(306,68,18,'','','','',''),(307,68,19,'','','','',''),(308,68,20,'','','','',''),(309,69,6,'','','','',''),(310,69,8,'','','','',''),(311,69,9,'','','','',''),(312,69,10,'','','','',''),(313,69,11,'','','','',''),(314,69,12,'','','','',''),(315,69,14,'','','','',''),(316,69,15,'','','','',''),(317,69,16,'','','','',''),(318,69,22,'','','','',''),(319,70,5,'','','','',''),(320,70,7,'','','','',''),(321,70,17,'','','','',''),(322,71,2,'','','','',''),(323,71,21,'','','','',''),(324,72,13,'','','','',''),(325,72,18,'','','','',''),(326,72,19,'','','','',''),(327,72,20,'','','','',''),(328,73,6,'','','','',''),(329,73,8,'','','','',''),(330,73,9,'','','','',''),(331,73,10,'','','','',''),(332,73,11,'','','','',''),(333,73,12,'','','','',''),(334,73,14,'','','','',''),(335,73,15,'','','','',''),(336,73,16,'','','','',''),(337,73,22,'','','','',''),(338,74,5,'','','','',''),(339,74,7,'','','','',''),(340,74,17,'','','','',''),(341,75,2,'','','','',''),(342,75,21,'','','','',''),(343,77,5,'','','','',''),(344,77,8,'','','','',''),(345,77,12,'','','','',''),(346,77,14,'','','','',''),(347,77,15,'','','','',''),(348,77,17,'','','','',''),(349,77,16,'','','','',''),(350,77,9,'','','','',''),(351,77,6,'','','','',''),(352,78,13,'','','','',''),(353,78,18,'','','','',''),(354,78,19,'','','','',''),(355,78,20,'','','','',''),(356,79,6,'','','','',''),(357,79,8,'','','','',''),(358,79,9,'','','','',''),(359,79,10,'','','','',''),(360,79,11,'','','','',''),(361,79,12,'','','','',''),(362,79,14,'','','','',''),(363,79,15,'','','','',''),(364,79,16,'','','','',''),(365,79,22,'','','','',''),(366,80,5,'','','','',''),(367,80,7,'','','','',''),(368,80,17,'','','','',''),(369,81,2,'','','','',''),(370,81,21,'','','','',''),(371,82,13,'','','','',''),(373,82,19,'','','','',''),(374,82,20,'','','','',''),(375,83,6,'','','','',''),(376,83,8,'','','','',''),(377,83,9,'','','','',''),(378,83,10,'','','','',''),(379,83,11,'','','','',''),(380,83,12,'','','','',''),(381,83,14,'','','','',''),(382,83,15,'','','','',''),(383,83,16,'','','','',''),(384,83,22,'','','','',''),(385,84,5,'','','','',''),(386,84,7,'','','','',''),(387,84,17,'','','','',''),(388,85,2,'','','','',''),(389,85,21,'','','','',''),(390,86,6,'','','','',''),(391,86,7,'','','','',''),(392,86,12,'','','','',''),(393,86,8,'','','','',''),(394,68,2,'','','','',''),(395,68,9,'','','','',''),(396,87,13,'','','','',''),(397,87,18,'','','','',''),(398,87,19,'','','','',''),(399,87,20,'','','','',''),(400,88,6,'','','','',''),(401,88,8,'','','','',''),(402,88,9,'','','','',''),(403,88,10,'','','','',''),(404,88,11,'','','','',''),(405,88,12,'','','','',''),(406,88,14,'','','','',''),(407,88,15,'','','','',''),(408,88,16,'','','','',''),(409,88,22,'','','','',''),(410,89,5,'','','','',''),(411,89,7,'','','','',''),(412,89,17,'','','','',''),(413,90,2,'','','','',''),(414,90,21,'','','','',''),(415,91,13,'','','','',''),(416,91,18,'','','','',''),(417,91,19,'','','','',''),(418,91,20,'','','','',''),(419,92,6,'','','','',''),(420,92,8,'','','','',''),(421,92,9,'','','','',''),(422,92,10,'','','','',''),(423,92,11,'','','','',''),(424,92,12,'','','','',''),(425,92,14,'','','','',''),(426,92,15,'','','','',''),(427,92,16,'','','','',''),(428,92,22,'','','','',''),(433,94,21,'','','','',''),(435,93,10,'','','','',''),(436,93,2,'','','','',''),(437,93,12,'','','','',''),(438,82,5,'','','','',''),(439,90,9,'','','','',''),(440,90,10,'','','','',''),(441,90,12,'','','','',''),(442,94,7,'','','','',''),(449,98,6,'','','','',''),(450,98,8,'','','','',''),(451,98,9,'','','','',''),(452,98,10,'','','','',''),(453,98,11,'','','','',''),(454,98,12,'','','','',''),(455,98,14,'','','','',''),(456,98,15,'','','','',''),(457,98,16,'','','','',''),(458,98,22,'','','','',''),(459,99,5,'','','','',''),(460,99,7,'','','','',''),(461,99,17,'','','','',''),(462,100,2,'','','','',''),(463,100,21,'','','','',''),(464,101,13,'','','','',''),(465,101,18,'','','','',''),(466,101,19,'','','','',''),(467,101,20,'','','','',''),(468,101,23,'','','','',''),(469,101,24,'','','','',''),(470,102,6,'','','','',''),(471,102,8,'','','','',''),(472,102,9,'','','','',''),(473,102,10,'','','','',''),(474,102,11,'','','','',''),(475,102,12,'','','','',''),(476,102,14,'','','','',''),(477,102,15,'','','','',''),(478,102,16,'','','','',''),(479,102,22,'','','','',''),(480,103,5,'','','','',''),(481,103,7,'','','','',''),(482,103,17,'','','','',''),(483,104,2,'','','','',''),(484,104,21,'','','','',''),(485,108,13,'','','','',''),(486,108,18,'','','','',''),(487,108,19,'','','','',''),(488,108,20,'','','','',''),(489,108,23,'','','','',''),(490,108,24,'','','','',''),(537,114,13,'','','','',''),(538,114,18,'','','','',''),(539,114,19,'','','','',''),(540,114,20,'','','','',''),(541,114,23,'','','','',''),(542,114,24,'','','','',''),(543,115,6,'','','','',''),(544,115,8,'','','','',''),(545,115,9,'','','','',''),(546,115,10,'','','','',''),(547,115,11,'','','','',''),(548,115,12,'','','','',''),(549,115,14,'','','','',''),(550,115,15,'','','','',''),(551,115,16,'','','','',''),(552,115,22,'','','','',''),(553,116,5,'','','','',''),(554,116,7,'','','','',''),(555,116,17,'','','','',''),(556,117,2,'','','','',''),(557,117,21,'','','','',''),(558,118,6,'','','','',''),(559,118,8,'','','','',''),(560,118,9,'','','','',''),(561,118,10,'','','','',''),(562,118,11,'','','','',''),(563,118,12,'','','','',''),(564,118,14,'','','','',''),(565,118,15,'','','','',''),(566,118,16,'','','','',''),(567,118,22,'','','','',''),(568,119,5,'','','','',''),(569,119,7,'','','','',''),(570,119,17,'','','','',''),(571,120,2,'','','','',''),(572,120,21,'','','','',''),(573,121,13,'','','','',''),(574,121,18,'','','','',''),(575,121,19,'','','','',''),(576,121,20,'','','','',''),(577,121,23,'','','','',''),(578,121,24,'','','','',''),(579,122,6,'','','','',''),(580,122,8,'','','','',''),(581,122,9,'','','','',''),(582,122,10,'','','','',''),(583,122,11,'','','','',''),(584,122,12,'','','','',''),(585,122,14,'','','','',''),(586,122,15,'','','','',''),(587,122,16,'','','','',''),(588,122,22,'','','','',''),(589,123,5,'','','','',''),(590,123,7,'','','','',''),(591,123,17,'','','','',''),(592,124,2,'','','','',''),(593,124,21,'','','','',''),(594,125,13,'','','','',''),(595,125,18,'','','','',''),(596,125,19,'','','','',''),(597,125,20,'','','','',''),(598,125,23,'','','','',''),(599,125,24,'','','','',''),(600,126,6,'','','','',''),(601,126,8,'','','','',''),(602,126,9,'','','','',''),(603,126,10,'','','','',''),(604,126,11,'','','','',''),(605,126,12,'','','','',''),(606,126,14,'','','','',''),(607,126,15,'','','','',''),(608,126,16,'','','','',''),(609,126,22,'','','','',''),(610,127,5,'','','','',''),(611,127,7,'','','','',''),(612,127,17,'','','','',''),(613,128,2,'','','','',''),(614,128,21,'','','','',''),(788,132,6,'','','','',''),(789,132,12,'','','','',''),(790,132,15,'','','','',''),(791,132,11,'','','','',''),(792,132,8,'','','','',''),(793,132,14,'','','','',''),(794,132,10,'','','','',''),(795,132,16,'','','','',''),(796,132,9,'','','','',''),(797,132,22,'','','','',''),(798,133,17,NULL,NULL,NULL,NULL,NULL),(799,133,7,NULL,NULL,NULL,NULL,NULL),(800,133,5,NULL,NULL,NULL,NULL,NULL),(801,134,17,NULL,NULL,NULL,NULL,NULL),(802,134,7,NULL,NULL,NULL,NULL,NULL),(803,134,5,NULL,NULL,NULL,NULL,NULL),(804,134,9,'0',NULL,NULL,NULL,NULL),(805,135,2,'','','','',''),(806,135,21,'','','','',''),(807,135,5,'','','','',''),(808,116,25,'','','','',''),(809,136,18,'','','','',''),(810,136,24,'','','','',''),(811,136,23,'','','','',''),(812,136,20,'','','','',''),(813,136,13,'','','','',''),(814,136,19,'','','','',''),(815,136,25,'','','','',''),(816,136,7,'','','','',''),(817,136,11,'','','','',''),(818,136,2,'','','','',''),(820,137,18,NULL,NULL,NULL,NULL,NULL),(821,137,24,NULL,NULL,NULL,NULL,NULL),(822,137,23,NULL,NULL,NULL,NULL,NULL),(823,137,20,NULL,NULL,NULL,NULL,NULL),(824,137,13,NULL,NULL,NULL,NULL,NULL),(825,137,19,NULL,NULL,NULL,NULL,NULL),(826,137,25,NULL,NULL,NULL,NULL,NULL),(827,138,18,'','','','',''),(828,138,24,'','','','',''),(829,138,23,'','','','',''),(830,138,20,'','','','',''),(831,138,13,'','','','',''),(832,138,19,'','','','',''),(833,138,25,'','','','',''),(834,139,18,NULL,NULL,NULL,NULL,NULL),(835,139,24,NULL,NULL,NULL,NULL,NULL),(836,139,23,NULL,NULL,NULL,NULL,NULL),(837,139,20,NULL,NULL,NULL,NULL,NULL),(838,139,13,NULL,NULL,NULL,NULL,NULL),(839,139,19,NULL,NULL,NULL,NULL,NULL),(840,139,25,NULL,NULL,NULL,NULL,NULL),(841,142,2,NULL,NULL,NULL,NULL,NULL),(842,142,21,NULL,NULL,NULL,NULL,NULL),(843,144,17,'','','','',''),(844,144,7,'','','','',''),(845,144,5,'','','','',''),(846,145,2,'','','','',''),(847,145,21,'','','','',''),(848,146,17,'','','','',''),(849,146,7,'','','','',''),(850,146,5,'','','','',''),(852,147,7,NULL,NULL,NULL,NULL,NULL),(853,147,5,NULL,NULL,NULL,NULL,NULL),(854,147,2,'0',NULL,NULL,NULL,NULL),(855,147,10,'0',NULL,NULL,NULL,NULL),(856,147,18,'0',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `trips_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `firstName` varchar(50) DEFAULT NULL,
  `LastName` varchar(50) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `pass` varchar(50) DEFAULT NULL,
  `role` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Yassine','Baghdadi','yassine','yassine',0),(2,'admin','admin','admin','admin',0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vans`
--

DROP TABLE IF EXISTS `vans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vans` (
  `id` int NOT NULL AUTO_INCREMENT,
  `matr` varchar(50) DEFAULT NULL,
  `driver` varchar(50) DEFAULT NULL,
  `max_places` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vans`
--

LOCK TABLES `vans` WRITE;
/*!40000 ALTER TABLE `vans` DISABLE KEYS */;
INSERT INTO `vans` VALUES (1,'48A55120','1',18),(2,'84A3354','2',19);
/*!40000 ALTER TABLE `vans` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-07 12:22:12
