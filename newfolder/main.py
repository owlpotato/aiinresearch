from controller.search_controller import SearchController

# Konfiguration: Hier steuerst du, welche Datenquellen aktiv sind
config = {
    'scopus_key': '4f8e6aded569f7273528997a3b055f35',
    'wos_key': '34fb3dd31f0621e066a60689e5f8f8e5c2158c78',
    'use_scopus': False,
    'use_openalex': False,
    'use_wos': True,
}

def main():
    controller = SearchController(config)
    query = input("🔍 Suchbegriff eingeben: ").strip()
    filters = {}  # Erweiterbar z.B. {'year_from': 2020, 'quality_min': 0.8}
    controller.search_and_export(query, filters)

if __name__ == '__main__':
    main()
