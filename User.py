
from uuid import uuid4

class User:
    def __init__(self,userName,password,emailAddress,phoneNumber,userAddress):
        self.userName = userName
        self.password = password
        self.emailAddress = emailAddress
        self.phoneNumber = phoneNumber
        self.userAddress = userAddress
        self.isLoggedIn = False
        self.userID = uuid4()

    def displayUserDetails(self):
        print("User Name is "+self.userName)
        print("Email Address is "+self.emailAddress)
        print("Phone Number is "+self.emailAddress)
        print("User Address is "+self.userAddress)
        print("is logged in "+self.isLoggedIn)

    def getLoggingInfo(self):
        self.isLoggedIn

    def changelogInStatus(self,status):
        self.isLoggedIn = status