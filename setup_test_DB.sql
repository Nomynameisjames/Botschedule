 -- Creates database hbnb_test_db

DROP DATABASE IF EXISTS BotSchedule_test_db;

CREATE DATABASE IF NOT EXISTS BotSchedule_test_db;
USE BotSchedule_test_db;
CREATE USER IF NOT EXISTS 'BotSchedule_test'@'localhost';
SET PASSWORD FOR 'BotSchedule_test'@'localhost' = 'BotSchedule_test_pwd';
GRANT ALL PRIVILEGES ON BotSchedule_test_db.* TO 'BotSchedule_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'BotSchedule_test'@'localhost';



  
  -- Create database + user if doesn't exist
  
  --
  -- Table structure for table `cities`
  --
  
DROP TABLE IF EXISTS `January`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
  /*!40101 SET character_set_client = utf8 */;
CREATE TABLE `January` (
    `ID` int NOT NULL AUTO_INCREMENT,
    `Days` VARCHAR(50),
    `Course` VARCHAR(50),
    `Topic` VARCHAR(50),
    `Target` INT,
    `Average` INT,
    `created_at` VARCHAR(50),
    `updated_at` VARCHAR(50),
    PRIMARY KEY(`ID`)
  );
