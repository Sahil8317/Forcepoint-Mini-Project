from User import User

class Driver(User):
    def __init__(self, driverID, userName, password, emailAddress, phoneNumber, userAddress,cabDetails):
        super().__init__(userName, password, emailAddress, phoneNumber, userAddress)
        self.driverID = driverID
        self.cabDetails = cabDetails
        self.rating = 0

    @staticmethod
    def createDriver(driverID, userName,password,emailAddress,phoneNumber,address, cabDetails):
        newDriver = Driver(driverID, userName,password,emailAddress,phoneNumber,address, cabDetails)
        return newDriver

    def displayDriverDetails(self):
        print("Driver Name "+self.userName)
        print("Driver Phone Number is "+self.phoneNumber)




