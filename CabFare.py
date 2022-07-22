
from CabCategory import *

class CabFare:
    def __init__(self, cabCategory:ICabCategory) -> None:
        self.cabCategory = cabCategory

    def calculateCabFare(self, distanceTravelled):
        return self.cabCategory.calculateCabFare(distanceTravelled)


# myObj = CabFare(Economy())
# print(myObj.calculateCabFare(3)) #55
# myObj = CabFare(Sedan())
# print(myObj.calculateCabFare(5)) #100

# class CabFare:

#     @staticmethod
#     def calculateCabFare(cabCategory, distanceTravelled):
#         if cabCategory.lower() == 'economy':
#         elif cabCategory.lower() == 'sedan':
#         elif cabCategory.lower() == 'prime':
#         print('Something went wrong, Fare not get processed.')
#         return 0
