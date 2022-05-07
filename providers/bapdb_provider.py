class BAPDBProvider:

    def __init__(self, db_con):
        self.db_con = db_con

    def _bulk_provide(self):
        cursor = self.db_con.cursor()
        cursor.execute("select anamnese, procedere, beurteilung, diagnosen, befundeWeitere, befundeRadiologie, befunde, befundeLabor  from report_nf ")
        records = cursor.fetchall()

        for r in records:
            print(30 * "=")
            print(r)
            print(30 * "=")
