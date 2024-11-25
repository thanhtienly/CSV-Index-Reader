from modules.csv_reader import CsvReader
import json

def sort_raw_file():
    # TODO 
    # Read the "chuyen_khoan.csv" file, then sort this file by "credit" column
    # Write the result to the new file with name "sorted_transactions.csv" without header row.
    pass

if __name__ == "__main__":
    sort_raw_file()

    file = open('sorted_transactions.csv', 'rb')
    csvReader = CsvReader(file)
    # TODO
    # Implement index method of CSVReader to index the CSV file
    indexes = csvReader.index()

    with open('index.json', 'w') as file:
        json.dump(indexes, file)