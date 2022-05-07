"""
B - Berteleug
A - Anamanesis
R - Procedure
D - Diganostic
B - Biufunde
"""


class BAPDBData:

    def __init__(self, berteleug, anamnesis, procedure, diagnostic, bifunde):
        self.berteleug = berteleug
        self.anamnesis = anamnesis
        self.procedure = procedure
        self.dignostic = diagnostic
        self.bifunde = bifunde

    def render_json(self):
        pass
