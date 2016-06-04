import json


def save(data, filename):
    string = json.dumps(data, indent=2, sort_keys=True)
    with open(filename, "w") as file:
        file.write(string)
