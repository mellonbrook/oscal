#/bin/bash python

import csv
import json

class Group(object):
    def __init__(self, id, group_class, title, controls = []):
        self.id = id
        self.group_class= group_class
        self.title = title 
        self.controls = controls 

    def to_dict(self):
        _dict = {}
        for key, value in self.__dict__.items():
            if key == "controls":
                _dict[key] = []
                for control in self.controls:
                  _dict[key].append(control.to_dict())
            else:
                if key == "group_class":
                   _dict["class"] = value
                else:
                   _dict[key] = value
        return _dict

class Control(object):
    def __init__(self, id, parts, title, properties, control_class = None, parameters = [], links = []):
        self.id = id
        self.parts = parts
        self.title = title
        self.properties = properties
        self.control_class = control_class
        self.parameters = parameters
        self.links = links

    def to_dict(self):
        _dict = {}
        for key, value in self.__dict__.items():
            if key == "parts":
                _dict[key] = []
                for part in self.parts:
                  _dict[key].append(part.to_dict())
            else:
                if key == "control_class":
                   _dict["class"] = value
                else:
                   _dict[key] = value
        return _dict

class Statement(object):
    def __init__(self, id, prose, name="statement", parts=[]):
        self.id = id + "_smt"
        self.prose = prose
        self.name = name
        self.parts = parts

    def to_dict(self):
        _dict = {}
        for key, value in self.__dict__.items():
            _dict[key] = value
        return _dict

class Guidance(object):
    def __init__(self, id, prose, name = "guidance", links=[]):
        self.id = id + "_gdn"
        self.prose = prose
        self.name = name
        self.parts = links

    def to_dict(self):
        _dict = {}
        for key, value in self.__dict__.items():
            _dict[key] = value
        return _dict

def convert_csv_to_oscal_json():
    group = Group(id="3.1", group_class="family", title="Access Control")

    with open('data/800-171-source.csv', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            control = Control(id=row[0], 
                              parts=[Statement(id=row[0], prose=row[1]), 
                                  Guidance(id=row[0], prose=row[2].replace("\\n", ' '))],
                              title=row[1], 
                              properties=[{"name":"label", "value": row[0]}]
                             )
            group.controls.append(control)

    return json.dumps(group.to_dict(), indent=4)

def write_oscal_json_to_file(oscal_json):
      file = open('800-171-oscal.json', "w")
      file.write(oscal_json) 
      file.close()  

def main():
    oscal_json = convert_csv_to_oscal_json()
    write_oscal_json_to_file(oscal_json)
    print("-------Conversion Complete : OUTPUT FILE: 800-171-oscal.json------- ")

if __name__ == "__main__":
    main()
