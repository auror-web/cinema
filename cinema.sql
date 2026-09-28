-- =====================================================================
--  PROGETTO 4 — Cinema "Aurora" (programmazione e biglietti)
--  Database: cinema                                   MySQL 8
-- =====================================================================
--  COME CARICARE QUESTO FILE (va eseguito con l'utente root)
--
--  MySQL Workbench:
--     1. Aprite la connessione "Local instance MySQL80" (utente root)
--     2. File > Open SQL Script...  > scegliete cinema.sql
--     3. Premete il FULMINE (Execute)  e poi aggiornate il pannello Schemas
--
--  Da terminale (Prompt dei comandi):
--     cd "C:\Program Files\MySQL\MySQL Server 8.0\bin"
--     mysql -u root -p < C:\percorso\cinema.sql
--
--  Lo script crea anche l'utente  studente / studente  usato da database.py.
--  NOTA: le date degli spettacoli sono calcolate a partire da OGGI
--  (CURDATE()), così ci sono sempre spettacoli nei prossimi giorni.
--  Se passa più di una settimana, rieseguite lo script.
-- =====================================================================

SET NAMES utf8mb4;

DROP DATABASE IF EXISTS cinema;
CREATE DATABASE cinema CHARACTER SET utf8mb4;
USE cinema;

CREATE USER IF NOT EXISTS 'studente'@'localhost' IDENTIFIED BY 'studente';
GRANT ALL PRIVILEGES ON cinema.* TO 'studente'@'localhost';
FLUSH PRIVILEGES;

-- ---------------------------------------------------------------------
--  TABELLE
-- ---------------------------------------------------------------------
CREATE TABLE film (
    id_film       INT AUTO_INCREMENT PRIMARY KEY,
    titolo        VARCHAR(100) NOT NULL,
    regista       VARCHAR(80)  NOT NULL,
    genere        VARCHAR(30)  NOT NULL,
    durata_min    INT          NOT NULL,
    trama         TEXT,
    locandina_url VARCHAR(255)
);

CREATE TABLE sale (
    id_sala INT AUTO_INCREMENT PRIMARY KEY,
    nome    VARCHAR(30) NOT NULL,
    posti   INT NOT NULL
);

CREATE TABLE spettacoli (
    id_spettacolo INT AUTO_INCREMENT PRIMARY KEY,
    id_film       INT NOT NULL,
    id_sala       INT NOT NULL,
    data_ora      DATETIME NOT NULL,
    prezzo        DECIMAL(5,2) NOT NULL,
    FOREIGN KEY (id_film) REFERENCES film(id_film),
    FOREIGN KEY (id_sala) REFERENCES sale(id_sala)
);

-- Ogni riga è UN biglietto (un posto) venduto
CREATE TABLE biglietti (
    id_biglietto  INT AUTO_INCREMENT PRIMARY KEY,
    id_spettacolo INT NOT NULL,
    data_acquisto DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_spettacolo) REFERENCES spettacoli(id_spettacolo)
);

-- ---------------------------------------------------------------------
--  DATI DI ESEMPIO (film inventati)
-- ---------------------------------------------------------------------
INSERT INTO film (titolo, regista, genere, durata_min, trama, locandina_url) VALUES
('L''ultimo treno per il Sud', 'Chiara Lo Presti', 'Drammatico',   118,
 'Un anziano ferroviere accompagna la nipote in un lungo viaggio tra ricordi e segreti di famiglia.',
 'https://placehold.co/300x450?text=Ultimo+treno'),
('Galassia Zero',             'Marco Venturi',    'Fantascienza', 134,
 'L''equipaggio di una nave mineraria riceve un segnale da un pianeta che non dovrebbe esistere.',
 'https://placehold.co/300x450?text=Galassia+Zero'),
('Il pasticcio',              'Paolo Serra',      'Commedia',      96,
 'Due pasticceri rivali devono preparare insieme la torta per il matrimonio del sindaco.',
 'https://placehold.co/300x450?text=Il+pasticcio'),
('Ombre sul lago',            'Elena Moretti',    'Thriller',     109,
 'Una giornalista indaga sulla scomparsa di un pescatore in un paesino dove tutti mentono.',
 'https://placehold.co/300x450?text=Ombre+sul+lago'),
('Pixel e la foresta magica', 'Studio Lumen',     'Animazione',    88,
 'Un piccolo robot perso nel bosco scopre che gli alberi sanno parlare.',
 'https://placehold.co/300x450?text=Pixel');

INSERT INTO sale (nome, posti) VALUES
('Sala Verde', 120),
('Sala Blu',    80),
('Sala Studio', 10);

-- TIMESTAMP(giorno, ora) costruisce data e ora. CURDATE() + INTERVAL 1 DAY = domani
INSERT INTO spettacoli (id_film, id_sala, data_ora, prezzo) VALUES
(1, 1, TIMESTAMP(CURDATE() + INTERVAL 1 DAY, '18:30:00'), 8.00),   -- 1
(1, 2, TIMESTAMP(CURDATE() + INTERVAL 2 DAY, '21:00:00'), 8.00),   -- 2
(2, 1, TIMESTAMP(CURDATE() + INTERVAL 1 DAY, '21:00:00'), 10.00),  -- 3
(2, 1, TIMESTAMP(CURDATE() + INTERVAL 3 DAY, '21:00:00'), 10.00),  -- 4
(3, 2, TIMESTAMP(CURDATE() + INTERVAL 1 DAY, '20:00:00'), 8.00),   -- 5
(3, 1, TIMESTAMP(CURDATE() + INTERVAL 2 DAY, '18:00:00'), 8.00),   -- 6
(4, 3, TIMESTAMP(CURDATE() + INTERVAL 2 DAY, '22:00:00'), 7.00),   -- 7 quasi esaurito
(5, 2, TIMESTAMP(CURDATE() + INTERVAL 3 DAY, '16:00:00'), 6.50);   -- 8

INSERT INTO biglietti (id_spettacolo) VALUES
(1),(1),(1),(1),
(3),(3),(3),(3),(3),(3),
(5),(5),
(7),(7),(7),(7),(7),(7),(7),(7),(7),
(8),(8),(8);

-- ---------------------------------------------------------------------
--  QUERY DI ESEMPIO
--  Servono solo a vedere i dati e a ricordare la sintassi.
--  NON sono le query del progetto: quelle le dovete scrivere voi,
--  provandole prima qui in Workbench.
-- ---------------------------------------------------------------------

-- 1) Film che durano più di 100 minuti
SELECT titolo, durata_min
FROM film
WHERE durata_min > 100
ORDER BY durata_min DESC;

-- 2) Quanti spettacoli ci sono per ogni prezzo del biglietto (GROUP BY)
SELECT prezzo, COUNT(*) AS numero_spettacoli
FROM spettacoli
GROUP BY prezzo
ORDER BY prezzo;
