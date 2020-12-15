#/bin/bash python

import csv

def convert_csv_to_oscal_json():
    with open('data/800-171-source.csv', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

def main():
    oscal_json = convert_csv_to_oscal_json()

if __name__ == "__main__":
    main()
