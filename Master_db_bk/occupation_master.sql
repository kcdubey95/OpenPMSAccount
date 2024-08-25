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
-- Table structure for table `occupation_master`
--

DROP TABLE IF EXISTS `occupation_master`;
CREATE TABLE IF NOT EXISTS `occupation_master` (
  `id` int NOT NULL AUTO_INCREMENT,
  `occupation_name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `occupation_name` (`occupation_name`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `occupation_master`
--

INSERT INTO `occupation_master` (`id`, `occupation_name`) VALUES
(1, 'Business'),
(2, 'Private Sector'),
(3, 'Government'),
(4, 'Other');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
