import csv

def get_zip_dataset():
    result = {}
    with open('us_postal_codes.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            result[row[0]] = {
                'place': row[1],
                'state': row[2],
                'abbreviation': row[3],
                'country': row[4],
                'latitude': row[5],
                'longitude': row[6]
            }
    return result

