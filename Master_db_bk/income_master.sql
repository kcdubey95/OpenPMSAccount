-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Aug 25, 2024 at 06:39 PM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `prabhudas_lilladher`
--

-- --------------------------------------------------------

--
-- Table structure for table `income_master`
--

DROP TABLE IF EXISTS `income_master`;
CREATE TABLE IF NOT EXISTS `income_master` (
  `id` int NOT NULL AUTO_INCREMENT,
  `income_rang` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `income_rang` (`income_rang`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `income_master`
--

INSERT INTO `income_master` (`id`, `income_rang`) VALUES
(1, '1 To 7 Lakh'),
(2, '7 To 10 Lakh'),
(3, '10 Lakh And Above');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
