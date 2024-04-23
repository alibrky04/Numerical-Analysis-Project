from questions.question1 import question1
import matplotlib.pyplot as plt
import numpy as np

Q1LIMIT = 100

q1 = question1(Q1LIMIT)

q1.calculateUntil()

q1.showResult()