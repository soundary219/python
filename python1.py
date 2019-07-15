print("Hello WORLD")

for i in range(5):
    if i==3:
        continue
    print(i)
for i in range(5):
    if i==3:
        break
    print(i)
from datetime import datetime
'''print("hello world!")
for i in range(10):
    if i==3:
        break
    print("{}".format(i))
#shift+enter for working in interactive mode'''

class Employee():
    #class variable
    bonus=5000
    #parameterized constructor
    def __init__(self,name,salary):
        #instance variable
        self.name=name 
        self.salary=salary
    #instance method
    def getsalary(self):
        return self.salary
    #instance method
    def applyhike(self):
        self.salary=self.salary*1.04  #4% hike
        return self.salary
    # class method since uses class property 'bonus'
    @classmethod
    def setbonus(cls,amount):
        cls.bonus=amount
    #
    @staticmethod
    def isworkingday():
        #local variable
        day=datetime.now().strftime('%w')
        if day=='0' or day=='6':
            return False
        else:
            return True
    def __str__(self):
        return self.name
    def __add__(self,other):
        return self.salary+other.salary
class Developer(Employee):
    def __init__(self,name,salary,stack):
        self.stack=stack
        super().__init__(name,salary)
    def getstack(self):
        return self.stack
    """emp1=Employee('krishita',200000)
    emp2=Employee('riya',15000)
    print(emp1)
    print(emp2) #memorylocation
    print(emp1.getsalary())
    print(Employee.getsalary(emp1))
    print(emp1.applyhike())
    Employee.setbonus(10000)
    print(emp1.bonus)
    print(emp2.applyhike())
    print(emp1.__dict__)  #view properties of emp1 object
    print(emp2.__dict__)
    print(Employee.isworkingday())
    print(emp1+emp2)"""
if __name__== '__main__':
    dev1=Developer("sound",30000,"ss")
    print(dev1.getstack())
    print(dev1.getsalary())
    