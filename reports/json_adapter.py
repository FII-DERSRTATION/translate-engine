import json
import re


class JSONContentRedAdapter:

    def __init__(self):
        pass

    @staticmethod
    def convert(self, payload_string):
        trimmed_str = re.sub(r"[\n\t\s]*", "", payload_string.decode("utf-8"))

        try:
            data = json.loads(trimmed_str)
        except ValueError as e:
            return ""

