import json

from domain.BAPDBData import BAPDBData
from translate.translate_startegy import TranslateStrategy


class BAPDBFactory:

    def __init__(self):
        pass

    @staticmethod
    def _collect_diagnostics(diagnostic_json):
        a = json.loads(diagnostic_json)

        diagnostic = []

        for e in a['Diagnosen']['Diagnosen']['List']:
            title = e['Titel']

            if "Inhalt" in e.keys():
                content = e['Inhalt']
                diagnostic.append((title, content))
            else:
                diagnostic.append((title, ''))

        return diagnostic


    @staticmethod
    def build(data):
        berteleug = data[0]
        anamnesis = data[1]
        procedure = data[2]
        id_lab = data[8]

        try:
            # diagnostic_json = json.loads(str(data[3].decode("utf-8")))
            diagnostic = BAPDBFactory._collect_diagnostics(data[3])
        except Exception as e:
            diagnostic = ''

        bifunde = {
            'befundeWeitere': data[4],
            'befundeRadiologie': data[5],
            'befunde': data[6],
            'befundeLabor': data[7]
        }

        bapdb = BAPDBData(berteleug=berteleug, anamnesis=anamnesis, procedure=procedure, diagnostic=diagnostic,
                          bifunde=bifunde, id_lab=id_lab)
        return bapdb

    @staticmethod
    def build_en_translated(data, translation_strategy: TranslateStrategy):
        bapdb = BAPDBFactory.build(data)
        bapdb.anamnesis = translation_strategy.translate(bapdb.anamnesis.decode("utf-8") or ' empty ', 'en')
        bapdb.berteleug = translation_strategy.translate(bapdb.berteleug.decode("utf-8") or ' empty ', 'en')
        bapdb.procedure = translation_strategy.translate(bapdb.procedure.decode("utf-8") or ' empty ', 'en')

        translated_diagnostic = []
        for td in bapdb.dignostic:
            t_title = translation_strategy.translate(td[0] or ' ', 'en')
            t_content = translation_strategy.translate(td[1] or ' ', 'en')

            translated_diagnostic.append((t_title, t_content))

        bapdb.diagnostic = translated_diagnostic

        bapdb.bifunde = {
            'befundeWeitere': translation_strategy.translate(bapdb.bifunde['befundeWeitere'].decode("utf-8") or ' empty ', 'en'),
            'befundeRadiologie': translation_strategy.translate(bapdb.bifunde['befundeRadiologie'].decode("utf-8") or ' empty ', 'en'),
            'befunde': translation_strategy.translate(bapdb.bifunde['befunde'].decode("utf-8") or ' empty ', 'en'),
            'befundeLabor': translation_strategy.translate(bapdb.bifunde['befundeLabor'].decode("utf-8") or ' empty ', 'en')
        }

        return bapdb