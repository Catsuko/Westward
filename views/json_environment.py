import json


class JsonEnvironment:

    def __init__(self, filename):
        self.filename = filename
        self.json = None

    def color(self, key):
        if self.json is None:
            self.__read_json()
        return self.json["colors"][key]

    def __read_json(self):
        with open(self.filename) as json_file:
            self.json = json.load(json_file)
