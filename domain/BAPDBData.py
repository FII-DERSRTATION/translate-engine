"""
B - Berteleug
A - Anamanesis
R - Procedure
D - Diganostic
B - Biufunde
"""

## todo: refaactor bifunde to befunde (findings)
## todo: refactor berteleug (assesment) to berte
## todo: put them in english
import json


class BAPDBData:

    def __init__(self, berteleug, anamnesis, procedure, diagnostic, bifunde, id_lab):
        self.berteleug = berteleug
        self.anamnesis = anamnesis
        self.procedure = procedure
        self.dignostic = diagnostic
        self.bifunde = bifunde
        self.id_lab = id_lab

    def render_json(self):
        return json.dumps(self.__dict__)
