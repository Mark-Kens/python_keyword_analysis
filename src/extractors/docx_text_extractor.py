from docx import Document
def extract_text_from_docx(docx_file_path):
    document = Document(docx_file_path)
    paragraphs = [paragraph.text for paragraph in document.paragraphs if paragraph.text]
    return "\n".join(paragraphs)