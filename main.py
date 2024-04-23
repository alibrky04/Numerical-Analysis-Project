from questions.question1 import question1
import matplotlib.pyplot as plt
import numpy as np

Q1FINAL = 100

q1 = question1()

q1.calculateUntil(Q1FINAL)

for i in range(Q1FINAL):
    print(f"Element {i + 1} : " + str(q1.calculatedElements[i]))

plt.plot(np.arange(1, 101), q1.calculatedElements)
plt.yscale('log')
plt.xlabel('Element')
plt.ylabel('Value')
plt.title('Elements while x_n = (1 - sqrt(3))^(n-1)')

custom_ticks = [1] + list(range(5, 101, 5))
custom_tick_labels = [f'n{i}' for i in custom_ticks]
plt.xticks(custom_ticks, custom_tick_labels)

plt.grid(True)
plt.show()