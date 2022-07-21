
from User import User
from uuid import uuid4

class Admin(User):

    allDrivers = []
    allCustomers = []
    def __init__(self, userName, password, emailAddress, phoneNumber, userAddress):
        super().__init__(userName, password, emailAddress, phoneNumber, userAddress)
        self.driverID = uuid4()


    def addCustomers():
        pass

    def addDrivers():
        pass

    def deleteCustomers():
        pass

    def deleteDriver():
        pass
    