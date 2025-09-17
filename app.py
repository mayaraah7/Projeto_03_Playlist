import streamlit as st

# Nome da pasta que você quer criar
generos = ["Kpop", "Pop", "Hip Hop/Rap", "Trap", "Funk", "Eletronica", "MPB", "Sertanejo"]

# Dicionário relacionando gêneros a musicais
musicas_por_generos = { 
    "Kpop": ["BTS", "Aespa", "Blackpink", "Stray Kids", "BabyMonster", "Le Sserafim", "Enhypen"],
    "Pop": ["The Weeknd", "Lana del rey", "Ariana Grande", "Taylor Swift", "Billie Eilish", "Fifth Harmony", "Dua Lipa"],
    "Hip Hop/Rap": ["Eminem", "50 Cent", "B2K", "Rihanna", "Beyonce", "Ciara", "Cassie"],
    "Trap": ["Veigh", "Yunk Vino","Kendrick Lamar", "A$AP Rocky"],
    "Funk": ["Kevin", "Livinho", "Kevinho", "Jerry Smith"],
    "Eletronica": ["SNOW STRIPPERS", "CHRYSTAL"],
    "MPB": ["Legião Urbana", "Ari", "Acústico 1Kilo"],
    "Sertanejo": ["Marília Mendonça", "Cristiano Araújo", "Luan Santana"]



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





