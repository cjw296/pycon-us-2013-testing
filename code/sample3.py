import csv

def most_owed(path):
    
    with open(path) as data:
        reader = csv.DictReader(data)
        
        owed = 0
        name = None
        
        for row in reader:

            # what if this blows up?
            current = int(row['Money Owed'])
            
            if current > owed:
                owed = current
                name = row['Name']

        # how long did it take?
        return name.strip()
