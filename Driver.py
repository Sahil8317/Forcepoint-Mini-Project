from User import User
from uuid import uuid4

class Driver(User):
    def __init__(self, userName, password, emailAddress, phoneNumber, userAddress,cabDetails):
        super().__init__(userName, password, emailAddress, phoneNumber, userAddress)
        deriverID = uuid4()
        self.cabDetails = cabDetails
        self.rating = 0
        self.currentLocation = None

    def setDriverCurrentLocation(self):
        pass

    def getDriverDetails(self):
        pass


