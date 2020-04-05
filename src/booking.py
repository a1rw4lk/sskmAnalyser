

class Booking:

    def __init__(self, date, purpose, name, value):
        self.date = date
        self.purpose = purpose
        self.name = name
        self.value = value
        self.category = "" 

    def isExpense(self):
        if self.value < 0:
            return True
        else:
            return False    