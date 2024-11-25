from io import IOBase
import os

class CsvReader:
    def __init__(self, file_stream: IOBase) -> None:
        self.file_stream = file_stream

    # Method to check that current position of file stream is end of file or not
    def is_eof(self):
        current_position = self.file_stream.tell()    # save current position
        self.file_stream.seek(0, os.SEEK_END)
        
        end_position = self.file_stream.tell()    # find the size of file
        self.file_stream.seek(current_position, os.SEEK_SET)
        return current_position == end_position

    # Function to create an index for CSV file with index by amount
    # Index of CSV file is a dictionary with this format 
    # {
    #   "1st credit (value of credit column)": [offset of 1st line contain this credit, offset of last line contain this credit],
    #   "2nd credit": [offset of 1st line contain this credit, offset of last line contain this credit]
    #
    #   "last_line_offset": offset to the beginning of the last line in CSV file
    # }
    # You can use self.file_stream to get the current offset of file stream
    def index(self):
        pass

    
    # Jump to specific offset
    def seek(self, offset: int = 0):
        self.file_stream.seek(offset)

    # Read 1 line from file_stream
    def readline(self):
        line = self.file_stream.readline()
        return line
    
    # Read multiple lines from file_stream
    def readlines(self):
        lineList = []
        while self.is_eof() is False:
            line = self.readline()
            lineList.append(line)
        return lineList#