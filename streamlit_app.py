import streamlit as st
from PyPDF2 import PdfFileReader
import io

# Função para exibir o PDF
def display_pdf(file):
    with io.BytesIO(file.read()) as f:
        pdf = PdfFileReader(f)
        st.write(f"Total de páginas: {pdf.getNumPages()}")
        st.write("Exibindo a primeira página do PDF:")
        st.write(f"Conteúdo da primeira página: {pdf.getPage(0).extractText()}")

# Título da aplicação
st.title("Upload e Categorização de PDFs")

# Dicionário para armazenar os arquivos PDFs categorizados
pdf_files = {}

# Upload do PDF
uploaded_file = st.file_uploader("Escolha um arquivo PDF", type="pdf")
if uploaded_file is not None:
    categories = st.text_input("Digite a categoria para este PDF")
    if categories:
        if categories not in pdf_files:
            pdf_files[categories] = []
        pdf_files[categories].append(uploaded_file)
        st.success(f"Arquivo {uploaded_file.name} carregado na categoria {categories}")

# Exibir categorias no cabeçalho
if pdf_files:
    selected_category = st.selectbox("Escolha uma categoria", list(pdf_files.keys()))
    if selected_category:
        st.write(f"Arquivos na categoria {selected_category}:")
        for pdf_file in pdf_files[selected_category]:
            st.write(pdf_file.name)
            display_pdf(pdf_file)