from connector import connect_to_kis_db
from providers.bapdb_provider import BAPDBProvider

if __name__ == "__main__":
    db = connect_to_kis_db()
    bapdb_prov = BAPDBProvider(db)
    bapdb_prov._bulk_provide()
