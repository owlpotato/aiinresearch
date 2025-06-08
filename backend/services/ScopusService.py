# services/scopus_service.py
# Scopus-API-Abfrage mit Fehlerbehandlung

from datetime import date
import requests

from backend.services.PaperRestService import PaperRestService
from backend.models.PaperDTO import PaperDTO


class ScopusService(PaperRestService):

    def __init__(self):
        self.api_key = ''
        self.base_url = "https://api.elsevier.com/content/search/scopus"

    def query(self, search_term: str) -> list[PaperDTO]:
        headers = {'X-ELS-APIKey': self.api_key}
        params = {'query': search_term, 'count': '25'}

        try:
            response = requests.get(self.base_url, headers=headers, params=params)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"[Scopus API Fehler]: {e}")
            return []

        data = response.json()
        entries = data.get('search-results', {}).get('entry', [])
        if not entries:
            print("🔍 Scopus liefert keine Treffer für diesen Suchbegriff.")
            return []

        results: list[PaperDTO] = []

        for entry in entries:
            title = entry.get('dc:title', 'N/A')
            authors = entry.get('dc:creator', 'N/A')
            abstract = entry.get('dc:description', 'N/A')
            date = entry.get('prism:coverDate', '1900-01-01')
            journal_name = entry.get('prism:publicationName')
            issn = entry.get('prism:issn') or entry.get('prism:eIssn')
            doi = entry.get('prism:doi')
            citations = int(entry.get('citedby-count', 0))
            url = f"https://doi.org/{doi}" if doi else None

            print(f"📄 Titel: {title} | DOI: {doi} | ISSN: {issn} | Citations: {citations}")

            results.append(PaperDTO(
                title=title,
                authors=authors,
                abstract=abstract,
                date=date,
                source='Scopus',
                quality_score=0.0,
                journal_name=journal_name,
                issn=issn.replace('-', '') if issn else None,
                eissn=None,
                doi=doi,
                url=url,
                citations=citations
            ))
        return results

    def getPaperList(self, searchTerm: str) -> list[PaperDTO]:
        return self.query(searchTerm)
