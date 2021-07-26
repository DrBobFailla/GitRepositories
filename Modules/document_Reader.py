import PyPDF2
from striprtf.striprtf import rtf_to_text


def read_pdf(docObject):
    text = ''
    for page_num in range(docObject.getNumPages()):
        page = docObject.getPage(page_num)
        text += page.extractText()
    return text


def read_rtf_doc(docObject):
    text = ''
    with open(docObject, 'r') as file:
        text = file.read()
    return rtf_to_text(text)


def read_word_doc(docObject):
    text = ''
    for para in docObject.paragraphs:
        text += para.text
    return str(text)
