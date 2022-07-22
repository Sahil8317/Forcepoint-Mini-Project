import uuid

from rideDetails import RideDetails

class Bill:
    allBillhistory = []
    def __init__(self, customerID, rideDetails, amount):
        self.billID = uuid.uuid4()
        self.customerID = customerID
        self.rideDetails = rideDetails
        self.amount = amount
        self.isBillPaid = False
        Bill.allBillhistory.append(self)

    # @staticmethod
    # def createBill(customerID, cabDetails, driverID, amount):
    #     return Bill(customerID, cabDetails, driverID, amount)

    @staticmethod
    def generateBill(customerID, rideDetails, amount):
        newBill = Bill(customerID, rideDetails, amount)
        return newBill
    
    def displayBill(self):
        print(" ****Generated Bill is as follows!!*** ")
        print(f'Bill ID: {self.billID}')
        self.rideDetails.setAmount(self.amount)
        self.rideDetails.displayRideDetails()
        if self.isBillPaid:
            print('Bill Paid!')
        else:
            print('Bill Pending.')

    def changeBillStatus(self,newStatus):
        self.isBillPaid = newStatus