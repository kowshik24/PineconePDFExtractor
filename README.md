# PineconePDFExtractor

PineconePDFExtractor is a Python library for extracting text from PDF files for pinecone.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PineconePDFExtractor.

```bash
pip install PineconePDFExtractor
```

## Check the latest version here:
https://pypi.org/project/PineconePDFExtractor/


## Usage

```python
from PineconePDFExtractor import PdfProcessor

# Create a PineconePDFExtractor instance with a batch size of 200
extractor = PineconePDFExtractor(200)

# Process a list of PDF files
result = extractor.process_files(['file1.pdf', 'file2.pdf'])

# The result is a dictionary with the batch size and a list of documents
# Each document is a dictionary with the id (file name without extension), metadata (number of pages), source (file path), and text (extracted text)

## Example result
# {
#   'batch_size': 200,
#   'documents': [
#     {
#       'id': 'file1',
#       'metadata': {
#         'pages': 1
#       },
#       'source': 'file1.pdf',
#       'text': 'This is the extracted text from file1.pdf'
#     },
#     {
#       'id': 'file2',
#       'metadata': {
#         'pages': 2
#       },
#       'source': 'file2.pdf',
#       'text': 'This is the extracted text from file2.pdf'
#     }
#   ]
# }