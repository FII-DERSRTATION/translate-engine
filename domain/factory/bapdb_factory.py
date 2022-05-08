import json

from domain.BAPDBData import BAPDBData





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

        try:
            diagnostic_json = json.loads(data[3])
            diagnostic = BAPDBFactory._collect_diagnostics(diagnostic_json)
        except Exception as e:
            diagnostic = json.loads("{}")

        bifunde = {
            'befundeWeitere': data[4],
            'befundeRadiologie': data[5],
            'befunde': data[6],
            'befundeLabor': data[7]
        }

        bapdb = BAPDBData(berteleug=berteleug, anamnesis=anamnesis, procedure=procedure, diagnostic=diagnostic,
                          bifunde=bifunde)
        return bapdb