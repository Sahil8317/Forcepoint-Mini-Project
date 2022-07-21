import uuid

class Bill:
    allBillhistory = []
    def __init__(self, customerID, cabDetails, driverID, amount):
        self.billID = uuid.uuid4()
        self.customerID = customerID
        self.cabDetails = cabDetails
        self.driverID = driverID
        self.amount = amount
        self.isBillPaid = False
        Bill.allBillhistory.append(self)

    def generateBill():
        pass

    def changeBillStatus():
        pass