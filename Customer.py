from Location import Location
from User import User
from billing import Bill
from payment import *


class Customer(User):
    def __init__(self, customerID, userName, password, emailAddress, phoneNumber, address):
        super().__init__(userName, password, emailAddress, phoneNumber, address)
        self.customerID = customerID
        self.bookingID = -1
        self.paymentMethods = []
        self.onARide = False
        self.billDetails = None
        self.currentLocation = None
        self.isBillGenerated = False

    @staticmethod
    def createCustomer(customerID, userName,password,emailAddress,phoneNumber,address):
        newCustomer = Customer(customerID, userName,password,emailAddress,phoneNumber,address)
        return newCustomer

    def setCustomerCurrentlocation(self,locationName,locationPincode):
        customerLocationObject =  Location.createLocationObject(locationName,locationPincode,self.customerID)
        self.currentLocation = customerLocationObject

    def getCustomerCurrentLocation(self):
        if self.currentLocation==None:
            print("please set the current location of the customer!")
            return False
        return self.currentLocation

    def bookARide(self,cabCategory,cabDetails):
        # function to book a cab
        self.bookingID = str(cabDetails.carID)+str(self.customerID)
        self.onARide = True
        print("Your cab has been booked with booking ID "+self.bookingID)
        return True

    
    def generateBillDetails(self, cabDetail, driverID, amount):
        self.billDetails = Bill.generateBill(self.customerID, cabDetail, driverID, amount)
        
    def payBill(self, bill):
        print("Choose the payment method from below,")
        print("1. Credit Crad")
        print("2. UPI")
        choice = int(input('Enter Choice: '))

        if choice == 1:
            creditCardNumber = int(input('Enter the credit card number: '))
            cvv = int(input('Enter the cvv: '))
            newPayment = CreditPaymentProcessor(creditCardNumber, cvv)
            newPayment.payAmount(bill.amount)
            bill.isBillPaid = True
            return True
        elif choice == 2:
            upiID = (input('Enter the UPI ID: '))
            passcode = (input('Enter the passcode: '))
            newPayment = UPIPaymentProcessor(upiID, passcode)
            newPayment.payAmount(bill.amount)
            bill.isBillPaid = True
            return True
        
        print('Invalid Choice, Please start the billing again.')
        return False

        

