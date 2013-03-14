import csv

def most_owed(path):
    with open(path) as data:
        reader = csv.DictReader(data)
        for row in reader:
            return row['Name']
