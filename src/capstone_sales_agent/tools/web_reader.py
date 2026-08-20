import requests
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": "Mozilla/5.0 SalesAssistantStudentProject/1.0"
}


def read_webpage(url: str, max_characters: int = 15000) -> str:
    """Download a public webpage and return readable text."""

    if not url.startswith(("http://", "https://")):
        raise ValueError("The URL must begin with http:// or https://")

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=20,
        )
        response.raise_for_status()
    except requests.RequestException as error:
        return f"Unable to retrieve {url}: {error}"

    soup = BeautifulSoup(response.text, "html.parser")

    for element in soup(
        ["script", "style", "nav", "footer", "form", "noscript"]
    ):
        element.decompose()

    text = " ".join(soup.stripped_strings)

    if not text:
        return f"No readable information was found at {url}."

    return text[:max_characters]
