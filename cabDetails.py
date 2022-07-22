import uuid

class CabDetails:
    def __init__(self, driverID, carNumber, carModel,cabCategory):
        self.carID = uuid.uuid4()
        self.driverID = driverID
        self.carNumber = carNumber
        self.carModel = carModel
        self.cabCategory = cabCategory
        self.currentLocation = None
        self.fareMultiplier = 0

    @staticmethod
    def createCab(driverID, carNumber, carModel,cabCategory):
        newCab = CabDetails(driverID, carNumber, carModel,cabCategory)
        return newCab

    def displayCabDetails(self):
        print("Cab Number is "+str(self.carNumber))
        print("Cab Model is "+self.carModel)
        print("Cab Category "+self.cabCategory)
        print("Current location of cab is ")
        self.currentLocation.displayLocationDetails()
        return 
        