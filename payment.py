from abc import ABC, abstractclassmethod
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
    def __init__(self, securityCode):
        self.securityCode = securityCode
        self.status = ''

    def payAmount(self, amount):
        print('Processng Credit Card...')
        print(f'Verifying Security Code {self.securityCode}')
        print(f'Transaction Successful \nAmount: Rs. {amount} is paid!')
        self.status = 'paid'

class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, securityCode):
        self.securityCode = securityCode
        self.status = ''

    def payAmount(self, amount):
        print('Processng Debit Card...')
        print(f'Verifying Security Code {self.securityCode}')
        self.status = 'paid'


if __name__ == "__main__":
    newPayment = CreditPaymentProcessor('1234')
    newPayment.payAmount('1234')