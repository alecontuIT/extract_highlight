import fitz  # PyMuPDF

class TextExctactor:
    def __init__(self, pdf_path):
        self.doc = fitz.open(pdf_path)

    def extract_highlighted_text(self):
        """
        Estrae il testo evidenziato da un file PDF.
        """
        
        highlighted_text = []
        
        for page in self.doc:
            for annot in page.annots():
                if annot.type[0] == 8:  # Controlla se l'annotazione è un highlight
                    text = annot.info.get("content", "").strip()
                    if not text:
                        text = page.get_text("text", clip=annot.rect).strip()  # Estrae il testo all'interno del rettangolo evidenziato
                    if text:
                        highlighted_text.append(text)
        
        return highlighted_text
    
    def pdf_to_text(self, output_txt_path):
        """
        Converte il testo evidenziato in un file di testo.
        """
        highlighted_text = self.extract_highlighted_text()
        
        with open(output_txt_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(highlighted_text)
        
        print(f"Text file saved as {output_txt_path}")