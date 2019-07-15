class Bank:
    def __init__(self):
        self.bal=5000

    def withdraw(self,val):
        if(self.bal>5000):
            self.bal=self.bal-val
        else:
            ("Cannot withdraw")

    def deposit(self,dp):
        self.bal=self.bal+dp


    def getbalance(self):
        print(self.bal)
    
bank=Bank()
bank1=Bank()
bank.deposit(2000)
bank.withdraw(500)
bank.getbalance()
bank1.deposit(3000)
bank1.withdraw(1000)
bank1.getbalance()
    