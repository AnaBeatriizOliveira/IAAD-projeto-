-- Criar Tabela Artistas
CREATE TABLE Artistas (
    id_artista INT PRIMARY KEY,
    artist_name VARCHAR(255)
);



-- Inserir Dados na Tabela Artistas
INSERT INTO Artistas (id_artista, artist_name)
VALUES
    (1, 'Latto'), 
    (2, 'Jung Kook'),
    (3, 'Myke Towers'),
    (4, 'Olivia Rodrigo'),
    (5, 'Taylor Swift'),
    (6, 'Bad Bunny'),
    (7, 'Dave'),
    (8, 'Central Cee'),
    (9, 'Eslabon Armado'), 
    (10, 'Peso Pluma'),
    (11, 'Quevedo'),
    (12, 'Gunna'),
    (13, 'Yng Lvcas');





-- Criar Tabela Musicas
CREATE TABLE Musicas (
    id_musica INT PRIMARY KEY,
    track_name VARCHAR(255),
    released_year INT,
    released_month INT,
    released_day INT,
    bpm INT,
    music_key VARCHAR(255),
    mode VARCHAR(10),
    danceability_percentage DECIMAL(5,2),
    valence_percentage DECIMAL(5,2),
    energy_percentage DECIMAL(5,2),
    acousticness_percentage DECIMAL(5,2),
    instrumentalness_percentage DECIMAL(5,2),
    liveness_percentage DECIMAL(5,2),
    speechiness_percentage DECIMAL(5,2)
);





-- Inserir Dados na Tabela Musicas
INSERT INTO Musicas (id_musica, track_name, released_year, released_month, released_day, bpm, music_key, mode, danceability_percentage, valence_percentage, energy_percentage, acousticness_percentage, instrumentalness_percentage, liveness_percentage, speechiness_percentage)
VALUES
    (1, 'Seven', 2023, 7, 14, 125, 'B', 'Major', 80, 89, 83, 31, 0, 8, 4),
    (2, 'LALA', 2023, 3, 23, 92, 'C#', 'Major', 71, 61, 74, 7, 0, 10, 4),
    (3, 'vampire', 2023, 6, 30, 138, 'F', 'Major', 51, 32, 53, 17, 0, 31, 6),
    (4, 'Cruel Summer', 2019, 8, 23, 170, 'A', 'Major', 55, 58, 72, 11, 0, 11, 15),
    (5, 'WHERE SHE GOES', 2023, 5, 18, 144, 'A', 'Minor', 65, 23, 80, 14, 63, 11, 6),
    (6, 'Sprinter', 2023, 6, 1, 141, 'C#', 'Major', 92, 66, 58, 19, 0, 8, 24),
    (7, 'Ella Baila Sola', 2023, 3, 16, 148, 'F', 'Minor', 67, 83, 76, 48, 0, 8, 3),
    (8, 'Columbia', 2023, 7, 7, 100, 'F', 'Major', 67, 26, 71, 37, 0, 11, 4),
    (9, 'fukumean', 2023, 5, 15, 130, 'C#', 'Minor', 85, 22, 62, 12, 0, 28, 9),
    (10, 'La bebe - Remix', 2023, 3, 17, 170, 'D', 'Minor', 81, 56, 48, 21, 0, 8, 33);



-- Criar Tabela ArtistasMusicas
CREATE TABLE ArtistasMusicas (
    id_relacao INT PRIMARY KEY,
    id_musica INT,
    id_artista INT,
    FOREIGN KEY (id_musica) REFERENCES Musicas(id_musica),
    FOREIGN KEY (id_artista) REFERENCES Artistas(id_artista)
);



-- Inserir Dados na Tabela ArtistasMusicas
INSERT INTO ArtistasMusicas (id_relacao, id_musica, id_artista)
VALUES
    (1, 1, 1),
    (2, 1, 2),
    (3, 2, 3),
    (4, 3, 4),
    (5, 4, 5),
    (6, 5, 6),
    (7, 6, 7),
    (8, 6, 8),
    (9, 7, 9),
    (10, 7, 10),
    (11, 8, 11),
    (12, 9, 12),
    (13, 10, 10),
    (14, 10, 13);


DELIMITER //

CREATE TRIGGER ContagemMusicasArtista
AFTER INSERT ON ArtistasMusicas
FOR EACH ROW
BEGIN
    -- Atualizar a contagem de músicas para o artista
    UPDATE Artistas AS a
    SET num_musicas = (
        SELECT COUNT(*)
        FROM ArtistasMusicas am
        JOIN Musicas m ON am.id_musica = m.id_musica
        WHERE am.id_artista = NEW.id_artista
    )
    WHERE a.id_artista = NEW.id_artista;
END;
//

DELIMITER ;
