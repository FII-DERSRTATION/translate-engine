from domain.BAPDBData import BAPDBData


class BAPDBFactory:

    def __init__(self):
        pass

    @staticmethod
    def build(data):
        berteleug = data['berteleug']
        anamnesis = data['anamnesis']
        procedure = data['procedure']
        diagnostic = data['diagnostic']
        bifunde = data['bifunde']

        bapdb = BAPDBData(berteleug=berteleug, anamnesis=anamnesis, procedure=procedure, diagnostic=diagnostic,
                          bifunde=bifunde)