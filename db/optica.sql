-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  sam. 27 juil. 2019 à 17:28
-- Version du serveur :  5.7.21
-- Version de PHP :  5.6.35

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `optica`
--

-- --------------------------------------------------------

--
-- Structure de la table `achat`
--

DROP TABLE IF EXISTS `achat`;
CREATE TABLE IF NOT EXISTS `achat` (
  `Id_Produit` varchar(50) NOT NULL,
  `Nombre_Produit` int(11) NOT NULL,
  `Prix_Unitaire` float NOT NULL,
  `Nom_Produit` varchar(50) NOT NULL,
  `Numero_Commande` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `client`
--

DROP TABLE IF EXISTS `client`;
CREATE TABLE IF NOT EXISTS `client` (
  `Id_Client` int(11) NOT NULL AUTO_INCREMENT,
  `Nom_Client` varchar(50) NOT NULL,
  `Prenom_Client` varchar(250) DEFAULT NULL,
  `Numero_Commande` varchar(250) NOT NULL,
  PRIMARY KEY (`Id_Client`),
  UNIQUE KEY `Numero_Commande` (`Numero_Commande`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `commande`
--

DROP TABLE IF EXISTS `commande`;
CREATE TABLE IF NOT EXISTS `commande` (
  `Numero_Commande` varchar(255) NOT NULL,
  `Id_Client` int(11) NOT NULL,
  `Date_Commande` datetime NOT NULL,
  `Date_Livraison` datetime DEFAULT NULL,
  `User_Cmd` varchar(30) NOT NULL,
  `User_Livr` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Numero_Commande`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `monture`
--

DROP TABLE IF EXISTS `monture`;
CREATE TABLE IF NOT EXISTS `monture` (
  `Ref` varchar(50) NOT NULL,
  `Couleur` varchar(50) NOT NULL,
  `Forme` varchar(50) NOT NULL,
  `Nombre_Stock` int(11) NOT NULL,
  `Prix_Achat` float NOT NULL,
  `Prix_Vente` float NOT NULL,
  PRIMARY KEY (`Ref`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `personnel`
--

DROP TABLE IF EXISTS `personnel`;
CREATE TABLE IF NOT EXISTS `personnel` (
  `User` varchar(20) NOT NULL,
  `Nom` varchar(50) NOT NULL,
  `Prenom` varchar(50) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Admin` tinyint(1) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `personnel`
--

INSERT INTO `personnel` (`User`, `Nom`, `Prenom`, `Password`, `Admin`) VALUES
('gaetan1903', 'Bakary', 'Gaetan Jonathan', 'c16bac42f30d5063f6671b27125938b43dc48ab4', 1),
('ld', 'Manankoraisina', 'Landry Daniel', '9cf95dacd226dcf43da376cdb6cbba7035218921', 0);

-- --------------------------------------------------------

--
-- Structure de la table `verre`
--

DROP TABLE IF EXISTS `verre`;
CREATE TABLE IF NOT EXISTS `verre` (
  `Type_Verre` varchar(30) NOT NULL,
  `Traiter` varchar(30) NOT NULL,
  `Degre` varchar(30) NOT NULL,
  `Nombre_Stock` int(11) NOT NULL,
  `Prix_Achat` float NOT NULL,
  `Prix_Vente` float NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
