import PyPDF2
import os

#
# reader = PyPDF2.PdfReader("test.pdf")
#
# text = reader.pages[0].extract_text().split()
#
# barcode = text[0]
#
# print(barcode)

directories = os.listdir("files")
print(directories)

for directory in directories:
    files = os.listdir(f"files/{directory}")

    files_without_txt = [x for x in files if ".txt" not in x]

    print(files)
    print(files_without_txt)

    if len(files) != len(files_without_txt):
        continue

    for file in files:
        reader = PyPDF2.PdfReader(f"files/{directory}/{file}")
        text = reader.pages[0].extract_text().split()

        barcode_number = text[0]
        vendor_code = text[8]
        size = text[13]

        with open(f"files/{directory}/{vendor_code}.txt", "a") as f:
            f.write(f"{size} - {barcode_number}\n")