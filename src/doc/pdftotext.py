import pdfplumber
from typing_extensions import Literal

pdf = pdfplumber.open('D://invite6.pdf')


text = ''

for page_num in range(0, len(pdf.pages)):
    page = pdf.pages[page_num]

    text = text + page.extract_text()

    print(text)
    pdf.close()
