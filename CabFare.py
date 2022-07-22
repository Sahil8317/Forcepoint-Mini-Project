

class CabFare:
    baseFare = 50.0

    @staticmethod
    def calculateCabFare(cabCategory, distanceTravelled):
        if cabCategory.lower() == 'economy':
            return distanceTravelled*5 + CabFare.baseFare
        elif cabCategory.lower() == 'sedan':
            return distanceTravelled*10 + CabFare.baseFare
        elif cabCategory.lower() == 'prime':
            return distanceTravelled*15 + CabFare.baseFare
        print('Something went wrong, Fare not get processed.')
        return 0
