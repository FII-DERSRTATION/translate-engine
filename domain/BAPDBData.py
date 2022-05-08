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


class BAPDBData:

    def __init__(self, berteleug, anamnesis, procedure, diagnostic, bifunde):
        self.berteleug = berteleug
        self.anamnesis = anamnesis
        self.procedure = procedure
        self.dignostic = diagnostic
        self.bifunde = bifunde

    def render_json(self):
        pass
