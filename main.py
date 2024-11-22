import streamlit as st
from app.gcloud_utils import upload_file_to_gcs
from app.pdf_processor import process_pdf_to_text
from app.rag_engine import query_with_rag, query_without_rag

# Titre de l'application
st.title("Chat RAG avec Google Cloud")

# Initialiser les variables globales
cloud_file_name = None

# Upload d'un fichier PDF
uploaded_file = st.file_uploader("Upload un fichier PDF", type="pdf")

if uploaded_file:
    # Nom du fichier PDF à conserver
    cloud_file_name = uploaded_file.name
    
    # Upload du fichier PDF original vers Google Cloud Storage
    gcs_url = upload_file_to_gcs(uploaded_file, cloud_file_name)
    st.success(f"Fichier PDF uploadé sur Google Cloud Storage : {gcs_url}")
    
    # Convertir le PDF en texte pour le traitement local
    text_file = process_pdf_to_text(uploaded_file)
    st.success("Fichier converti en texte pour la recherche.")

# Entrée utilisateur
user_query = st.text_input("Posez une question ici :")

# Slider pour régler la température
temperature = st.slider("Réglez la température du LLM", min_value=0.0, max_value=1.0, step=0.1, value=0.5)

if user_query:
    # Afficher les réponses sans RAG
    st.subheader("Résultat sans RAG")
    response_no_rag = query_without_rag(user_query, temperature)
    st.write(response_no_rag)

    # Afficher les réponses avec RAG
    st.subheader("Résultat avec RAG")
    if cloud_file_name:
        response_rag = query_with_rag(user_query, temperature, cloud_file_name)
        st.write(response_rag)
    else:
        st.warning("Veuillez d'abord uploader un fichier PDF pour utiliser le RAG.")
