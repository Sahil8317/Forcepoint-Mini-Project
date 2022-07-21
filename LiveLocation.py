
from uuid import uuid4


class LiveLocation:
    def __init__(self,driverID,prevLocation,currLocation):
        self.locationID = uuid4()
        self.driverID = driverID
        self.previousLocation = prevLocation
        self.currentLocation = currLocation
        self.isShared = False

    def updatePreviouslocation():
        pass

    def updateCurrentlocation():
        pass

    def changeSharedlocation():
        pass
    