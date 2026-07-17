

# creating a function that takes the PDF file path and returns its text
import pymupdf


def extract_text(pdf_path: str) -> str:
    """
    Extract all text from a PDF file.
    """
    doc = pymupdf.open(pdf_path)

    print(f"Number of pages: {doc.page_count}")

    all_text = ""

    for page in doc:
        all_text += page.get_text()

    doc.close()

    return all_text