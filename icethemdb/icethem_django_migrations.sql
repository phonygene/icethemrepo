-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: icethem
-- ------------------------------------------------------
-- Server version	5.7.19-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_czech_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_czech_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-01-25 02:35:03.119772'),(2,'auth','0001_initial','2018-01-25 02:35:09.639388'),(3,'admin','0001_initial','2018-01-25 02:35:10.946526'),(4,'admin','0002_logentry_remove_auto_add','2018-01-25 02:35:10.965518'),(5,'contenttypes','0002_remove_content_type_name','2018-01-25 02:35:12.181639'),(6,'auth','0002_alter_permission_name_max_length','2018-01-25 02:35:12.776010'),(7,'auth','0003_alter_user_email_max_length','2018-01-25 02:35:13.318078'),(8,'auth','0004_alter_user_username_opts','2018-01-25 02:35:13.344079'),(9,'auth','0005_alter_user_last_login_null','2018-01-25 02:35:13.766480'),(10,'auth','0006_require_contenttypes_0002','2018-01-25 02:35:13.801293'),(11,'auth','0007_alter_validators_add_error_messages','2018-01-25 02:35:13.849140'),(12,'auth','0008_alter_user_username_max_length','2018-01-25 02:35:14.904895'),(13,'auth','0009_alter_user_last_name_max_length','2018-01-25 02:35:15.555471'),(14,'sessions','0001_initial','2018-01-25 02:35:15.956010'),(15,'user','0001_initial','2018-01-25 02:35:16.192882'),(16,'user','0002_auto_20180112_1413','2018-01-25 02:35:16.310392'),(17,'user','0003_auto_20180124_1513','2018-01-25 02:35:16.332615');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-01-29  9:53:39
