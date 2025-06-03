# === controller/search_controller.py ===
from services.scopus_service import ScopusService
from services.openalex_service import OpenAlexService
from services.wos_service import WOSService
import csv

class SearchController:
    def __init__(self, config):
        self.sources = [
            ScopusService(api_key=config['scopus_key'], enabled=config.get('use_scopus', True)),
            OpenAlexService(enabled=config.get('use_openalex', True)),
            WOSService(api_key=config['wos_key'], enabled=config.get('use_wos', True))
        ]

    def search_and_export(self, query, filters, filename="results.csv"):
        all_papers = []
        for service in self.sources:
            papers = service.query(query, filters)
            all_papers.extend(papers)

        if not all_papers:
            print("❌ Keine Ergebnisse gefunden.")
            return

        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['Title', 'Authors', 'Abstract', 'Date', 'Source', 'QualityScore']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for paper in all_papers:
                    writer.writerow(paper.to_dict())
            print(f"✅ Ergebnisse gespeichert in {filename}")
        except Exception as e:
            print(f"[CSV Export Error]: {e}")
