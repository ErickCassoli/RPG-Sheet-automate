from PyPDF2 import PdfReader

def read_pdf(file_path: str) -> list:
    reader = PdfReader(file_path)
    content = [page.extract_text() for page in reader.pages]
    return content
