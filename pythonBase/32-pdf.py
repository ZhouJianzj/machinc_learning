# 对pdf的操作
import pdfplumber as pfdTool

pdf = pfdTool.open("D:\C-文档\zhoujian.pdf")
for page in pdf.pages:
    print(page, type(page))
    print(page.extract_text())
    print(page.page_number)
