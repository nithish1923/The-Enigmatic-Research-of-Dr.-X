import os
import docx
import pandas as pd
from PyPDF2 import PdfReader

def extract_docx_text(path):
    doc = docx.Document(path)
    return '\n'.join([para.text for para in doc.paragraphs])

def extract_pdf_text(path):
    reader = PdfReader(path)
    all_text = ""
    for page_num, page in enumerate(reader.pages):
        try:
            text = page.extract_text()
            if text:
                all_text += f"\n[Page {page_num+1}]\n{text}"
        except Exception:
            continue
    return all_text

def extract_excel_text(path):
    dfs = pd.read_excel(path, sheet_name=None)
    return '\n'.join([df.to_string(index=False) for df in dfs.values()])

def extract_csv_text(path):
    df = pd.read_csv(path)
    return df.to_string(index=False)

def load_text_from_file(path):
    ext = os.path.splitext(path)[-1].lower()
    if ext == '.pdf':
        return extract_pdf_text(path)
    elif ext == '.docx':
        return extract_docx_text(path)
    elif ext in ['.xlsx', '.xls', '.xlsm']:
        return extract_excel_text(path)
    elif ext == '.csv':
        return extract_csv_text(path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")
