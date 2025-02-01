import streamlit as st
from text_extractor import TextExctactor

def main():
    """
    Interfaccia Streamlit per caricare un PDF e scaricare il Markdown generato.
    """
    st.title("PDF to Txt Converter")
    st.subheader("Upload a PDF file and download the highlighted text as a txt file")
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    
    if uploaded_file is not None:
        pdf_path = f"{uploaded_file.name}"  # Salva il file temporaneamente
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        output_txt_path = pdf_path.replace(".pdf", ".txt")  # Genera il nome del file di output

        text_extractor = TextExctactor(pdf_path)
        text_extractor.pdf_to_text(output_txt_path)
        
        with open(output_txt_path, "r", encoding="utf-8") as f:
            st.download_button("Download Txt File of highlighted text", f, file_name=output_txt_path)  # Pulsante per scaricare il file

if __name__ == "__main__":
    main()