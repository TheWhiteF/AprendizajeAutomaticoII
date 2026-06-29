import os
import streamlit as st
from dotenv import load_dotenv

from rag_pipeline import index_pdf, search_context
from llm_client import generate_answer

load_dotenv()

st.set_page_config(
    page_title="Asistente RAG de Estudio",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Asistente Inteligente de Estudio con RAG")

st.write("""
Sube tus apuntes en PDF y haz preguntas sobre ellos.
El sistema buscará la información relevante y generará una respuesta usando IA generativa.
""")

os.makedirs("data/documentos", exist_ok=True)

st.sidebar.header("1. Subir documentos")

uploaded_file = st.sidebar.file_uploader(
    "Sube un PDF",
    type=["pdf"]
)

if uploaded_file is not None:
    file_path = os.path.join("data/documentos", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.sidebar.success(f"Archivo guardado: {uploaded_file.name}")

    if st.sidebar.button("Indexar documento"):
        with st.spinner("Indexando documento..."):
            num_chunks = index_pdf(file_path)

        st.sidebar.success(f"Documento indexado en {num_chunks} fragmentos.")

st.header("2. Preguntar al asistente")

question = st.text_input("Escribe tu pregunta:")

if st.button("Responder"):
    if not question:
        st.warning("Escribe una pregunta primero.")
    else:
        with st.spinner("Buscando información relevante..."):
            context, sources = search_context(question)

        with st.spinner("Generando respuesta con el LLM..."):
            answer = generate_answer(question, context)

        st.subheader("Respuesta")
        st.write(answer)

        st.subheader("Fuentes utilizadas")
        for source in sources:
            st.write(f"- {source}")