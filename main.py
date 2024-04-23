from questions.question1 import question1
from questions.question2 import question2

Q1LIMIT = 100
Q2LIMIT = 15

q1 = question1()
q2 = question2()

q2.calculateUntil(Q2LIMIT)

q2.showResults()