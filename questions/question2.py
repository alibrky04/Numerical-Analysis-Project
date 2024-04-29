import math as m
import matplotlib.pyplot as plt
import numpy as np

class question2:
    def __init__(self):
        self.fResults = []
        self.gResults = []
        self.inputBaseValue = 8

    def calculateUntil(self, limit = 1):
        l = len(self.fResults)

        if limit <= 0:
            print("Limit must be a positive number!")
        elif limit <= l:
            print('Already reachead this index!\n')
            return

        for i in range(l + 1, limit + 1):
            x = (self.inputBaseValue**-i)

            result = m.sqrt(x**2 + 1) - 1
            self.fResults.append(result)

            result = x**2 / (m.sqrt(x**2 + 1) + 1)
            self.gResults.append(result)

    def showResults(self):
        l = len(self.fResults)

        max_length = max(len(str(result)) for result in self.fResults + self.gResults)

        for i in range(l):
            fResult = str(self.fResults[i]).ljust(max_length)
            gResult = str(self.gResults[i]).ljust(max_length)
            print(f'f(8^-{i + 1}) : {fResult}\tg(8^-{i + 1}) : {gResult}')