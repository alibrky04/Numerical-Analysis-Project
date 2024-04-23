import math as m
import matplotlib.pyplot as plt
import numpy as np

class question1:
    def __init__(self, limit = 3):
        self.calculatedElements = [1, 1 - m.sqrt(3)]
        self.limit = limit
    
    def calculateUntil(self):
        for i in range(2, self.limit):
            newElement = 2 * (self.calculatedElements[i - 1] + self.calculatedElements[i - 2])
            self.calculatedElements.append(newElement)

    def showResult(self):
        for i in range(self.limit):
            print(f"Element {i + 1} : " + str(self.calculatedElements[i]))

        plt.plot(np.arange(1, 101), self.calculatedElements)
        plt.yscale('log')
        plt.xlabel('Element')
        plt.ylabel('Value')
        plt.title('Elements while x_n = (1 - sqrt(3))^(n-1)')

        custom_ticks = [1] + list(range(5, 101, 5))
        custom_tick_labels = [f'n{i}' for i in custom_ticks]
        plt.xticks(custom_ticks, custom_tick_labels)

        plt.grid(True)
        plt.show()