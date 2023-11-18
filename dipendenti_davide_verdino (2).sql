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
-- Struttura della tabella `dipendenti_davide_verdino`
--

CREATE TABLE `dipendenti_davide_verdino` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `cognome` varchar(100) NOT NULL,
  `posizione lavorativa` varchar(100) NOT NULL,
  `data di assunzione` date NOT NULL,
  `telefono` varchar(100) NOT NULL,
  `indirizzo` varchar(1024) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `dipendenti_davide_verdino`
--

INSERT INTO `dipendenti_davide_verdino` (`id`, `nome`, `cognome`, `posizione lavorativa`, `data di assunzione`, `telefono`, `indirizzo`) VALUES
(1, 'Gordon', 'Freeman', 'fisico_teorico', '1998-07-12', '366 670 1234', 'black_mesa_12'),
(2, 'Michele', 'Salvemini', 'rapper', '2006-03-23', '123 444 5512', 'Corso_Cavour_1'),
(3, 'Laszlo', 'Martinez', 'ingegnere_informatico', '2004-11-16', '123 456 7274', 'city_17'),
(4, 'Ajay', 'Ghal', 'fattorino', '2023-10-26', '333 443 7274', 'via della costituzione 6'),
(5, 'Gennaro', 'Caruso', 'magazziniere', '2004-04-16', '342 411 5105', 'Viale della liberta 6'),
(6, 'Jack', 'White', 'ingegnere_informatico', '2011-09-14', '340 676 1234', 'Via della pace 5');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `dipendenti_davide_verdino`
--
ALTER TABLE `dipendenti_davide_verdino`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `dipendenti_davide_verdino`
--
ALTER TABLE `dipendenti_davide_verdino`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
