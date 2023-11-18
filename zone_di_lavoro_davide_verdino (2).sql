-- phpMyAdmin SQL Dump
-- version 4.6.6deb5ubuntu0.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Creato il: Nov 17, 2023 alle 10:51
-- Versione del server: 5.7.40-0ubuntu0.18.04.1
-- Versione PHP: 7.2.24-0ubuntu0.18.04.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5ATepsit`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `zone_di_lavoro_davide_verdino`
--

CREATE TABLE `zone_di_lavoro_davide_verdino` (
  `id_zona` int(11) NOT NULL,
  `nome_zona` varchar(100) NOT NULL,
  `numero_clienti` int(100) NOT NULL,
  `id_dipendente` varchar(100) NOT NULL,
  `orario_lavoro` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `zone_di_lavoro_davide_verdino`
--

INSERT INTO `zone_di_lavoro_davide_verdino` (`id_zona`, `nome_zona`, `numero_clienti`, `id_dipendente`, `orario_lavoro`) VALUES
(1, 'magazzino', 20, '2c7d', '8:00-14:00 15:00-17:00'),
(3, 'officina', 4, '2', '8:00-13:00'),
(4, 'ufficio acquisti', 10, 'sa5', '5:00-14:00');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `zone_di_lavoro_davide_verdino`
--
ALTER TABLE `zone_di_lavoro_davide_verdino`
  ADD PRIMARY KEY (`id_zona`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `zone_di_lavoro_davide_verdino`
--
ALTER TABLE `zone_di_lavoro_davide_verdino`
  MODIFY `id_zona` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
