from os import stat


class RideDetails:
    def __init__(self, pickupLocation, dropLocation, customerID, driverID, cabCategory):
        self.pickupLocation = pickupLocation
        self.dropLocation = dropLocation
        self.customerID = customerID
        self.driverID = driverID
        self.cabCategory = cabCategory
        self.billAmount = 0

    @staticmethod
    def createRideDetails(pickupLocation,dropLocation,customerID,driverID,cabCategory):
        newRideDetails = RideDetails(pickupLocation,dropLocation,customerID,driverID,cabCategory)
        return newRideDetails
    
    def displayRideDetails(self):
        print('Pickup Location Details:')
        self.pickupLocation.displayLocationDetails()
        print('Drop Location Details:')
        self.dropLocation.displayLocationDetails()
        print(f'Cab Category: {self.cabCategory}')
        print(f'Total Bill: {self.billAmount}')

    def setAmount(self, amount):
        self.billAmount = amount