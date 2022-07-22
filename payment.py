from abc import ABC, abstractclassmethod
from time import sleep
import uuid
# 

class PaymentProcessor(ABC):
    @abstractclassmethod
    def payAmount(self, amount):
        pass

# class Payment(PaymentProcessor):
#     def __init__(self, customerID, paymentType):
#         self.transactionID = uuid.uuid4()
#         self.customerID = customerID
#         self.paymentType = paymentType
    
#     def payAmount():
#         pass

class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, creditCardNumber, securityCode):
        self.creditCardNumber = creditCardNumber
        self.securityCode = securityCode
        self.status = ''

    def payAmount(self, amount):
        print('Processng Credit Card...')
        sleep(4)
        print(f'Verifying Security Code for credit card {self.creditCardNumber}')
        print(f'Transaction Successful \nAmount: Rs. {amount} is paid!')
        self.status = 'paid'

class UPIPaymentProcessor(PaymentProcessor):
    def __init__(self, upiID, securityCode):
        self.upiID = upiID
        self.securityCode = securityCode
        self.status = ''

    def payAmount(self, amount):
        print('Processng Debit Card...')
        print(f'Verifying Security Code for UPI ID {self.upiID}')
        self.status = 'paid'

