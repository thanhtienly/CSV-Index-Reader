from fastapi import FastAPI
from modules.query_builder import QueryBuilder
from modules.transaction import Transaction, TransactionTable
from modules.csv_reader import CsvReader

app = FastAPI()


# return of this api needs to match this format
# {
#   "data": transaction_table
#   "next_cursor": str
# }

# next_cursor is null if CSV file don't have any more transaction match the search term
# Otherwise, next_cursor is string of number (number -> string)

@app.get('/query')
def get_transactions(amount: str = "", message : str = "", next_cursor: int = 0):
    if amount == "" and message == "":
        return {
            "data": [],
            "next_cursor": "null"
        }
    
    queryBuilder = QueryBuilder(next_cursor, amount, message)

    # TODO
    # get start_offset, end_offset from QueryBuilder, then csvReader use this offset to read the CSV file
    
    file = open('sorted_transactions.csv', 'rb')
    csvReader = CsvReader(file)

    # TODO 
    # csvReader use the offset above to jump to specific position, then read transaction line by line
    # Use QueryBuilder to check each transaction line, 
    # If transaction detail match the search term, then insert transaction into transaction table