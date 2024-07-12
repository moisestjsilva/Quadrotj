import streamlit as st
import os

# Função para salvar o arquivo PDF no diretório correspondente
def save_uploaded_file(uploaded_file, category):
    os.makedirs(os.path.join("uploads", category), exist_ok=True)
    with open(os.path.join("uploads", category, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    return os.path.join("uploads", category, uploaded_file.name)

# Título da aplicação
st.title("Upload e Categorização de PDFs")

# Upload do PDF
uploaded_file = st.file_uploader("Escolha um arquivo PDF", type="pdf")
if uploaded_file is not None:
    category = st.text_input("Digite a categoria para este PDF")
    if category:
        file_path = save_uploaded_file(uploaded_file, category)
        st.success(f"Arquivo {uploaded_file.name} carregado na categoria {category}")

# Listar as categorias disponíveis
if os.path.exists("uploads"):
    categories = os.listdir("uploads")
    if categories:
        selected_category = st.selectbox("Escolha uma categoria", categories)
        if selected_category:
            pdf_files = os.listdir(os.path.join("uploads", selected_category))
            selected_pdf = st.selectbox("Escolha um PDF", pdf_files)
            if selected_pdf:
                file_path = os.path.join("uploads", selected_category, selected_pdf)
                # Mostrar o PDF usando o visualizador embutido
                st.components.v1.iframe(f"file://{file_path}", width=700, height=1000)
                st.download_button(label="Baixar PDF", data=open(file_path, "rb").read(), file_name=selected_pdf, mime="application/pdf")