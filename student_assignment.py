from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)
from langchain_community.document_loaders import PyPDFLoader, PyMuPDFLoader

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def print_docs(docs):
    count = 0
    for doc in docs:
        print("----- Doc", count, "begin ------")
        print("**** Page Content ****")
        print(len(doc.page_content))
        print(doc.page_content)
        print("**********************")
        print("===== MetaData ====")
        print(doc.metadata)
        print("===================")
        print("----- Doc", count, "end ------")
        count = count + 1
        print()

def load_with_PyPdf(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return docs

def recursive_split_with_regex():
    q2_pdf = "道路交通管理處罰條例.pdf"
    loader = PyPDFLoader(q2_pdf)
    docs = loader.load()
    text = ""
    for doc in docs:
        text = text + doc.page_content + "\n"
    spliter = RecursiveCharacterTextSplitter(separators=["第 \\d+-?\\d* 條\n", "   第 .+ 章 .+\n"],
                                    chunk_size=0,
                                    chunk_overlap=0,
                                    is_separator_regex=True,
                                    keep_separator=True)
    result = spliter.create_documents([text], metadatas=[{"Example": "HA"}])
    print_docs(result)

def hw02_1(q1_pdf):
    result = load_with_PyPdf(q1_pdf)
    return result[-1]

def hw02_2(q2_pdf):
    loader = PyPDFLoader(q2_pdf)
    docs = loader.load()
    text = ""
    for doc in docs:
        text = text + doc.page_content + "\n"
    spliter = RecursiveCharacterTextSplitter(separators=["第 \\d+-?\\d* 條\n", "   第 .+ 章 .+\n"],
                                    chunk_size=0,
                                    chunk_overlap=0,
                                    is_separator_regex=True,
                                    keep_separator=True)
    result = spliter.create_documents([text], metadatas=[{"Example": "HA"}])
    return len(result)


if __name__ == "__main__":
    # result = hw02_1(q1_pdf)
    # print(result)
    result = hw02_2(q2_pdf)
    print(result)