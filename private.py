class Mobile:
    #dundar method(__eG__)
    def __init__(self):
        self.__maxPrice=9999
    def getPrice(self):
        print(self.__maxPrice)
    def setPrice(self,price):
        self.__maxPrice=price
mobile=Mobile()
#print(mobile.maxPrice)
mobile.getPrice()
mobile.setPrice(5000)
mobile.getPrice()































