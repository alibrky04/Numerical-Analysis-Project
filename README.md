# Numerical Analysis Project

This repository contains Python code to solve three mathematical questions. The questions are implemented as separate classes in the [questions](questions) module, each with its own calculation and visualization methods.

## Questions

### [Question 1](questions/question1.py)

**Description:** Calculates elements according to the recurrence relation: $x_n = 2 * (x_{n-1} + x_{n-2})$, where the initial elements are $x_0 = 1$ and $x_1 = 1 - \sqrt{3}$.

### [Question 2](questions/question2.py)

**Description:** Computes two functions ($f$ and $g$) for a given input base value. Functions are defined as follows:
- $f(x) = \sqrt{x^2 + 1} - 1$
- $g(x) = \frac{x^2}{\sqrt{x^2 + 1} + 1}$

### [Question 3](questions/question3.py)

**Description:** Calculates elements according to the recurrence relation: $x_{n+1} = \frac{13}{3}x_n - \frac{4}{3}x_{n-1}$, with initial elements $x_0 = 1$ and $x_1 = \frac{1}{3}$.

## Usage

To use the provided code:

1. Import the question classes from the [questions](questions.py) module.
2. Set limits for each question using the constants `Q1LIMIT`, `Q2LIMIT`, and `Q3LIMIT`.
3. Initialize instances of the question classes.
4. Call the `calculateUntil()` method for each question with the desired limit.
5. Optionally, call the `showResults()` method to display calculated elements and visualizations.

## Dependencies

- Python 3.x
- Required Python packages: `matplotlib`, `numpy`
