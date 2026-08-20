
import requests
from bs4 import BeautifulSoup


def fetch_webpage_text(url):
    """
    Download a webpage and return readable text.
    """

    try:
        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        for tag in soup([
            "script",
            "style",
            "nav",
            "footer"
        ]):
            tag.decompose()

        text = soup.get_text(
            separator=" ",
            strip=True
        )

        return text[:12000]

    except requests.RequestException as error:
        return f"Unable to retrieve webpage: {error}"

def fetch_webpage_data(url):
    text = fetch_webpage_text(url)

    return {
        "url": url,
        "content": text
    }


if __name__ == "__main__":
    test_url = "https://www.example.com"

    result = fetch_webpage_text(test_url)

    print("===== WEB RESEARCH TEST =====")
    print(result)
def fetch_multiple_pages(urls):
    results = []

    for url in urls:
        data = fetch_webpage_data(url)
        results.append(data)

    return results