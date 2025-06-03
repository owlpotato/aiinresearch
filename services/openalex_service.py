import requests
from models.paper import Paper

class OpenAlexService:
    def __init__(self, enabled=True):
        self.base_url = "https://api.openalex.org/works"
        self.enabled = enabled

    def query(self, search_term, filters):
        if not self.enabled:
            return []

        params = {'search': search_term, 'per-page': 25}
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            entries = data.get('results', [])
            return [Paper(
                entry.get('title', 'N/A'),
                "; ".join([auth['author']['display_name'] for auth in entry.get('authorships', [])]),
                "...abstract...",  # Optional: abstract aus Inverted Index aufbauen
                entry.get('publication_date', '1900-01-01'),
                'OpenAlex',
                entry.get('cited_by_count', 0)
            ) for entry in entries]
        except requests.RequestException as e:
            print(f"[OpenAlex API Error]: {e}")
            return []