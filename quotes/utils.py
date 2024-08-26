import requests

def get_random_quote():
    url = "https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json()
        quote_text = data.get('quoteText', 'No quote found')
        quote_author = data.get('quoteAuthor', 'Unknown')
        return quote_text, quote_author
    except requests.RequestException as e:
        print(f"Error: {e}")
        return "No quote found", "Unknown"
