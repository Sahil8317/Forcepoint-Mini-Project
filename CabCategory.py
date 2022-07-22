from abc import ABC, abstractclassmethod, abstractstaticmethod

class ICabCategory(ABC):
    @abstractclassmethod
    def calculateCabFare(self, distanceTravelled):
        pass
    @abstractstaticmethod
    def returnCabList():
        pass

class Economy(ICabCategory):
    baseFare = 40.0
    economyCabList = []
    def calculateCabFare(self, distanceTravelled):
        return distanceTravelled*5 + Economy.baseFare
    
    @staticmethod
    def returnCabList():
        return Economy.economyCabList

class Sedan(ICabCategory):
    baseFare = 50.0
    sedanCabList = []
    def calculateCabFare(self, distanceTravelled):
        return distanceTravelled*10 + Sedan.baseFare
    
    @staticmethod
    def returnCabList():
        return Sedan.sedanCabList


class Prime(ICabCategory):
    baseFare = 60.0
    primeCabList = []
    def calculateCabFare(self, distanceTravelled):
        return distanceTravelled*15 + Prime.baseFare

    @staticmethod
    def returnCabList():
        return Prime.primeCabList
        
