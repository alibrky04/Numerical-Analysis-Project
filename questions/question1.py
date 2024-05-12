import math as m
import matplotlib.pyplot as plt
import numpy as np

class question1:
    def __init__(self):
        self.calculatedElements = [1, 1 - m.sqrt(3)]
    
    def calculateUntil(self, limit = 3):
        l = len(self.calculatedElements)

        if limit <= 0:
            print("Limit must be a positive number!")
        elif limit <= l:
            print('Already reachead this index!\n')
            return

        for i in range(l, limit):
            newElement = 2 * (self.calculatedElements[i - 1] + self.calculatedElements[i - 2])
            self.calculatedElements.append(newElement)

    def showResults(self):
        l = len(self.calculatedElements)

        for i in range(l):
            print(f'x{i + 1} : ' + str(self.calculatedElements[i]))

        plt.figure(figsize=(6, 4), dpi=150)

        plt.plot(np.arange(1, l + 1), self.calculatedElements, label='$x_n = (1 - \sqrt{3})^{n-1}$')
        plt.yscale('log')
        plt.xlabel('$n$')
        plt.ylabel('$x_n$')
        plt.title('$x_n = (1 - \sqrt{3})^{n-1}$')

        custom_ticks = [1] + list(range(10, l + 1, 10))
        plt.xticks(custom_ticks)

        plt.grid(linewidth=0.25)
        
        plt.legend()

        plt.show()

        plt.figure(figsize=(6, 4), dpi=150)

        plt.plot(np.arange(1, l + 1), self.calculatedElements, label='$x_n = (1 - \sqrt{3})^{n-1}$')
        plt.xlabel('$n$')
        plt.ylabel('$x_n$')
        plt.title('$x_n = (1 - \sqrt{3})^{n-1}$')

        plt.xticks(custom_ticks)

        plt.ylim(-1, 1)
        plt.grid(linewidth=0.25)

        plt.legend()

        plt.show()