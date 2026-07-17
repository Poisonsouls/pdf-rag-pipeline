#a library in paython called "Regular Expressions"
#helps in searching inside the texts and edit it
import re

# a function that takes a raw text and return it clean
def clean_text(text: str) -> str:
    """
    Clean extracted text before chunking.
    """

 # Remove standalone page numbers
    text = re.sub(r"\n\s*\d+\s*\n", "\n", text)

    # Remove repeated spaces 
    text = re.sub(r"[ \t]+", " ", text)

    # Remove repeated blank lines
    text = re.sub(r"\n{2,}", "\n\n", text)

    # Remove extra spaces,lines
    text = re.sub(r"\s+", " ", text)

  
 # Remove extra spaces again
    text = re.sub(r"\s+", " ", text)

    # Remove leading/trailing spaces (the start and the end of the text)
    text = text.strip()

    return text
