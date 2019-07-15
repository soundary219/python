from abc import ABC,abstractmethod
import math
class shape(ABC):
    @abstractmethod
    def getArea():
        pass
class Circle(shape):
    def getArea(self):
        return math.pi*5*5
circle=Circle()
print(circle.getArea())