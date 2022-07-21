
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

    def displayUserDetails():
        pass

    def getLoggingInfo():
        pass

    def changelogInStatus():
        pass