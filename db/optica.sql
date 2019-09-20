-- MariaDB dump 10.17  Distrib 10.4.7-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: optica
-- ------------------------------------------------------
-- Server version	10.4.7-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `achat`
--

DROP TABLE IF EXISTS `achat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `achat` (
  `Id_Produit` varchar(50) NOT NULL,
  `Nombre_Produit` int(11) NOT NULL,
  `Prix_Unitaire` float NOT NULL,
  `Nom_Produit` varchar(50) NOT NULL,
  `Numero_Commande` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `achat`
--

LOCK TABLES `achat` WRITE;
/*!40000 ALTER TABLE `achat` DISABLE KEYS */;
/*!40000 ALTER TABLE `achat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client` (
  `Id_Client` int(11) NOT NULL AUTO_INCREMENT,
  `Nom_Client` varchar(50) NOT NULL,
  `Prenom_Client` varchar(250) DEFAULT NULL,
  `Numero_Commande` varchar(250) NOT NULL,
  PRIMARY KEY (`Id_Client`),
  UNIQUE KEY `Numero_Commande` (`Numero_Commande`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commande`
--

DROP TABLE IF EXISTS `commande`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `commande` (
  `Numero_Commande` varchar(255) NOT NULL,
  `Id_Client` int(11) NOT NULL,
  `Date_Commande` datetime NOT NULL,
  `Date_Livraison` datetime DEFAULT NULL,
  `User_Cmd` varchar(30) NOT NULL,
  `User_Livr` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Numero_Commande`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commande`
--

LOCK TABLES `commande` WRITE;
/*!40000 ALTER TABLE `commande` DISABLE KEYS */;
/*!40000 ALTER TABLE `commande` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `monture`
--

DROP TABLE IF EXISTS `monture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `monture` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Ref` varchar(25) NOT NULL,
  `Couleur` varchar(50) NOT NULL,
  `Forme` varchar(50) NOT NULL,
  `Nombre_Stock` int(11) NOT NULL,
  `Reserver` int(11) NOT NULL DEFAULT 0,
  `Prix_Achat` float NOT NULL,
  `Prix_Vente` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monture`
--

LOCK TABLES `monture` WRITE;
/*!40000 ALTER TABLE `monture` DISABLE KEYS */;
INSERT INTO `monture` VALUES (11,'1245','Rouge','Pantos',25,0,5000,7500);
/*!40000 ALTER TABLE `monture` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personnel`
--

DROP TABLE IF EXISTS `personnel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `personnel` (
  `User` varchar(20) NOT NULL,
  `Nom` varchar(50) NOT NULL,
  `Prenom` varchar(50) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Admin` tinyint(1) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personnel`
--

LOCK TABLES `personnel` WRITE;
/*!40000 ALTER TABLE `personnel` DISABLE KEYS */;
INSERT INTO `personnel` VALUES ('gaetan1903','Bakary','Gaetan Jonathan','c16bac42f30d5063f6671b27125938b43dc48ab4',1),('ld','Manankoraisina','Landry Daniel','9cf95dacd226dcf43da376cdb6cbba7035218921',0);
/*!40000 ALTER TABLE `personnel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `verre`
--

DROP TABLE IF EXISTS `verre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `verre` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Ref` varchar(20) NOT NULL,
  `Type_Verre` varchar(30) NOT NULL,
  `Traiter` varchar(30) NOT NULL,
  `Degre` varchar(30) NOT NULL,
  `Nombre_Stock` int(11) NOT NULL,
  `Reserver` int(11) NOT NULL DEFAULT 0,
  `Prix_Achat` float NOT NULL,
  `Prix_Vente` float NOT NULL,
  PRIMARY KEY (`Ref`),
  UNIQUE KEY `id` (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `verre`
--

LOCK TABLES `verre` WRITE;
/*!40000 ALTER TABLE `verre` DISABLE KEYS */;
INSERT INTO `verre` VALUES (1,'VPBcm0.75','Policarbonate','Blancs','-0.75',10,0,10000,12000),(2,'VOAcp0.25','Organqiue','Antireflets','+0.25',10,0,5000,12000);
/*!40000 ALTER TABLE `verre` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-09-20 19:28:15
