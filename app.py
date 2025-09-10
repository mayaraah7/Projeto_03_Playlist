import streamlit as st

# Nome da pasta que você quer criar
generos = ["Kpop", "Pop", "Eletrónica", "Hip Hop/Rap", "Funk", "MPB", "Sertanejo"]

# Dicionário relacionando gêneros a musicais
musicas_por_generos = { 
    "Kpop": ["BTS", "Aespa", "Blackpink", "Stray Kids", "BabyMonster", "Le Sserafim", "Enhypen", "NewJeans", "Kiss of Life"],
    "Pop": ["The Weeknd", "Lana del rey", "Ariana Grande", "", "", "", "", ""],
    "Fantasia": ["O Senhor dos Anéis", "Harry Potter", "As Crônicas de Nárnia"],
    "Terror": ["It: A Coisa", "O Iluminado", "Drácula"],
    "Terror": ["It: A Coisa", "O Iluminado", "Drácula"],


}               

genero_selecionado = st.sidebar.selectbox("Selecione o gênero:", generos)



# Selectbox para escolher o livro (apenas do gênero selecionado)
if genero_selecionado:
    musica_selecionada = st.sidebar.selectbox(
        "Selecione o Artista:", 
        musicas_por_generos[genero_selecionado]
    )

# Mostrar apenas o livro selecionado
if genero_selecionado and musica_selecionada:
    st.write(f"**Artista Selecionado:** {musica_selecionada}")
    st.write(f"**Gênero:** {genero_selecionado}")
    st.image(f"{musica_selecionada}.png")




