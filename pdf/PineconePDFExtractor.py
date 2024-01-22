from typing import List
import PyPDF2

class PdfProcessor:
    def __init__(self, batch_size: int = 200):
        self.batch_size = batch_size

    def process_files(self, files: List[str]) -> dict:
        documents = []
        for file_path in files:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                number_of_pages = len(pdf_reader.pages)
                text = ""
                for page in range(number_of_pages):
                    page_text = pdf_reader.pages[page].extract_text()
                    # Ensure the text is UTF-8 encoded
                    page_text = page_text.encode('utf-8', errors='ignore').decode('utf-8')
                    text += page_text

                documents.append({
                "id": file_path.split('/')[-1].split('.')[0],
                "metadata": {"number_of_pages": number_of_pages},
                "source": file_path,
                "text": text
                })
        
        return {
        "batch_size": self.batch_size,
        "documents": documents
        }