"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name,contract,basePay,hours,commission,bonusPay,cPay,cAmount):
        self.name = name
        self.basePay = basePay
        self.pay = 0
        self.hours = hours
        self.contractType = contract
        self.commissionType = commission
        self.bonusPay = bonusPay
        self.contractPay = cPay
        self.contractAmount = cAmount


    def getCommission(self):
        if self.commissionType == "commission":
            return self.contractPay*self.contractAmount
        elif self.commissionType == "bonus":
            return self.bonusPay
        else:
            return 0

    def textCheck(self):
        if self.commissionType == "commission":
            return f" and receives a commission for {self.contractAmount}(s) at {self.contractPay}/contract."
        elif self.commissionType == "bonus":
            return f" and receives a bonus commission of {self.bonusPay}"
        else:
            return "."

    def get_pay(self):
        if self.contractType==("hour"):
            self.pay = self.hours*self.basePay
        elif self.contractType==("month"):
            self.pay = self.basePay

        self.pay += self.getCommission()

        return self.pay

    def __str__(self):
        if self.contractType == "hour":
            finalText =  f"{self.name} works on a {self.hours} at {self.basePay}/hour"
            finalText += self.textCheck()
        else:
            finalText =  f"{self.name} works on monthly salary of {self.basePay}"
            finalText+= self.textCheck()

        finalText += f" Their total pay is {self.pay}."
        print(finalText)
        return finalText



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee("Billie","month",4000,0,"",0,0,0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',"hour",25,100,"",0,0,0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',"month",3000,0,"commission",0,200,4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',"hour",25,150,"commission",0,220,3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',"month",2000,0,"bonus",1500,0,0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',"hour",30,120,"bonus",600,0,0)

billie.get_pay()
billie.__str__()
charlie.__str__()
renee.__str__()
jan.__str__()
robbie.__str__()
ariel.__str__()
