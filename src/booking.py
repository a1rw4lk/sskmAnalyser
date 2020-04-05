

class Booking:

    def __init__(self, date, bookingType, name, purpose, value):
        self.date = date
        self.bookingType = bookingType
        self.name = name
        self.purpose = purpose
        self.value = value
        self.category = "" 

    def isExpense(self):
        if self.value < 0:
            return True
        else:
            return False    