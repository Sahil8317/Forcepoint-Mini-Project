from uuid import uuid4
import random

class Location:
    def __init__(self,locationName,locationPincode,userID):
        self.locationID = random.randint(100,300)
        self.locationName = locationName
        self.locationPincode = locationPincode
        self.userID = userID

    @staticmethod
    def createLocationObject(locationName,locationPincode,userID):
        newLocationObject = Location(locationName,locationPincode,userID)
        return newLocationObject

    def displayLocationDetails(self):
        print(f'\t Location: {self.locationName}')
        print(f'\t Location Pincode: {self.locationPincode}')
