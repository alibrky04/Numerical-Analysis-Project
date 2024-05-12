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

        x_axis = [self.inputBaseValue**-i for i in range(1, l+1)]

        fig, (f, g) = plt.subplots(1, 2, figsize=(12, 6))

        bar_width = 0.35
        x_axis = np.arange(len(x_axis))

        f.bar(x_axis, self.fResults, color='skyblue', width=bar_width, label='f')
        f.set_title('$f(x) = \sqrt{x^2 + 1} - 1$', fontsize=15)
        f.set_yscale('log')
        f.set_xlabel('$x$', fontsize=12)
        f.set_ylabel('$f(x)$', fontsize=12)
        f.set_xticks(x_axis)
        f.set_xticklabels([f'$8^{{-{i + 1}}}$' for i in range(l)])

        g.bar(x_axis, self.gResults, color='salmon', width=bar_width, label='g')
        g.set_title('$g(x) = \\frac{x^2}{\sqrt{x^2 + 1} + 1}$', fontsize=15)
        g.set_yscale('log')
        g.set_xlabel('$x$', fontsize=12)
        g.set_ylabel('$g(x)$', fontsize=12)
        g.set_xticks(x_axis)
        g.set_xticklabels([f'$8^{{-{i + 1}}}$' for i in range(l)])

        plt.tight_layout()

        f.grid(linewidth=0.25)
        g.grid(linewidth=0.25)

        f.legend()
        g.legend()

        plt.show()