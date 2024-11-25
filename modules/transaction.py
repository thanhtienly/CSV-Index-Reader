class Transaction:
    def __init__(self, rawLine: bytearray) -> None:
        self.rawLength = len(rawLine)
        line = rawLine.decode('ascii')
        line = line.strip()
        line = line.split(',', 4)

        self.date = line[0]
        self.transactionId = line[1]
        self.credit = line[2]
        self.debit = line[3]
        self.detail = line[4]


    def get_message(self):
        return self.detail

    def to_JSON(self) -> object:
        return {
            "date": self.date,
            "transactionId": self.transactionId,
            "credit": self.credit,
            "debit": self.debit,
            "detail": self.debit
        }

    def get_raw_transaction_length(self) -> int:
        return self.rawLength

class TransactionTable:
    default_table_size = 50

    def __init__(self) -> None:
        self.table = []
        self.size = 0
        self.is_full = False

    # Insert match transaction to transaction table
    # check if table size reach page size or not, if not then insert transaction to the table and update table size
    # Otherwise, set is_full_status to True
    def insert_transaction(self, transaction : Transaction):
        # TODO
        pass
        

    def set_full_status(self):
        self.is_full = True

    def get_is_full_status(self):
        return self.is_full
    
    def to_JSON(self):
        return self.table