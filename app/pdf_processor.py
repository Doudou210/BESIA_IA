from PyPDF2 import PdfReader

def process_pdf_to_text(uploaded_file):
    """
    Convertit un fichier PDF en texte brut.
    """
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    
    # Sauvegarder le texte dans un fichier temporaire
    with open("processed_text.txt", "w", encoding="utf-8") as f:
        f.write(text)
    return "processed_text.txt"
