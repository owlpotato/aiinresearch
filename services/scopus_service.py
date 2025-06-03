import requests
from models.paper import Paper

class ScopusService:
    def __init__(self, api_key, enabled=True):
        self.api_key = api_key
        self.base_url = "https://api.elsevier.com/content/search/scopus"
        self.enabled = enabled

    def query(self, search_term, filters):
        if not self.enabled:
            return []

        headers = {'X-ELS-APIKey': self.api_key}
        params = {'query': search_term, 'count': 25}

        try:
            response = requests.get(self.base_url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            entries = data.get('search-results', {}).get('entry', [])
            return [Paper(
                entry.get('dc:title', 'N/A'),
                entry.get('dc:creator', 'N/A'),
                entry.get('dc:description', 'N/A'),
                entry.get('prism:coverDate', '1900-01-01'),
                'Scopus',
                0.9
            ) for entry in entries]
        except requests.RequestException as e:
            print(f"[Scopus API Error]: {e}")
            return []
