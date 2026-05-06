import pdfplumber
def extract_text_from_pdf(pdf_file_path):
    extracted_pages = []
    with pdfplumber.open(pdf_file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                extracted_pages.append(page_text)
    return "\n".join(extracted_pages)
