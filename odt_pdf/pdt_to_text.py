# pdf to text
from pypdf import PdfReader
import re
from rich import print


def pdf_to_text(input_file: str) -> str:
    """
    Extracts the text from a PDF file and returns it as a string.

    Args:
        input_file (str): The path to the input PDF file.
    Returns:
        str: The extracted text from the PDF file.
    """

    reader = PdfReader(input_file)
    text = " "
    for page in reader.pages:
        text += page.extract_text()

    # print(text)

    text = text.replace("\n", " ")

    pattern = r"(\d+)\.(\w+(?:\s\w+)?):\s*(.*?)(?=\s\d+\.\w+|$)"
    matches = re.findall(pattern, text)

    attributes = {}
    for match in matches:
        key = match[1]
        value = match[2].strip()  # Remove leading/trailing whitespaces
        # If the value starts with "-", consider only the "-"
        if value.startswith("-"):
            value = "-"
        attributes[key] = value
    print(attributes)
    return text


if __name__ == "__main__":
    text = pdf_to_text("11099792_RELINT.pdf")
