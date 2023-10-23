import PyPDF2
import os

directories = os.listdir("files")

for directory in directories:
    files = os.listdir(f"files/{directory}")

    files_without_txt = [x for x in files if ".txt" not in x]

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
