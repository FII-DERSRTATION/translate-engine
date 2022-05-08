from domain.factory.bapdb_factory import BAPDBFactory
from translate.aws_detect_and_translate_strategy import AWSDetectAndTranslateStrategy


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
            bapdbs.append(BAPDBFactory.build_en_translated(r, AWSDetectAndTranslateStrategy()))

    def provide(self):
        return self._bulk_provide()
