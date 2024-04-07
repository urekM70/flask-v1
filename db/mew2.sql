-- --------------------------------------------------------
-- Strežnik:                     127.0.0.1
-- Verzija strežnika:            10.4.24-MariaDB - mariadb.org binary distribution
-- Operacijski sistem strežnika: Win64
-- HeidiSQL Različica:           12.5.0.6677
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for flask_proj
DROP DATABASE IF EXISTS `flask_proj`;
CREATE DATABASE IF NOT EXISTS `flask_proj` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `flask_proj`;

-- Dumping structure for tabela flask_proj.tasks
DROP TABLE IF EXISTS `tasks`;
CREATE TABLE IF NOT EXISTS `tasks` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `task` text NOT NULL,
  `UserID` int(11) NOT NULL DEFAULT 0,
  `TimeAdded` datetime NOT NULL DEFAULT current_timestamp(),
  `Stolpec 5` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Data exporting was unselected.

-- Dumping structure for tabela flask_proj.uporabniki
DROP TABLE IF EXISTS `uporabniki`;
CREATE TABLE IF NOT EXISTS `uporabniki` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(15) NOT NULL,
  `passwd` varchar(16) NOT NULL,
  `time` datetime DEFAULT current_timestamp(),
  `IPCheckLogin` int(1) DEFAULT 0,
  `IP` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4;

-- Data exporting was unselected.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
