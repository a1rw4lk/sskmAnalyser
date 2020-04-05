import csv
import os
import errno
import re
from booking import Booking

class DataParser:

    def __init__(self, filePath):
        self.dateColumn = 1
        self.nameColumn = 11
        self.purposeColumn = 4
        self.valueColumn = 14
        self.typeColumn = 3
        self.bookings = []

        if os.path.exists(filePath):
            with open(filePath, 'r', encoding='iso8859_16') as csvfile:
                # Read the data from file and skip first line
                reader = csv.reader(csvfile, delimiter=';')
                next(reader)            
                self.ParseRawData(reader)
        else : 
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), filePath)

    def ParseRawData(self, reader):
        for line in reader:
            # Ignore lines that arent booked yet
            if line[16] == "Umsatz vorgemerkt":
                continue

            # Delete unnecessary whitespaces with a regex
            for i, element in enumerate(line):
                line[i] = re.sub(' +', ' ', element)

            booking = Booking(line[self.dateColumn], \
                              line[self.typeColumn], \
                              line[self.nameColumn], \
                              line[self.purposeColumn], \
                              line[self.valueColumn])
            self.bookings.append(booking)

    def GetAllBookings(self):
        return self.bookings
