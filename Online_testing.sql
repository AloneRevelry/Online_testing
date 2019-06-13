-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: Online_testing
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.18.04.2

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
-- Table structure for table `User_user`
--

DROP TABLE IF EXISTS `User_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `user_type` varchar(20) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User_user`
--

LOCK TABLES `User_user` WRITE;
/*!40000 ALTER TABLE `User_user` DISABLE KEYS */;
INSERT INTO `User_user` VALUES (1,'pbkdf2_sha256$150000$dQJPKcGPtRJg$vgQCEtUODz7VSbiLZkstCae858Kh60WnPBbVGgFgr6Y=','2019-04-30 16:02:22.873987',1,'admin','','','',1,'2019-04-22 21:36:00.000000','teacher',1),(2,'pbkdf2_sha256$150000$PgjU6U8VZNc3$khvs9PQJ1yC2BNRHJPvBVtJptnqxG7y+GQb7NesQXJY=','2019-04-23 12:03:49.106504',0,'1610121101','明','小','',1,'2019-04-22 21:42:05.146772','student',0),(5,'pbkdf2_sha256$150000$7L7qE5AzQ0Q4$KRMITsM9REbrmNGUyN02Fj8FXLFeRqY6EmCrc3VLAmE=','2019-04-30 16:02:44.483847',0,'2019001','老师','张','',1,'2019-04-22 21:44:14.034014','teacher',0),(6,'pbkdf2_sha256$150000$b6lItxKIJYH3$6sJ07nJRB2l265BJebCHlBCndfIj/R160GdMGe4S4Dw=','2019-04-24 18:14:00.000000',0,'2019002','老师','李','',1,'2019-04-22 21:44:00.000000','teacher',1),(10,'pbkdf2_sha256$150000$4OudJyvNQDB5$Oi/5AD9JfTl8PDLvDqbuH1o0sR6WIpfRcUlvTQPKIsU=','2019-04-24 14:44:38.354584',0,'1610121103','','','',1,'2019-04-23 01:12:55.595607','student',0),(11,'pbkdf2_sha256$150000$zXdOlcwXKUra$LqVzLbjERuRjbL58Bqqyby21KoOz00bzoq5g0XO6gWw=','2019-04-24 16:20:45.620360',0,'1610121104','','','',1,'2019-04-23 16:54:49.622851','student',0),(12,'pbkdf2_sha256$150000$qdsHE9N51dPr$SxvpsQorPn9i48pGydXWN5O8DMW+QA/bGNjpZhDB9r0=','2019-04-30 15:06:56.601150',0,'1610121105','','','',1,'2019-04-23 16:54:49.970292','student',0),(13,'pbkdf2_sha256$150000$zAun5smr1HXT$b/D0lh5A08+SJ8FxntPKBJcdh8ZqeaRbK/Nrd8JmZ5Y=',NULL,0,'1610121106','','','',1,'2019-04-23 16:54:50.471643','student',0),(14,'pbkdf2_sha256$150000$XHT2tNcLB98x$pbBAtIkVft6dCdqA1Iin/yKSIcJQuAEQxqaGRNg7eps=',NULL,0,'1610121107','','','',1,'2019-04-23 16:54:50.794475','student',0),(15,'pbkdf2_sha256$150000$b1Nz7Rs214y7$WhcdGFVfEaczI7PZqUMW8C5IzRV+l798zFSSSQwTR+E=',NULL,0,'1610121108','','','',1,'2019-04-23 16:54:51.116819','student',0),(16,'pbkdf2_sha256$150000$FiLKoawEN13i$NiGvD9xYV6Imurh+OrtWXsDOgi51z84ahlkDJRmaZdA=',NULL,0,'1610121109','','','',1,'2019-04-23 16:54:51.461716','student',0),(17,'pbkdf2_sha256$150000$ZpzW6BJ3DBA3$oeRkeLjzdlptfeBe2dhrcjkgEaCrjNRzP4cI4ZjHLtM=',NULL,0,'161012110','','','',1,'2019-04-23 21:26:11.655733','student',0);
/*!40000 ALTER TABLE `User_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User_user_groups`
--

DROP TABLE IF EXISTS `User_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `User_user_groups_user_id_group_id_e1236af7_uniq` (`user_id`,`group_id`),
  KEY `User_user_groups_group_id_ca46cfeb_fk_auth_group_id` (`group_id`),
  CONSTRAINT `User_user_groups_group_id_ca46cfeb_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `User_user_groups_user_id_8a581615_fk_User_user_id` FOREIGN KEY (`user_id`) REFERENCES `User_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User_user_groups`
--

LOCK TABLES `User_user_groups` WRITE;
/*!40000 ALTER TABLE `User_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `User_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User_user_user_permissions`
--

DROP TABLE IF EXISTS `User_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `User_user_user_permissions_user_id_permission_id_f20e58ff_uniq` (`user_id`,`permission_id`),
  KEY `User_user_user_permi_permission_id_6ee76041_fk_auth_perm` (`permission_id`),
  CONSTRAINT `User_user_user_permi_permission_id_6ee76041_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `User_user_user_permissions_user_id_321bdf68_fk_User_user_id` FOREIGN KEY (`user_id`) REFERENCES `User_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User_user_user_permissions`
--

LOCK TABLES `User_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `User_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `User_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add 班级信息',6,'add_class'),(22,'Can change 班级信息',6,'change_class'),(23,'Can delete 班级信息',6,'delete_class'),(24,'Can view 班级信息',6,'view_class'),(25,'Can add 用户列表',7,'add_user'),(26,'Can change 用户列表',7,'change_user'),(27,'Can delete 用户列表',7,'delete_user'),(28,'Can view 用户列表',7,'view_user'),(29,'Can add 教师信息',8,'add_teacher'),(30,'Can change 教师信息',8,'change_teacher'),(31,'Can delete 教师信息',8,'delete_teacher'),(32,'Can view 教师信息',8,'view_teacher'),(33,'Can add 学生信息',9,'add_student'),(34,'Can change 学生信息',9,'change_student'),(35,'Can delete 学生信息',9,'delete_student'),(36,'Can view 学生信息',9,'view_student'),(37,'Can add 提交文件信息',10,'add_files'),(38,'Can change 提交文件信息',10,'change_files'),(39,'Can delete 提交文件信息',10,'delete_files'),(40,'Can view 提交文件信息',10,'view_files'),(41,'Can add 考试信息',11,'add_examinfo'),(42,'Can change 考试信息',11,'change_examinfo'),(43,'Can delete 考试信息',11,'delete_examinfo'),(44,'Can view 考试信息',11,'view_examinfo'),(45,'Can add Bookmark',12,'add_bookmark'),(46,'Can change Bookmark',12,'change_bookmark'),(47,'Can delete Bookmark',12,'delete_bookmark'),(48,'Can view Bookmark',12,'view_bookmark'),(49,'Can add User Setting',13,'add_usersettings'),(50,'Can change User Setting',13,'change_usersettings'),(51,'Can delete User Setting',13,'delete_usersettings'),(52,'Can view User Setting',13,'view_usersettings'),(53,'Can add User Widget',14,'add_userwidget'),(54,'Can change User Widget',14,'change_userwidget'),(55,'Can delete User Widget',14,'delete_userwidget'),(56,'Can view User Widget',14,'view_userwidget'),(57,'Can add log entry',15,'add_log'),(58,'Can change log entry',15,'change_log'),(59,'Can delete log entry',15,'delete_log'),(60,'Can view log entry',15,'view_log');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `class_info`
--

DROP TABLE IF EXISTS `class_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `class_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `classname` varchar(20) NOT NULL,
  `exam_flag` tinyint(1) NOT NULL,
  `msg` varchar(200) DEFAULT NULL,
  `exam_title` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class_info`
--

LOCK TABLES `class_info` WRITE;
/*!40000 ALTER TABLE `class_info` DISABLE KEYS */;
INSERT INTO `class_info` VALUES (1,'16级计科一班',1,'',NULL),(2,'16级计科二班',0,NULL,'test1'),(3,'16级计科三班',0,NULL,NULL),(4,'16级软工一班',0,NULL,NULL),(5,'16级软工二班',0,NULL,NULL),(6,'16级网工一班',0,NULL,NULL);
/*!40000 ALTER TABLE `class_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_User_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_User_user_id` FOREIGN KEY (`user_id`) REFERENCES `User_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(5,'sessions','session'),(10,'Student','files'),(11,'Teacher','examinfo'),(6,'User','class'),(9,'User','student'),(8,'User','teacher'),(7,'User','user'),(12,'xadmin','bookmark'),(15,'xadmin','log'),(13,'xadmin','usersettings'),(14,'xadmin','userwidget');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-04-22 21:35:49.818461'),(2,'contenttypes','0002_remove_content_type_name','2019-04-22 21:35:51.075816'),(3,'auth','0001_initial','2019-04-22 21:35:52.155342'),(4,'auth','0002_alter_permission_name_max_length','2019-04-22 21:35:55.903113'),(5,'auth','0003_alter_user_email_max_length','2019-04-22 21:35:55.958151'),(6,'auth','0004_alter_user_username_opts','2019-04-22 21:35:56.024974'),(7,'auth','0005_alter_user_last_login_null','2019-04-22 21:35:56.092237'),(8,'auth','0006_require_contenttypes_0002','2019-04-22 21:35:56.137118'),(9,'auth','0007_alter_validators_add_error_messages','2019-04-22 21:35:56.203538'),(10,'auth','0008_alter_user_username_max_length','2019-04-22 21:35:56.270491'),(11,'auth','0009_alter_user_last_name_max_length','2019-04-22 21:35:56.341606'),(12,'auth','0010_alter_group_name_max_length','2019-04-22 21:35:57.176004'),(13,'auth','0011_update_proxy_permissions','2019-04-22 21:35:57.242098'),(14,'User','0001_initial','2019-04-22 21:35:59.411207'),(15,'Student','0001_initial','2019-04-22 21:36:06.441273'),(16,'Student','0002_files_student','2019-04-22 21:36:07.059130'),(17,'Teacher','0001_initial','2019-04-22 21:36:07.993636'),(18,'Teacher','0002_examinfo_teacher','2019-04-22 21:36:08.638451'),(19,'admin','0001_initial','2019-04-22 21:36:09.982018'),(20,'admin','0002_logentry_remove_auto_add','2019-04-22 21:36:11.486350'),(21,'admin','0003_logentry_add_action_flag_choices','2019-04-22 21:36:11.531637'),(22,'sessions','0001_initial','2019-04-22 21:36:11.924723'),(23,'xadmin','0001_initial','2019-04-22 21:36:13.167079'),(24,'xadmin','0002_log','2019-04-22 21:36:17.132285'),(25,'xadmin','0003_auto_20160715_0100','2019-04-22 21:36:20.191314'),(26,'User','0002_student_examname','2019-04-22 22:28:08.025316'),(27,'User','0003_student_msg','2019-04-24 16:51:25.493205'),(28,'User','0004_auto_20190424_1655','2019-04-24 16:55:49.553085'),(29,'User','0005_class_exam_title','2019-04-24 17:57:23.147640');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_file`
--

DROP TABLE IF EXISTS `student_file`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student_file` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Filename` varchar(100) NOT NULL,
  `Filedata` longblob NOT NULL,
  `Filesize` varchar(100) NOT NULL,
  `Filetime` datetime(6) NOT NULL,
  `student_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `student_file_student_id_045c5dbc_fk_student_info_id` (`student_id`),
  CONSTRAINT `student_file_student_id_045c5dbc_fk_student_info_id` FOREIGN KEY (`student_id`) REFERENCES `student_info` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_file`
--

LOCK TABLES `student_file` WRITE;
/*!40000 ALTER TABLE `student_file` DISABLE KEYS */;
/*!40000 ALTER TABLE `student_file` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_info`
--

DROP TABLE IF EXISTS `student_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `studentname` varchar(20) NOT NULL,
  `sip` varchar(20) DEFAULT NULL,
  `submittime` datetime(6) DEFAULT NULL,
  `Class_id` int(11) NOT NULL,
  `user_id_id` int(11) NOT NULL,
  `examname` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id_id` (`user_id_id`),
  KEY `student_info_Class_id_fb44fdf8_fk_class_info_id` (`Class_id`),
  CONSTRAINT `student_info_Class_id_fb44fdf8_fk_class_info_id` FOREIGN KEY (`Class_id`) REFERENCES `class_info` (`id`),
  CONSTRAINT `student_info_user_id_id_3d950fdc_fk_User_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `User_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_info`
--

LOCK TABLES `student_info` WRITE;
/*!40000 ALTER TABLE `student_info` DISABLE KEYS */;
INSERT INTO `student_info` VALUES (1,'小明','127.0.0.1','2019-04-23 12:04:42.514098',1,2,'计算机网络期末测试'),(3,'小白','127.0.0.1','2019-04-23 01:38:45.132424',1,10,'计算机网络期末测试'),(4,'小黑','127.0.0.1',NULL,1,11,'计算机网络期末测试'),(5,'小蓝','192.168.253.5',NULL,1,12,'计算机网络期末测试'),(6,'小绿',NULL,NULL,1,13,'计算机网络期末测试'),(7,'小紫',NULL,NULL,1,14,'计算机网络期末测试'),(8,'小粉',NULL,NULL,1,15,'计算机网络期末测试'),(9,'小灰',NULL,NULL,1,16,'计算机网络期末测试');
/*!40000 ALTER TABLE `student_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher_examinfo`
--

DROP TABLE IF EXISTS `teacher_examinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teacher_examinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Examtitle` varchar(50) NOT NULL,
  `Examstarttime` datetime(6) NOT NULL,
  `is_auto` tinyint(1) NOT NULL,
  `Examstatus` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `teacher_examinfo_teacher_id_185ceed5_fk_teacher_info_id` (`teacher_id`),
  CONSTRAINT `teacher_examinfo_teacher_id_185ceed5_fk_teacher_info_id` FOREIGN KEY (`teacher_id`) REFERENCES `teacher_info` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher_examinfo`
--

LOCK TABLES `teacher_examinfo` WRITE;
/*!40000 ALTER TABLE `teacher_examinfo` DISABLE KEYS */;
INSERT INTO `teacher_examinfo` VALUES (1,'C++期末测试','2019-04-22 22:00:00.000000',1,0,1),(2,'Java期末测试','2019-04-22 22:07:00.000000',1,-1,1),(4,'C#期末测试','2019-08-23 22:41:00.000000',1,0,1),(7,'计算机网络期末测试','2019-04-24 01:41:00.000000',1,1,1);
/*!40000 ALTER TABLE `teacher_examinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher_info`
--

DROP TABLE IF EXISTS `teacher_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teacher_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `teachername` varchar(20) NOT NULL,
  `Class_id` int(11) NOT NULL,
  `user_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id_id` (`user_id_id`),
  KEY `teacher_info_Class_id_8d4b8fad_fk_class_info_id` (`Class_id`),
  CONSTRAINT `teacher_info_Class_id_8d4b8fad_fk_class_info_id` FOREIGN KEY (`Class_id`) REFERENCES `class_info` (`id`),
  CONSTRAINT `teacher_info_user_id_id_a4c68297_fk_User_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `User_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher_info`
--

LOCK TABLES `teacher_info` WRITE;
/*!40000 ALTER TABLE `teacher_info` DISABLE KEYS */;
INSERT INTO `teacher_info` VALUES (1,'张老师',1,5),(2,'李老师',2,6);
/*!40000 ALTER TABLE `teacher_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xadmin_bookmark`
--

DROP TABLE IF EXISTS `xadmin_bookmark`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xadmin_bookmark` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(128) NOT NULL,
  `url_name` varchar(64) NOT NULL,
  `query` varchar(1000) NOT NULL,
  `is_share` tinyint(1) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_bookmark_content_type_id_60941679_fk_django_co` (`content_type_id`),
  KEY `xadmin_bookmark_user_id_42d307fc_fk_User_user_id` (`user_id`),
  CONSTRAINT `xadmin_bookmark_content_type_id_60941679_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_bookmark_user_id_42d307fc_fk_User_user_id` FOREIGN KEY (`user_id`) REFERENCES `User_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xadmin_bookmark`
--

LOCK TABLES `xadmin_bookmark` WRITE;
/*!40000 ALTER TABLE `xadmin_bookmark` DISABLE KEYS */;
/*!40000 ALTER TABLE `xadmin_bookmark` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xadmin_log`
--

DROP TABLE IF EXISTS `xadmin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xadmin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `ip_addr` char(39) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` varchar(32) NOT NULL,
  `message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` (`content_type_id`),
  KEY `xadmin_log_user_id_bb16a176_fk_User_user_id` (`user_id`),
  CONSTRAINT `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_log_user_id_bb16a176_fk_User_user_id` FOREIGN KEY (`user_id`) REFERENCES `User_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xadmin_log`
--

LOCK TABLES `xadmin_log` WRITE;
/*!40000 ALTER TABLE `xadmin_log` DISABLE KEYS */;
INSERT INTO `xadmin_log` VALUES (1,'2019-04-22 21:39:11.202403','127.0.0.1','1','Class object (1)','create','已添加。',6,1),(2,'2019-04-22 21:39:27.231110','127.0.0.1','2','Class object (2)','create','已添加。',6,1),(3,'2019-04-22 21:39:37.240062','127.0.0.1','3','Class object (3)','create','已添加。',6,1),(4,'2019-04-22 21:39:55.096647','127.0.0.1','4','Class object (4)','create','已添加。',6,1),(5,'2019-04-22 21:40:05.488617','127.0.0.1','5','Class object (5)','create','已添加。',6,1),(6,'2019-04-22 21:40:24.727420','127.0.0.1','6','Class object (6)','create','已添加。',6,1),(7,'2019-04-22 21:42:05.365494','127.0.0.1','2','1610121101','create','已添加。',7,1),(8,'2019-04-22 21:42:20.746130','127.0.0.1','1','admin','change','Changed last_login 和 user_type.',7,1),(9,'2019-04-22 21:42:53.169031','127.0.0.1','3','1610121102','create','已添加。',7,1),(10,'2019-04-22 21:44:14.168308','127.0.0.1','5','2019001','create','已添加。',7,1),(11,'2019-04-22 21:44:34.444254','127.0.0.1','6','2019002','create','已添加。',7,1),(12,'2019-04-22 21:48:02.938355','127.0.0.1','1','1610121101','create','已添加。',9,1),(13,'2019-04-22 21:48:20.744542','127.0.0.1','2','1610121102','create','已添加。',9,1),(14,'2019-04-22 21:48:40.637634','127.0.0.1','1','2019001','create','已添加。',8,1),(15,'2019-04-22 21:48:52.780620','127.0.0.1','2','2019002','create','已添加。',8,1),(16,'2019-04-22 22:39:52.246148','127.0.0.1',NULL,'','delete','Batch delete 5 提交文件信息.',NULL,1),(17,'2019-04-22 22:40:19.128404','127.0.0.1','1','16级计科一班','change','Changed exam_flag.',6,1),(18,'2019-04-23 01:06:03.257448','127.0.0.1',NULL,'','delete','Batch delete 1 用户列表.',NULL,1),(19,'2019-04-23 01:10:45.040347','127.0.0.1',NULL,'','delete','Batch delete 1 用户列表.',NULL,1),(20,'2019-04-23 01:34:31.657937','127.0.0.1','1','1610121101','change','Changed submittime 和 examname.',9,1),(21,'2019-04-23 16:55:50.159051','127.0.0.1','9','1610121109','change','Changed examname.',9,1),(22,'2019-04-23 16:55:55.118548','127.0.0.1','8','1610121108','change','Changed examname.',9,1),(23,'2019-04-23 16:55:59.571294','127.0.0.1','7','1610121107','change','Changed examname.',9,1),(24,'2019-04-23 16:56:03.909533','127.0.0.1','6','1610121106','change','Changed examname.',9,1),(25,'2019-04-23 16:56:08.299898','127.0.0.1','5','1610121105','change','Changed examname.',9,1),(26,'2019-04-23 16:56:13.314769','127.0.0.1','4','1610121104','change','Changed examname.',9,1),(27,'2019-04-24 10:16:16.802012','127.0.0.1','7','Examinfo object (7)','change','Changed Examstarttime 和 Examstatus.',11,1),(28,'2019-04-24 10:18:18.251662','127.0.0.1','1','16级计科一班','change','Changed exam_flag.',6,1),(29,'2019-04-24 13:18:47.713840','127.0.0.1','10','161012110','change','Changed examname.',9,1),(30,'2019-04-24 18:19:22.305553','127.0.0.1','6','2019002','change','Changed last_login 和 is_staff.',7,1),(31,'2019-04-24 18:57:39.550239','127.0.0.1',NULL,'','delete','Batch delete 1 学生信息.',NULL,1),(32,'2019-04-24 18:58:50.320484','127.0.0.1',NULL,'','delete','Batch delete 4 提交文件信息.',NULL,1);
/*!40000 ALTER TABLE `xadmin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xadmin_usersettings`
--

DROP TABLE IF EXISTS `xadmin_usersettings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xadmin_usersettings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(256) NOT NULL,
  `value` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_usersettings_user_id_edeabe4a_fk_User_user_id` (`user_id`),
  CONSTRAINT `xadmin_usersettings_user_id_edeabe4a_fk_User_user_id` FOREIGN KEY (`user_id`) REFERENCES `User_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xadmin_usersettings`
--

LOCK TABLES `xadmin_usersettings` WRITE;
/*!40000 ALTER TABLE `xadmin_usersettings` DISABLE KEYS */;
INSERT INTO `xadmin_usersettings` VALUES (1,'dashboard:home:pos','',1);
/*!40000 ALTER TABLE `xadmin_usersettings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xadmin_userwidget`
--

DROP TABLE IF EXISTS `xadmin_userwidget`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xadmin_userwidget` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_id` varchar(256) NOT NULL,
  `widget_type` varchar(50) NOT NULL,
  `value` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_userwidget_user_id_c159233a_fk_User_user_id` (`user_id`),
  CONSTRAINT `xadmin_userwidget_user_id_c159233a_fk_User_user_id` FOREIGN KEY (`user_id`) REFERENCES `User_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xadmin_userwidget`
--

LOCK TABLES `xadmin_userwidget` WRITE;
/*!40000 ALTER TABLE `xadmin_userwidget` DISABLE KEYS */;
/*!40000 ALTER TABLE `xadmin_userwidget` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-05-30 22:16:00
