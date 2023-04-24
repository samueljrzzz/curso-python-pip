import csv

def leercsv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter= ',')
        header = next(reader)
        data = []
        for row in reader:
            iteration = zip(header, row)
            paisdict = {k:v for k, v in iteration}
            data.append(paisdict)
    return data