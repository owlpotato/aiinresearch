from backend.controller.SearchController import SearchController

# Initialisierung des Controllers
controller = SearchController()

# Deine Suchanfrage
query = "AI"

# Starte die Suche
print(controller.searchPapers(query))
