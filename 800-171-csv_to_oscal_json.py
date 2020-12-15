#/bin/bash python

import csv

class Group(object):
    def __init__(self, id, group_class, title, controls = []):
        self.id = id
        self.group_class= group_class
        self.title = title 
        self.controls = controls 

class Control(object):
    def __init__(self, id, parts, title, properties, control_class = None, parameters = [], links = []):
        self.id = id
        self.parts = parts
        self.title = title
        self.properties = properties
        self.control_class = control_class
        self.parameters = parameters
        self.links = links

class Statement(object):
    def __init__(self, id, prose, name="statement", parts=[]):
        self.id = id + "_smt"
        self.prose = prose
        self.name = name
        self.parts = parts

class Guidance(object):
    def __init__(self, id, prose, name = "guidance", links=[]):
        self.id = id + "_gdn"
        self.prose = prose
        self.name = name
        self.parts = links

def convert_csv_to_oscal_json():
    group = Group(id="3.1", group_class="family", title="Access Control")

    with open('data/800-171-source.csv', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            control = Control(id=row[0], 
                              parts=[Statement(id=row[0], prose=row[1]), 
                                  Guidance(id=row[1], prose=row[2].replace("\\n", ' '))],
                              title=row[1], 
                              properties=[{"name":"label", "value": row[0]}]
                             )
            group.controls.append(control)
    return group

def main():
    oscal_json = convert_csv_to_oscal_json()

if __name__ == "__main__":
    main()
