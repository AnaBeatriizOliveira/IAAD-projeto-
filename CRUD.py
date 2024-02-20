import streamlit as st
import mysql.connector

# Função para conectar ao banco de dados MySQL
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database=""
    )

# Operação CREATE (Adicionar Artista)
def add_artist(artist_name):
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO Artistas (artist_name) VALUES (%s)", (artist_name,))
        connection.commit()
        st.success("Artista adicionado com sucesso!")
    except Exception as e:
        st.error(f"Erro ao adicionar artista: {e}")
    finally:
        cursor.close()
        connection.close()

# Operação READ (Listar Artistas)
def list_artists(artist_name_filter=""):
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        if artist_name_filter:
            cursor.execute("SELECT id_artista, artist_name, num_musicas FROM Artistas WHERE artist_name LIKE %s", ('%' + artist_name_filter + '%',))
        else:
            cursor.execute("SELECT id_artista, artist_name, num_musicas FROM Artistas")
        artists = cursor.fetchall()

        st.header("Lista de Artistas:")
        for artist in artists:
            st.write(f"ID: {artist[0]}, Nome: {artist[1]}, Número de Músicas: {artist[2]}")
    except Exception as e:
        st.error(f"Erro ao listar artistas: {e}")
    finally:
        cursor.close()
        connection.close()


# Operação UPDATE (Atualizar Nome de Artista)
def update_artist_name(artist_id, new_name):
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        cursor.execute("UPDATE Artistas SET artist_name = %s WHERE id_artista = %s", (new_name, artist_id))
        connection.commit()
        st.success("Nome do artista atualizado com sucesso!")
    except Exception as e:
        st.error(f"Erro ao atualizar nome do artista: {e}")
    finally:
        cursor.close()
        connection.close()

# Operação DELETE (Remover Artista)
def delete_artist(artist_id):
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        # Remover todas as associações do artista
        cursor.execute("DELETE FROM ArtistasMusicas WHERE id_artista = %s", (artist_id,))
        connection.commit()

        # Remover o artista
        cursor.execute("DELETE FROM Artistas WHERE id_artista = %s", (artist_id,))
        connection.commit()
        st.success("Artista removido com sucesso!")
    except Exception as e:
        st.error(f"Erro ao remover artista: {e}")
    finally:
        cursor.close()
        connection.close()

# Operação CREATE (Adicionar Música)
def add_song(track_name, released_year, released_month, released_day, bpm, music_key, mode,
             danceability_percentage, valence_percentage, energy_percentage,
             acousticness_percentage, instrumentalness_percentage, liveness_percentage, speechiness_percentage):
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO Musicas (track_name, released_year, released_month, released_day, bpm, music_key, mode, "
                       "danceability_percentage, valence_percentage, energy_percentage, acousticness_percentage, "
                       "instrumentalness_percentage, liveness_percentage, speechiness_percentage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (track_name, released_year, released_month, released_day, bpm, music_key, mode,
                        danceability_percentage, valence_percentage, energy_percentage,
                        acousticness_percentage, instrumentalness_percentage, liveness_percentage, speechiness_percentage))
        connection.commit()
        st.success("Música adicionada com sucesso!")
    except Exception as e:
        st.error(f"Erro ao adicionar música: {e}")
    finally:
        cursor.close()
        connection.close()

# Operação READ (Listar Músicas)
def list_songs(track_name_filter=""):
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        if track_name_filter:
            cursor.execute("SELECT * FROM Musicas WHERE track_name LIKE %s", ('%' + track_name_filter + '%',))
        else:
            cursor.execute("SELECT * FROM Musicas")
        songs = cursor.fetchall()

        st.header("Lista de Músicas:")
        for song in songs:
            st.write(f"ID: {song[0]}, Nome: {song[1]}, Ano: {song[2]}, BPM: {song[5]}")
    except Exception as e:
        st.error(f"Erro ao listar músicas: {e}")
    finally:
        cursor.close()
        connection.close()

# Operação UPDATE (Atualizar Nome de Música)
def update_song_name(id_musica, new_name):
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        cursor.execute("UPDATE Musicas SET track_name = %s WHERE id_musica = %s", (new_name, id_musica))
        connection.commit()
        st.success("Nome da música atualizado com sucesso!")
    except Exception as e:
        st.error(f"Erro ao atualizar nome da música: {e}")
    finally:
        cursor.close()
        connection.close()

# Operação DELETE (Remover Música)
def delete_song(id_musica):
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        # Remover todas as associações da música
        cursor.execute("DELETE FROM ArtistasMusicas WHERE id_musica = %s", (id_musica,))
        connection.commit()

        # Remover a música
        cursor.execute("DELETE FROM Musicas WHERE id_musica = %s", (id_musica,))
        connection.commit()
        st.success("Música removida com sucesso!")
    except Exception as e:
        st.error(f"Erro ao remover música: {e}")
    finally:
        cursor.close()
        connection.close()

# Operação CREATE (Associar Artista a Música)
def associate_artist_to_song(id_musica, id_artista):
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO ArtistasMusicas (id_musica, id_artista) VALUES (%s, %s)", (id_musica, id_artista))
        connection.commit()
        st.success("Associação entre artista e música criada com sucesso!")

        list_artists()

    except Exception as e:
        st.error(f"Erro ao associar artista à música: {e}")
    finally:
        cursor.close()
        connection.close()


# Operação READ (Listar Associações Artista-Música)
def list_artist_song_associations():
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM ArtistasMusicas")
        associations = cursor.fetchall()

        st.header("Lista de Associações Artista-Música:")
        for association in associations:
            st.write(f"ID Relação: {association[0]}, ID Música: {association[1]}, ID Artista: {association[2]}")
    except Exception as e:
        st.error(f"Erro ao listar associações artista-música: {e}")
    finally:
        cursor.close()
        connection.close()

# Operação DELETE (Desassociar Artista de Música)
def disassociate_artist_from_song(id_relacao):
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM ArtistasMusicas WHERE id_relacao = %s", (id_relacao,))
        connection.commit()
        st.success("Associação entre artista e música removida com sucesso!")
    except Exception as e:
        st.error(f"Erro ao desassociar artista de música: {e}")
    finally:
        cursor.close()
        connection.close()

def list_artist_song_associations(song_filter="", artist_filter="", id_filter=""):
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        query = "SELECT * FROM ArtistasMusicas WHERE 1=1"
        params = []

        if song_filter:
            query += " AND id_musica = %s"
            params.append(song_filter)
        if artist_filter:
            query += " AND id_artista = %s"
            params.append(artist_filter)
        if id_filter:
            query += " AND id_relacao = %s"
            params.append(id_filter)

        cursor.execute(query, params)
        associations = cursor.fetchall()

        st.header("Lista de Associações Artista-Música:")
        for association in associations:
            st.write(f"ID Relação: {association[0]}, ID Música: {association[1]}, ID Artista: {association[2]}")
    except Exception as e:
        st.error(f"Erro ao listar associações artista-música: {e}")
    finally:
        cursor.close()
        connection.close()


# Interface gráfica com Streamlit
def main():
    st.title("Sistema de Gerenciamento SpotifyDB")

    # Operação CREATE
    st.header("Adicionar Artista:")
    artist_name = st.text_input("Nome do Artista:")
    if st.button("Adicionar Artista"):
        add_artist(artist_name)

    # Operação READ
    st.header("Listar Artistas:")
    artist_name_filter = st.text_input("Filtrar por Nome de Artista:")
    list_artists(artist_name_filter)

    # Operação UPDATE
    st.header("Atualizar Nome de Artista:")
    artist_id_update = st.number_input("ID do Artista a ser atualizado:")
    new_name_update = st.text_input("Novo Nome:")
    if st.button("Atualizar Nome"):
        update_artist_name(artist_id_update, new_name_update)

    # Operação DELETE
    st.header("Remover Artista:")
    artist_id_delete = st.number_input("ID do Artista a ser removido:")
    if st.button("Remover Artista"):
        delete_artist(artist_id_delete)

    # Operação CREATE (Adicionar Música)
    st.header("Adicionar Música:")
    track_name = st.text_input("Nome da Música:")
    released_year = st.number_input("Ano de Lançamento:")
    released_month = st.number_input("Mês de Lançamento:", 1, 12)
    released_day = st.number_input("Dia de Lançamento:", 1, 31)
    bpm = st.number_input("BPM:")
    music_key = st.text_input("Music_Key:")
    mode = st.number_input("Mode:")
    danceability_percentage = st.number_input("Danceability (%):", 0.0, 100.0)
    valence_percentage = st.number_input("Valence (%):", 0.0, 100.0)
    energy_percentage = st.number_input("Energy (%):", 0.0, 100.0)
    acousticness_percentage = st.number_input("Acousticness (%):", 0.0, 100.0)
    instrumentalness_percentage = st.number_input("Instrumentalness (%):", 0.0, 100.0)
    liveness_percentage = st.number_input("Liveness (%):", 0.0, 100.0)
    speechiness_percentage = st.number_input("Speechiness (%):", 0.0, 100.0)
    if st.button("Adicionar Música"):
        add_song(track_name, released_year, released_month, released_day, bpm, music_key, mode,
                 danceability_percentage, valence_percentage, energy_percentage,
                 acousticness_percentage, instrumentalness_percentage, liveness_percentage, speechiness_percentage)

    # Operação READ (Listar Músicas)
    st.header("Listar Músicas:")
    track_name_filter = st.text_input("Filtrar por Nome de Música:")
    list_songs(track_name_filter)

    # Operação UPDATE (Atualizar Nome de Música)
    st.header("Atualizar Nome de Música:")
    song_id_update = st.number_input("ID da Música a ser atualizada:")
    new_name_song_update = st.text_input("Novo Nome da Música:")
    if st.button("Atualizar Nome da Música"):
        update_song_name(song_id_update, new_name_song_update)

    # Operação DELETE (Remover Música)
    st.header("Remover Música:")
    song_id_delete = st.number_input("ID da Música a ser removida:")
    if st.button("Remover Música"):
        delete_song(song_id_delete)

    # Operação CREATE (Associar Artista a Música)
    st.header("Associar Artista a Música:")
    artist_song_id = st.number_input("ID da Música:")
    artist_id_associate = st.number_input("ID do Artista:")
    if st.button("Associar Artista a Música"):
        associate_artist_to_song(artist_song_id, artist_id_associate)

    st.header("Listar Associações Artista-Música:")
    song_filter = st.text_input("Filtrar por ID da Música:")
    artist_filter = st.text_input("Filtrar por ID do Artista:")
    id_filter = st.text_input("Filtrar por ID da Relação:")
    list_artist_song_associations(song_filter, artist_filter, id_filter)

    # Operação DELETE (Desassociar Artista de Música)
    st.header("Desassociar Artista de Música:")
    association_id_delete = st.number_input("ID da Associação a ser removida:")
    if st.button("Desassociar Artista de Música"):
        disassociate_artist_from_song(association_id_delete)

if _name_ == "_main_":
    main()