import math as m

class question1:
    def __init__(self):
        self.calculatedElements = [1, 1 - m.sqrt(3)]
    
    def calculateUntil(self, lastNumber = 3):
        for i in range(2, lastNumber):
            newElement = 2 * (self.calculatedElements[i - 1] + self.calculatedElements[i - 2])
            self.calculatedElements.append(newElement)