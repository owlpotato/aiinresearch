import requests
from models.paper import Paper

class WOSService:
    def __init__(self, api_key, enabled=True):
        self.api_key = api_key
        self.base_url = "https://api.clarivate.com/api/wos"
        self.enabled = enabled

    def query(self, search_term, filters):
        if not self.enabled:
            return []

        headers = {
            'X-ApiKey': self.api_key,
            'Accept': 'application/json'
        }
        params = {
            'databaseId': 'WOS',
            'usrQuery': search_term,
            'count': 25
        }

        try:
            response = requests.get(self.base_url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            records = data.get('Data', {}).get('Records', {}).get('records', [])

            return [
                Paper(
                    rec.get('title', {}).get('value', 'N/A'),
                    ", ".join([a.get('full_name', 'N/A') for a in rec.get('authors', [])]),
                    rec.get('abstract', {}).get('value', 'N/A'),
                    rec.get('source', {}).get('published_biblio_date', '1900-01-01'),
                    'WOS',
                    0.85
                )
                for rec in records
            ]
        except requests.RequestException as e:
            print(f"[WOS API Error]: {e}")
            return []
