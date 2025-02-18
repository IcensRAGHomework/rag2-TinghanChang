from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)
from langchain_community.document_loaders import PyPDFLoader, PyMuPDFLoader

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"

def load_with_PyPdf(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return docs[-1]

def hw02_1(q1_pdf):
    result = load_with_PyPdf(q1_pdf)
    return result

def hw02_2(q2_pdf):
    pass


if __name__ == "__main__":
    result = hw02_1(q1_pdf)
    print(result)