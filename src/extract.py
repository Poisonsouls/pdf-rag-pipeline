import pymupdf
from clean import clean_text

#creating a function that 1. take the pdf file path 2. return the text that in the file
def extract_text(pdf_path: str) -> str:
    """
    Extract all text from a PDF file.
    """
    doc = pymupdf.open(pdf_path)

    print(f"Number of pages: {doc.page_count}")

    all_text = ""

    for page in doc:
        all_text += page.get_text() #extract the text from each page and save it in the variable

    doc.close()

    return all_text


if __name__ == "__main__":
    text = extract_text("data/fannie_mae.pdf")
    cleaned_text = clean_text(text)

    print("\nFirst 1000 characters:\n")
    print(cleaned_text[:2000])