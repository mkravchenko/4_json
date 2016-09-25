import json
import os
import sys


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        data = f.read()
    return json.loads(data)


def pretty_print_json(jdata):
    print(json.dumps(jdata, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    path_to_file = sys.argv[1]
    json_data = load_data(path_to_file)
    pretty_print_json(json_data)
