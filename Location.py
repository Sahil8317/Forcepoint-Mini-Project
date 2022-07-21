from uuid import uuid4
class Location:
    def __init__(self,locationName,locationPincode,userID):
        self.locationID = uuid4()
        self.locationName = locationName
        self.locationPincode = locationPincode
        self.userID = userID

    def displayLocationDetails(self):
        pass
