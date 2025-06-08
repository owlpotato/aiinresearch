from backend.services.OpenalexService import OpenAlexService
from backend.services.PaperRestService import PaperRestService
from backend.services.ScopusService import ScopusService
from backend.services.WosService import WOSService
from backend.models.PaperDTO import PaperDTO

class SearchController:
    apiClients: list[PaperRestService]

    def __init__(self):

        # self.config = config
        # self.journal_data = load_journal_ratings(config['rating_file'])

        # API-Clients initialisieren
        scopus = ScopusService()
        openalex = OpenAlexService()
        #TODO check API key wos = WOSService()

        self.apiClients = [scopus, openalex]

    def searchPapers(self, searchTerm: str) -> list[PaperDTO]:

        all_results: list[PaperDTO] = []

        for apiClient in self.apiClients:
            all_results += apiClient.getPaperList(searchTerm)

        return all_results
