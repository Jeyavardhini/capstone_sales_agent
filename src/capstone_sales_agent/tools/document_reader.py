from io import BytesIO

from pypdf import PdfReader


def read_pdf(file_bytes: bytes, max_characters: int = 12000) -> str:
    """Extract text from an uploaded PDF document."""

    if not file_bytes:
        return ""

    reader = PdfReader(BytesIO(file_bytes))
    page_text = []

    for page in reader.pages:
        page_text.append(page.extract_text() or "")

    text = "\n".join(page_text).strip()

    if not text:
        return "No readable text was found in the uploaded PDF."

    return text[:max_characters]