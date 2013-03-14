import datetime
import csv, logging

log = logging.getLogger()

def most_owed(path):
    started = datetime.datetime.now()
    with open(path) as data:
        reader = csv.DictReader(data)
        owed = 0
        name = None
        for row in reader:
            value = row['Money Owed']
            try:
                current = int(value)
            except ValueError:
                log.warning(
                    'ignoring %r as not valid',
                    value
                    )
                continue
            if current > owed:
                owed = current
                name = row['Name']
    log.info('Processing took %s',
             datetime.datetime.now() - started)
    return name.strip()
