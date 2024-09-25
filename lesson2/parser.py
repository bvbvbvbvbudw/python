import json

class Parser(object):
    def __init__(self, config_file):
        self.config_file = config_file
        self.config_data = {}

    def parse(self):
        current_section = None
        with open(self.config_file, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if line.startswith('[') and line.endswith(']'):
                    current_section = line[1:-1]
                    self.config_data[current_section] = {}
                elif '=' in line:
                    key, value = map(str.strip, line.split('=', 1))
                    self.config_data[current_section][key] = self.validate(key, value)
        return self.config_data

    def validate(self, key, value):
        if key == "port" and not value.isdigit():
            exit("port must be an integer")
        if key == "timeout" and not value.isdigit():
            exit("timeout must be an integer")
        return value

    def save_json(self, json_file):
        with open(json_file, 'w') as file:
            json.dump(self.config_data, file, indent=1)


parse = Parser('config.cfg')
print(parse.parse())
parse.save_json('config.json')