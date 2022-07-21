from User import User
from uuid import uuid4


class Customer(User):
    def __init__(self,userName,password,emailAddress,phoneNumber,address):
        super.__init__(userName,password,emailAddress,phoneNumber,address)
        self.customerID = uuid4() 
        self.currentLocation = None
        self.bookingID = -1
        self.paymentMethods = []
        self.onARide = False

    def getCustomerCurrentLocation(self):
        pass

    def payBill(self):
        pass

    def bookARide(self):
        pass

    def findRide(self):
        pass

    def cancelRide(self):
        pass
    
        

