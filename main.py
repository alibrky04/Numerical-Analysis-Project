from questions.question1 import question1
from questions.question2 import question2
from questions.question3 import question3

Q1LIMIT = 100
Q2LIMIT = 15
Q3LIMIT = 50

q1 = question1()
q2 = question2()
q3 = question3()

q1.calculateUntil(Q1LIMIT)
q2.calculateUntil(Q2LIMIT)
q3.calculateUntil(Q3LIMIT)
q3.showResults()