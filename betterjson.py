import json
import os
class BetterJson:
    def __init__(self, file_name: str = "data.json"):
        if not file_name.endswith(".json"):
            file_name += ".json"
        self.filename = file_name
    def write(self, data: dict, indent: int = 4):
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=indent)
    def save(self, data: dict):
        data.clear()
        data.update(self.load())
    def load(self):
        data = {}
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                data = json.load(file)
        return data
    def set(self, key, value=None):
        data = self.load()
        data[key] = value
        self.write(data)
    
    def get(self, key, default=None):
        return self.load().get(key, default)
    