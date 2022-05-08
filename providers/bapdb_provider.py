from domain.factory.bapdb_factory import BAPDBFactory


class BAPDBProvider:

    def __init__(self, db_con):
        self.db_con = db_con

    def _bulk_provide(self):
        cursor = self.db_con.cursor()
        cursor.execute(
            "select anamnese, procedere, beurteilung, diagnosen, befundeWeitere, befundeRadiologie, befunde, befundeLabor  from report_nf ")
        records = cursor.fetchall()

        bapdbs = []

        for r in records:
            bapdbs.append(BAPDBFactory.build(r))

    def provide(self):
        return self._bulk_provide()
