# Probability Distribution Function and Its Types

## 1. Introduction

A **Probability Distribution Function (PDF)** describes how probabilities are distributed over the values of a random variable.

It tells us:

- Which values the variable can take
- How likely each value is

---

## 2. Types of Random Variables

There are two types of random variables:

1. **Discrete Random Variable**
2. **Continuous Random Variable**

---

## 3. Discrete Probability Distribution

### Definition

A **Discrete Probability Distribution** gives the probability of each possible value of a discrete random variable.

### Probability Mass Function (PMF)

P(X = x)

### Properties

- 0 ≤ P(X = x) ≤ 1
- Σ P(X = x) = 1

### Example

| X (Number of Heads) | P(X) |
| ------------------- | ---- |
| 0                   | 0.25 |
| 1                   | 0.50 |
| 2                   | 0.25 |

### Common Discrete Distributions

#### 1. Bernoulli Distribution

- Two outcomes: Success (1), Failure (0)
- Example: Single coin toss

#### 2. Binomial Distribution

- Repeated independent trials
- Formula:  
  P(X = k) = nCk _ p^k _ (1 - p)^(n - k)

#### 3. Poisson Distribution

- Models rare events
- Formula:  
  P(X = k) = (λ^k \* e^(-λ)) / k!

---

## 4. Continuous Probability Distribution

### Definition

A **Continuous Probability Distribution** describes probabilities over a continuous range of values.

### Probability Density Function (PDF)

f(x)

### Properties

- f(x) ≥ 0
- Total area under curve = 1
- P(a ≤ X ≤ b) = ∫[a to b] f(x) dx

### Common Continuous Distributions

#### 1. Uniform Distribution

- All values equally likely
- Formula:  
  f(x) = 1 / (b - a)

#### 2. Normal Distribution (Gaussian)

- Bell-shaped curve
- Formula:  
  f(x) = (1 / (σ√(2π))) \* e^(-(x - μ)^2 / (2σ^2))

#### 3. Exponential Distribution

- Time between events
- Formula:  
  f(x) = λe^(-λx)

---

## 5. Difference Between Discrete and Continuous

| Feature     | Discrete        | Continuous       |
| ----------- | --------------- | ---------------- |
| Values      | Countable       | Infinite (range) |
| Function    | PMF             | PDF              |
| Example     | No. of students | Height, weight   |
| Probability | Direct value    | Area under curve |

---

## 6. Cumulative Distribution Function (CDF)

### Definition

The **CDF** gives the probability that a random variable is less than or equal to a value.

F(x) = P(X ≤ x)

### Properties

- 0 ≤ F(x) ≤ 1
- Non-decreasing function
- F(∞) = 1

---

## 7. Summary

- Probability distributions describe how data behaves
- Two main types: Discrete (PMF) and Continuous (PDF)
- CDF gives cumulative probability
- Widely used in statistics, ML, and data analysis

---
