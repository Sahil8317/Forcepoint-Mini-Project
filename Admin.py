
from time import sleep
from uuid import uuid4

from User import User
from CabCategory import *
from billing import Bill
from Driver import Driver
from CabFare import CabFare
from Customer import Customer
from Location import Location
from cabDetails import CabDetails
from rideDetails import RideDetails

#Singleton class

class Admin(User):
    admin = None
    allDrivers = []
    allCustomers = []
    cabCategopry = ["economy","sedan","prime"]
    cabCategoryCount = 3
    cabCategoryDictionary =  {"1":"economy","2":"sedan","3":"prime"}
    cabCategoryClassDictionary = {"economy":Economy,"sedan":Sedan,"prime":Prime}

    def __init__(self, userName, password, emailAddress, phoneNumber, userAddress):
        super().__init__(userName, password, emailAddress, phoneNumber, userAddress)
        self.currentCustomer = None
        self.customerCabCategory = None
        self.customerRideDetails = None
        self.customerBill = None

    @staticmethod
    def createAdmin(userName, password, emailAddress, phoneNumber, userAddress):
        if Admin.admin==None:
            admin = Admin(userName,password,emailAddress,phoneNumber,userAddress)
            return admin

        return Admin.admin



    def startSystem(self):
        # Login
        print("******** Welcome to cab rental system *********** ")
        choice = input("1. Login 2. SignIn  ") 
        response = False
        print(choice)
        if choice=='1':
           userName = input("please enter the userName ")
           response = self.loginCustomer(userName)
           if not response:
              self.addCustomers()
        elif choice=='2':
            self.addCustomers()

        # Ride booking
        print('Enter your current Location and Pincode,')
        currentLocationName = input('Current Location Name: ')
        pincode = input('Pincode: ')
        self.currentCustomer.setCustomerCurrentlocation(currentLocationName,pincode)
        choice = input("1. Book A Ride  ")
        if choice=='1':
            print('Enter your Drop Location and Pincode,')
            dropLocationName = input('Drop Location: ')
            dropPincode = input('Pincode: ')
            droplocation = Location.createLocationObject(dropLocationName,dropPincode,self.currentCustomer.customerID)
            self.findRideForCustomer(droplocation)
        else:
            print("Invalid choice!!")


        # Billing
        totalFare = self.calculateCustomerFare()
        self.customerBill = self.generateCustomerBill(self.currentCustomer.customerID,self.customerRideDetails,totalFare)
        # Display the bill to the customer.
        self.customerBill.displayBill()
        choice = input("Please enter 1 to proceed and pay the bill ")
        if choice == '1':
           response =  self.currentCustomer.payBill(self.customerBill)
           if response:
                print("Bill paid successfully!!")
           else:
                print("Some Error occured!!")

        else :
            print("invalid choice!")


        


    def displayCarCategory(self):
        print("Below are the cabs available in your area ")
        index = 1
        for cab in Admin.cabCategopry:
            print(str(index)+" .Book A "+cab)
            index+=1
        
    def addNewCabCategory(newCategoryName,baseFare):
        pass

    def findRideForCustomer(self,dropLocation):
        if self.currentCustomer==None:
            self.loginCustomer()
            return 
        self.displayCarCategory()
        customerCabChoice = input("Enter Choice ")
      
        self.customerCabCategory = Admin.cabCategoryDictionary[customerCabChoice]
        flag,driver = self.searchForNearestCab(self.customerCabCategory,Admin.cabCategoryClassDictionary[self.customerCabCategory])
        if not flag:
            return False
        self.pickUpCustomer(dropLocation,driver)
        return True
    

    def findDriver(self,driverID):
        for driver in Admin.allDrivers:
            if driver.driverID==driverID:
                return driver
        return False

    def searchForNearestCab(self,cabCategory,cabCategoryClass):
        cabList = cabCategoryClass.returnCabList()
        allotedCab = cabList[0]
        cabDistance = abs((cabList[0].currentLocation.locationID)-(self.currentCustomer.currentLocation.locationID))
        for cab in cabList:
            currentDistance = abs((cab.currentLocation.locationID)-(self.currentCustomer.currentLocation.locationID))
            if currentDistance < cabDistance:
                cabDistance = currentDistance
                allotedCab = cab
        
        response = self.currentCustomer.bookARide(cabCategory,allotedCab)
        if response :
            print("Your Cab Details are as follows: ")
            allotedCab.displayCabDetails()
            print("Driver Details are as follows: ")
            allotedDriver = self.findDriver(allotedCab.driverID)
            allotedDriver.displayDriverDetails()
            return True,allotedDriver
        print("Something Went Wrong Please Try Again!!")
            
         
    def pickUpCustomer(self,dropLocation,driver):
        print("Your Cab is Arriving Soon!!")
        sleep(5) # just for showing cab arrival
        self.customerRideDetails = RideDetails.createRideDetails(self.currentCustomer.currentLocation,dropLocation,self.currentCustomer.customerID,driver.driverID,self.customerCabCategory)
        self.cabRiding()

    def cabRiding(self):
        print(" Cab ride is Started!! ")
        sleep(10)
        self.dropCustomer()


    def dropCustomer(self):
        # make a ride details object and print it and generate bill
        print("dropped customer at ")
        self.customerRideDetails.dropLocation.displayLocationDetails()

    def generateCustomerBill(self,customerID,rideDetails,fare):
        customerBill = Bill.generateBill(customerID,rideDetails,fare)
        return customerBill

        
    def calculateCustomerFare(self):
        distanceTravelled = abs((self.customerRideDetails.pickupLocation.locationID)-(self.customerRideDetails.dropLocation.locationID))
        newCabFare = CabFare(Admin.cabCategoryClassDictionary[(self.customerCabCategory.lower())]())
        customerTotalFare = newCabFare.calculateCabFare(distanceTravelled)
        return customerTotalFare

    def _findCustomer(self, userName):
        for c in Admin.allCustomers:
            if c.userName == userName:
                return True, c
        return False, None

    def _findDriver(self, userName):
        for d in Admin.allDrivers:
            if d.userName == userName:
                return True, d
        return False, None

    def addCustomers(self):
        customerID = uuid4()
        userName = input("Enter the customer name: ")
        password = input("Enter the Password: ")
        emailID = input("Enter the Email ID: ")
        phoneNumber = input("Enter the Phone Number: ")
        address = input("Enter the residence address: ")
        flag, customer = self._findCustomer(userName)
        if flag:
            customer.isLoggedIn = True
            return customer
        
        newCustomer = Customer.createCustomer(customerID, userName, password, emailID, phoneNumber, address)
        newCustomer.isLoggedIn = True

        Admin.allCustomers.append(newCustomer)
        self.currentCustomer = newCustomer
        return newCustomer

    def addDrivers(self):
        driverID = uuid4()
        userName = input("Enter the drvier name: ")
        password = input("Enter the Password: ")
        emailID = input("Enter the Email ID: ")
        phoneNumber = input("Enter the Phone Number: ")
        address = input("Enter the residence address: ")
        flag, driver = self._findDriver(userName)
        if flag:
            driver.isLoggedIn = True
            return driver
        
        cabNumber = input("Enter the vehicle number: ")
        cabType = input("Enter the vehicle model: ")
        cabCategory = input("Enter the vehicle category(Economy/Sedan/Prime): ")
        locationName = input("Enter your current location ")
        locationPincode = input("Enter your current pincode! ")
        driverCurrentlocation = Location(locationName,locationPincode,driverID)
        newCab = CabDetails.createCab(driverID, cabNumber, cabType, cabCategory)
        newCab.currentLocation = driverCurrentlocation

        
        cablist = Admin.cabCategoryClassDictionary[cabCategory.lower()].returnCabList()
        cablist.append(newCab)

        newDriver = Driver.createDriver(driverID, userName, password, emailID, phoneNumber, address, newCab)
        newDriver.isLoggedIn = True
        
        Admin.allDrivers.append(newDriver)
        return newDriver

    def loginCustomer(self, userName):
        flag, customer = self._findCustomer(userName)
        if flag:
            customer.isLoggedIn = True
            self.currentCustomer = customer
            print('Log In Successful')
            return True
        print('Customer does not exist')
        return False

    def logOffCustomer(self, userName):
        """"""
        flag, customer = self._findCustomer(userName)
        if flag:
            customer.isLoggedIn = False
            self.currentCustomer = None
            print('Log Off Successful')
            return True
        print('Customer doenot exist')
        return False
        
    def deleteCustomers(self, userName):
        """Admin rights to remove the customer."""
        flag, customer = self._findCustomer(userName)
        if flag:
            customer.isLoggedIn = False
            Admin.allCustomers.remove(customer)
            print("Account deleted successfully!")
            return True
        print('Account doesnot exist!')
        return False

    def deleteDriver(self, userName):
        """Admin rights to remove the driver."""
        flag, driver = self._findDriver(userName)
        if flag:
            driver.isLoggedIn = False
            cab = driver.cabDetails

            cablist = Admin.cabCategoryClassDictionary[cab.cabCategory.lower()].returnCabList()
            cablist.remove(cab)
            Admin.allCustomers.remove(driver)
            print("Account deleted successfully!")
            return True
        print('Account doesnot exist!')
        return False



if __name__=="__main__":
    newAdmin = Admin.createAdmin("admin1","123","admin@gmail.com","8317219776","kasarvadavli")

    newAdmin.addDrivers()
    
    newAdmin.startSystem()