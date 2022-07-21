from User import User
from uuid import uuid4

class Driver(User):
    def __init__(self, userName, password, emailAddress, phoneNumber, userAddress):
        super().__init__(userName, password, emailAddress, phoneNumber, userAddress)
        deriverID = uuid4()
        