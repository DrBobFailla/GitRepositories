import csv


def csv2ListofDict(filename):
    # Converts the CSV file (transactions) into a list of dictionaries
    # Needs error checking

    listOfDictionaries = []

    with open(filename, 'r') as data:
        header = [line.strip() for line in data.readline().split(',')]
        reader = csv.DictReader(data, fieldnames=header)
        for i in reader:
            listOfDictionaries.append(i)
    return listOfDictionaries
