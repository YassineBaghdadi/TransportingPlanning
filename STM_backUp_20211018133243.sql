-- MySQL dump 10.13  Distrib 8.0.26, for Linux (x86_64)
--
-- Host: 10.73.200.200    Database: STM
-- ------------------------------------------------------
-- Server version	8.0.26-0ubuntu0.20.04.3

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
  `phone` varchar(20) DEFAULT NULL,
  `grp` int DEFAULT NULL,
  `rpr` varchar(100) DEFAULT NULL,
  `rpr_map` varchar(100) DEFAULT NULL,
  `pic` text,
  PRIMARY KEY (`id`),
  KEY `grp` (`grp`),
  CONSTRAINT `agents_ibfk_1` FOREIGN KEY (`grp`) REFERENCES `grps` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=154 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agents`
--

LOCK TABLES `agents` WRITE;
/*!40000 ALTER TABLE `agents` DISABLE KEYS */;
INSERT INTO `agents` VALUES (82,'SXD0166','OUSSAMA','LAMHAOUIAR','FA153725','MOTORISE',NULL,7,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(83,'SXD0042','HADIL','TAIBI','F664208','Hay AL MOUSTAQBAL  51 rue Mohamed EL KAHOUAJI Sidi Yahya NAJD 1 ',NULL,1,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(84,'SXD0033','ANASS','EL BALI','F442598','Dhar Lamhala, Lot Angad, C25, N10',NULL,4,'Café oslo','34.6866776,-1.8716554','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(85,'SXD0012','HAJAR','BAQALLI','F643352','Boulevard moulay elhassan riad isly villa n 265',NULL,4,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(86,'SXD0013','MOUNA','BARGUACHE','SA19100','Les iris boulevard Oum Rabia.',NULL,4,'Centre mixte','34.6630364,-1.9134147','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(87,'SXD0035','AHMED','EL HANAFY','FE18784','Doha iris  batiment 206 app 24',NULL,4,'Centre mixte','34.6630364,-1.9134147','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(88,'SXD0009','MOHAMED','AZAHAF','S746172','Iris Addoha',NULL,4,'Centre mixte','34.6630364,-1.9134147','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(89,'SXD0043','BILAL','HAMMANE','FJ27509','Hay Iris, rue sabou 2, Numero 15, Oujda, 60000',NULL,4,'Centre mixte','34.6630364,-1.9134147','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(90,'SXD0044','IMANE','HAMMOUTOU','F580238','Lts El aounia Route aounia secteur 0215 N83',NULL,4,'Colaimo','34.6967084,-1.8815927','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(91,'SXD0053','HAJAR','MALEK','FH53246','Hay al wafae route ain beni mathar rue C2 Nr22',NULL,4,'McDonnalds ','34.6765554,-1.9297767','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(92,'SXD0066','OUIJDANE','ZAHOUTE','F586889','Rue Aounia, quartier Achouri, N°1 Oujda',NULL,4,'Rond point laaouniya','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(93,'SXD0041','YASSINE','GAAMOUCH','CN15775','Lts Bellaoui Lot N 877 Etg. 2 60000 SECTEUR 0213',NULL,4,'Rond point la fac','34.6559609,-1.9006412','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(94,'SXD0021','HAJAR','BOUSRHIYAR','F419043','Lot Iris Darâa 04 N° 8',NULL,3,'Centre Mixte','34.6630364,-1.9134147','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(95,'SXD0057','KHALIL','MOUSSAID','F589748','hay zitoun a côté du lycée Abdelah Guenoun ',NULL,3,'Hamame Jaouhara','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(96,'SXD0007','KAOUTHAR','ATTAOUIL','SA19490','Jardin El Qouds a côté de lENCG',NULL,3,'Rond point la fac','34.6559609,-1.9006412','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(97,'SXD0014','NAOUFEL','BEKKAL','Z600026','Rue Sakhae 4  a côté du jardin Andalous',NULL,3,'Jardin andalous','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(98,'SXD0022','CHAIMAE','BOUSRHIYAR','F572842','Lot Iris Darâa 04 N° 8',NULL,3,'Centre Mixte','34.6630364,-1.9134147','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(99,'SXD0023','FADOUA','BRAZ','F547471','MOTORISE',NULL,7,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(100,'SXD0028','MAROUANE','DEFILI','FL95062','Douha Iris Immeuble 206 appat 24',NULL,3,'Rond point Coralia ','34.6649946,-1.9186124','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(101,'SXD0031','MOHAMED','EL AJJOURI','FB106905','Bd annebras hey alhasani',NULL,3,'Mosquée al manssour dahabi','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(102,'SXD0032','IBTISSAM','ELANSARI','F585330','bd el aounia lot douhi rue oued loukous N° 20',NULL,3,'Pharmacie Ousghir','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(103,'SXD0037','MOURAD','EL MAHI','FD22333','RTE AIN SERRAK IMM DOHA 207 APP 13 ',NULL,3,'Rond point Coralia ','34.6649946,-1.9186124','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(104,'SXD0038','KAWKAB','EL MAZOUZI','F582839','zone industrielle ( Maroc telecom/poissonerie aswak salam/maison coca)',NULL,3,'Usine Cocacola/Maroc telecom ','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(105,'SXD0051','ILHAM','LAASSIBA','FL88768','KENZI II - AL ANDALOUS ',NULL,3,'Jardin andalous','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(106,'SXD0055','DOUHA','MEZOUARI','F585953','Rte dalgerie LOT Aqel lot 185 ',NULL,3,'Station Hola Merhaba ','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(107,'SXD0016','HICHAM','BENAMAR','F589835','rue ben said el oujdi nr 34 ',NULL,3,'Souk Melilia','34.6800686,-1.9077273','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(108,'SXD0025','OUALID','CHIHABI','F429928','Rue annaourasse N°34 Agdal ',NULL,3,'Café Rolex ','34.6750894,-1.862512','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(109,'SXD0004','YASSINE','ANNOURI','SZ9197','RTE Ain Serrak  IMM  Doha 154 App  3',NULL,5,'LOrchidée Rose','34.6639504,-1.9157467','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(110,'SXD0002','MERYEM','AIT EL AOUAD','F586123','Imam EL Ghazali N° 14 bis ( Taxi Nador)',NULL,5,'Biougnach','34.6903861,-1.9180592','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(111,'SXD0019','FATIMA ZOHRA','BERRISSOUL','F659036','Quartier Oueld chrif rue 9 N°82',NULL,5,'Biougnach','34.6903861,-1.9180592','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(112,'SXD0065','SALMA','YAHIAOUI','F587736','N°9 rue A28 Hay Almanar Rte Taza',NULL,5,'Biougnach','34.6903861,-1.9180592','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(113,'SXD0054','MOUAAD','MASSAOUDI','R345374','RTE Maghnia Loi*tis Dor El Wouroud N°37',NULL,5,'Biougnach','34.6903861,-1.9180592','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(114,'SXD0036','NABIL','EL MADDAHI','F444540','Quartier El Nour rue S9 N°10 (  Nilou )',NULL,5,'Place 9 Juillet','34.6794282,-1.9202418','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(115,'SXD0063','BADR EDDINE','TANNOUCHE','FA181886','RTE Ain Serrak  IMM  Doha 154 App  4',NULL,5,'LOrchidée Rose','34.6639504,-1.9157467','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(116,'SXD0072','MANAL','SELMI','FA188214','nan',NULL,5,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(117,'SXD0116','NOUHAILA','AHMIAN','S715988','RTE AL JAMIA LOTS ALQODS LOT22 apprt6 oujda',NULL,5,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(118,'SXD0098','RAZAN','BOULAHCEN','SH195900','Rue Ikhlas Hay Najd 1 Sidi Yahya',NULL,5,'Nile Pharmacy','34.6624638,-1.8733987','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(119,'SXD0167','IMANE','ELFILALI','F658921','HAY AL QODS RESIDENCE CHAIMAE OUJDA',NULL,5,'Rond point la fac','34.6559609,-1.9006412','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(120,'SXD0168','OUAIL','SERHIRI','F442604','Hay Benkachour, rue 3 Nr 17, Oujda, Maroc, 60000. Terre.',NULL,5,'Ben Kachour','34.6673963,-1.9118692','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(121,'SXD0169','JIHANE','YAAKOUBI','F578675','hay al andalous rue al kaoutar 1nr 1 oujda',NULL,5,'Rond point la fac','34.6559609,-1.9006412','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(122,'SXD0170','MANAL','BOUNAFAI','SZ5622','Mistral Al Qods Pharmacie El Azzaoui',NULL,5,'Rond point la fac','34.6559609,-1.9006412','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(123,'SXD0171','SAFAE','KHARBOUCHE','ZG164400','Mistral Al Qods Pharmacie El Azzaoui',NULL,5,'Rond point la fac','34.6559609,-1.9006412','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(124,'SXD0111','TAHAYASSINE','BOUCHAMA','nan','MOTORISE',NULL,7,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(125,'SXD0011','AMINA','AZZMOURI','F444187','Rue Al Israe, Hay Al Qods, N° 16 - Oujda',NULL,5,'Rond point la fac','34.6559609,-1.9006412','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(126,'SXD0082','NADIA','AZZIMANI','F530757','RTE el aounia lot talhaoui rue E Nr 12 Oujda',NULL,7,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(127,'SXD0087','MERYEM','EL ARABI','F581299','nan',NULL,5,'Place 9 Juillet','34.6794282,-1.9202418','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(128,'SXD0172','AMINA','IDRAOUI','nan','LOT 76 DHAR LAMHALA HAY ELFARAH OUJDA (à côté de lycée ibn sina)',NULL,1,'Lycé Ibn Sina Hay Al FARAH','34.6866164,-1.8724977','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(129,'SXD0175','NAJOUA','BELMAHI','nan','Lot BENSAHLI rue Alaatae 1 N° 27 Agdal Oujda (à côté de l’agence BP)',NULL,1,'BP Quartier Agdal avenue Ibrahim Roudani','34.6755134,-1.8621477','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(130,'SXD0139','ILYAS','HAMRI','nan','Belhoucine 8 rue Skhirate Hay Zaytoune Oujda',NULL,1,'Lycée Mohammed 6 Lazaret','34.6768311,-1.8872976','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(131,'SXD0047','ANASS','KADA','S750520','nan',NULL,7,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(132,'SXD0140','YASSINE','BAGHDADI','ZG141585','block C2 imm 59 etage 1 N B Kenzi 2 alandaloss',NULL,7,'kenzi 2','34.6533176,-1.8806658','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(133,'SXD0127','MOHAMED','ZEROUALI','F375305','BD MLY HASSAN RIAD ISLY N° 159 OUJDA 60000',NULL,1,'Café Paris Route Marjane ','34.7229883,-1.9103077','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(134,'SXD0128','LAFTASS','SAID','nan','nan',NULL,7,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(135,'SXD0129','ARFAOUI','NAJIB','nan','nan',NULL,7,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(136,'SXD0130','GHAZOUANI','SAID','nan','nan',NULL,7,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(137,'SXD0131','HAYAT','AMARTI','F290795','nan',NULL,7,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(138,'SXD0132','IMANE','ER REZGUI','nan','nan',NULL,7,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(139,'SXD0133','SOUAD','ER REZGUI','nan','nan',NULL,7,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(140,'SXD0134','KASMI','ABDESSAMAD','nan','nan',NULL,7,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(141,'SXD0135','AYOUB','BEN MOUSSA','F587303','hay nour ain bni mather rue c 11 n°29',NULL,7,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(142,'SXD0141','CHEIKH AHMET TIDIANE','KONE','nan','nan',NULL,7,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(143,'SXD0143','SOUAD','BOUMAIZE','F379663','KENZI II - AL ANDALOUS ',NULL,7,'kenzi 2','34.6533176,-1.8806658','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(144,'SXD0178','REGIS','DABO NGAGO','BE57481K','nan',NULL,7,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(145,'XCD0002','AMADOU','PALAIS JANVIER','nan','MOTORISE',NULL,7,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(146,'nan','GHISLAINE','CHERRAT','nan','MOTORISE',NULL,7,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(147,'SXD0177','WAKA','LANCELOT','nan','nan',NULL,7,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(148,'WEA0007','SEYNABOU','CAMARA','nan','nan',NULL,7,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(149,'SXD0136','BOUNOUA','MIMOUNE','nan','nan',NULL,7,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(150,'nan','ALI','BENHAMOU','PY826139','263 GH40 ADDOHA OUJDA (rondpoint CORALIA)',NULL,1,'Rond point Coralia ','34.6649946,-1.9186124','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(151,'nan','EL HADJI DJIBRIL','DIAGNE ','BE62406D','nan',NULL,7,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(152,'nan','IMANE','OUFKIR','nan','Rue de boudir lot ben ziane N45 OUJDA ',NULL,7,'nan','nan','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4'),(153,'nan','CHOROUK','ZEROUALI','FB126751','Mistral Al Qods',NULL,5,'Rond point la fac','34.6559609,-1.9006412','https://firebasestorage.googleapis.com/v0/b/saccomxd-stm-yassine-baghdadi.appspot.com/o/profile.png?alt=media&token=30aaedee-2f7d-4b96-ad58-4649ae578ca4');
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
  `username` varchar(45) DEFAULT NULL,
  `pass` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drivers`
--

LOCK TABLES `drivers` WRITE;
/*!40000 ALTER TABLE `drivers` DISABLE KEYS */;
INSERT INTO `drivers` VALUES (1,'najib','najib','najib','1234'),(2,'said','said','said','1234');
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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grps`
--

LOCK TABLES `grps` WRITE;
/*!40000 ALTER TABLE `grps` DISABLE KEYS */;
INSERT INTO `grps` VALUES (1,'TDE','08-17'),(3,'SIC','14-23'),(4,'QSDEV','13-22'),(5,'ALTIMA','13-22'),(6,'MYASSURE','09-18'),(7,'STAFF','08-17');
/*!40000 ALTER TABLE `grps` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `logsfile`
--

DROP TABLE IF EXISTS `logsfile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `logsfile` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user` varchar(45) DEFAULT NULL,
  `query` varchar(500) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `descr` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
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
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trips`
--

LOCK TABLES `trips` WRITE;
/*!40000 ALTER TABLE `trips` DISABLE KEYS */;
INSERT INTO `trips` VALUES (7,1,1,'2021-10-15 17:00:00','OUT',NULL,NULL,NULL,NULL,NULL,NULL),(8,1,1,'2021-10-18 13:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(11,1,1,'2021-10-19 08:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(13,1,1,'2021-10-19 12:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(14,2,2,'2021-10-20 13:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL),(15,1,1,'2021-10-28 01:00:00','IN',NULL,NULL,NULL,NULL,NULL,NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=123 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trips_history`
--

LOCK TABLES `trips_history` WRITE;
/*!40000 ALTER TABLE `trips_history` DISABLE KEYS */;
INSERT INTO `trips_history` VALUES (39,7,143,NULL,NULL,NULL,NULL,NULL),(40,7,132,NULL,NULL,NULL,NULL,NULL),(41,7,150,NULL,NULL,NULL,NULL,NULL),(42,7,129,NULL,NULL,NULL,NULL,NULL),(43,7,130,NULL,NULL,NULL,NULL,NULL),(44,7,128,NULL,NULL,NULL,NULL,NULL),(45,7,133,NULL,NULL,NULL,NULL,NULL),(46,7,139,NULL,NULL,NULL,NULL,NULL),(47,7,82,NULL,NULL,NULL,NULL,NULL),(48,7,138,NULL,NULL,NULL,NULL,NULL),(49,7,137,NULL,NULL,NULL,NULL,NULL),(50,7,136,NULL,NULL,NULL,NULL,NULL),(51,7,135,NULL,NULL,NULL,NULL,NULL),(52,7,134,NULL,NULL,NULL,NULL,NULL),(53,7,131,NULL,NULL,NULL,NULL,NULL),(54,7,126,NULL,NULL,NULL,NULL,NULL),(55,7,124,NULL,NULL,NULL,NULL,NULL),(56,7,99,NULL,NULL,NULL,NULL,NULL),(57,7,140,NULL,NULL,NULL,NULL,NULL),(58,8,93,NULL,NULL,NULL,NULL,NULL),(59,8,119,NULL,NULL,NULL,NULL,NULL),(60,8,121,NULL,NULL,NULL,NULL,NULL),(61,8,153,NULL,NULL,NULL,NULL,NULL),(62,8,122,NULL,NULL,NULL,NULL,NULL),(63,8,125,NULL,NULL,NULL,NULL,NULL),(64,8,123,NULL,NULL,NULL,NULL,NULL),(65,8,118,NULL,NULL,NULL,NULL,NULL),(66,8,89,NULL,NULL,NULL,NULL,NULL),(67,8,88,NULL,NULL,NULL,NULL,NULL),(68,8,87,NULL,NULL,NULL,NULL,NULL),(69,8,86,NULL,NULL,NULL,NULL,NULL),(70,8,109,NULL,NULL,NULL,NULL,NULL),(71,8,115,NULL,NULL,NULL,NULL,NULL),(72,8,120,NULL,NULL,NULL,NULL,NULL),(73,8,91,NULL,NULL,NULL,NULL,NULL),(74,8,127,NULL,NULL,NULL,NULL,NULL),(75,8,114,NULL,NULL,NULL,NULL,NULL),(76,8,84,NULL,NULL,NULL,NULL,NULL),(77,11,143,NULL,NULL,NULL,NULL,NULL),(78,11,132,NULL,NULL,NULL,NULL,NULL),(79,11,150,NULL,NULL,NULL,NULL,NULL),(80,11,129,NULL,NULL,NULL,NULL,NULL),(81,11,130,NULL,NULL,NULL,NULL,NULL),(82,11,128,NULL,NULL,NULL,NULL,NULL),(83,11,133,NULL,NULL,NULL,NULL,NULL),(84,11,139,NULL,NULL,NULL,NULL,NULL),(85,11,82,NULL,NULL,NULL,NULL,NULL),(86,11,138,NULL,NULL,NULL,NULL,NULL),(87,11,137,NULL,NULL,NULL,NULL,NULL),(88,11,136,NULL,NULL,NULL,NULL,NULL),(89,11,135,NULL,NULL,NULL,NULL,NULL),(90,11,134,NULL,NULL,NULL,NULL,NULL),(91,11,131,NULL,NULL,NULL,NULL,NULL),(92,11,126,NULL,NULL,NULL,NULL,NULL),(93,11,124,NULL,NULL,NULL,NULL,NULL),(95,11,140,NULL,NULL,NULL,NULL,NULL),(96,11,97,'0',NULL,NULL,NULL,NULL),(97,13,93,'0',NULL,NULL,NULL,NULL),(99,14,119,NULL,NULL,NULL,NULL,NULL),(101,14,153,NULL,NULL,NULL,NULL,NULL),(102,14,122,NULL,NULL,NULL,NULL,NULL),(103,14,125,NULL,NULL,NULL,NULL,NULL),(104,14,123,NULL,NULL,NULL,NULL,NULL),(105,14,118,NULL,NULL,NULL,NULL,NULL),(106,14,89,NULL,NULL,NULL,NULL,NULL),(107,14,88,NULL,NULL,NULL,NULL,NULL),(108,14,87,NULL,NULL,NULL,NULL,NULL),(109,14,86,NULL,NULL,NULL,NULL,NULL),(110,14,109,NULL,NULL,NULL,NULL,NULL),(111,14,115,NULL,NULL,NULL,NULL,NULL),(112,14,120,NULL,NULL,NULL,NULL,NULL),(113,14,91,NULL,NULL,NULL,NULL,NULL),(114,14,127,NULL,NULL,NULL,NULL,NULL),(115,14,114,NULL,NULL,NULL,NULL,NULL),(116,14,84,NULL,NULL,NULL,NULL,NULL),(117,14,129,'0',NULL,NULL,NULL,NULL),(118,14,104,'0',NULL,NULL,NULL,NULL),(119,15,97,'0',NULL,NULL,NULL,NULL),(120,15,100,'0',NULL,NULL,NULL,NULL),(121,15,99,'0',NULL,NULL,NULL,NULL),(122,15,131,'0',NULL,NULL,NULL,NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'yassine','baghdadi','yassine','yassine',0);
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vans`
--

LOCK TABLES `vans` WRITE;
/*!40000 ALTER TABLE `vans` DISABLE KEYS */;
INSERT INTO `vans` VALUES (1,'van 1','2',19),(2,'van2','1',19);
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

-- Dump completed on 2021-10-18 13:32:45
