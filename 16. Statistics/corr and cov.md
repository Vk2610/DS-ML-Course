# Correlation and Covariance

# Correlation and Covariance

## Covariance

### Definition

**Covariance** measures how two random variables change together.  
It indicates the **direction of the linear relationship** between variables.

- If covariance is **positive**, the variables increase or decrease together.
- If covariance is **negative**, one variable increases while the other decreases.
- If covariance is **zero**, the variables are not linearly related.

### Formula

Cov(X,Y) = Σ[(Xi - X̄)(Yi - Ȳ)] / n

Where:

- **Xi, Yi** = individual data values
- **X̄** = mean of X
- **Ȳ** = mean of Y
- **n** = number of observations

---

## Example of Covariance

Consider two variables:

| X   | Y   |
| --- | --- |
| 2   | 4   |
| 4   | 8   |
| 6   | 12  |

Step 1: Calculate means

X̄ = (2 + 4 + 6) / 3 = 4  
Ȳ = (4 + 8 + 12) / 3 = 8

Step 2: Apply covariance formula

| Xi  | Yi  | Xi - X̄ | Yi - Ȳ | (Xi - X̄)(Yi - Ȳ) |
| --- | --- | ------ | ------ | ---------------- |
| 2   | 4   | -2     | -4     | 8                |
| 4   | 8   | 0      | 0      | 0                |
| 6   | 12  | 2      | 4      | 8                |

Cov(X,Y) = (8 + 0 + 8) / 3 = **5.33**

Since covariance is **positive**, X and Y increase together.

---

# Correlation

## Definition

**Correlation** measures the **strength and direction of the relationship** between two variables.

Unlike covariance, correlation values are **standardized between -1 and +1**.

| Value | Meaning                      |
| ----- | ---------------------------- |
| +1    | Perfect positive correlation |
| 0     | No correlation               |
| -1    | Perfect negative correlation |

---

## Formula

r = Cov(X,Y) / (σx × σy)

Where:

- **r** = correlation coefficient
- **Cov(X,Y)** = covariance of X and Y
- **σx** = standard deviation of X
- **σy** = standard deviation of Y

---

## Example of Correlation

Consider the dataset:

| Study Hours (X) | Exam Score (Y) |
| --------------- | -------------- |
| 1               | 50             |
| 2               | 55             |
| 3               | 65             |
| 4               | 70             |
| 5               | 80             |

Observation:

As **study hours increase, exam scores increase**, indicating **positive correlation**.

The correlation coefficient **r** will be close to **+1**.

---

# Difference Between Covariance and Correlation

| Covariance                         | Correlation                     |
| ---------------------------------- | ------------------------------- |
| Measures direction of relationship | Measures strength and direction |
| Value can be any number            | Value ranges from -1 to +1      |
| Harder to interpret                | Easier to interpret             |

---

# Applications

Correlation and covariance are widely used in:

- Statistics and data analysis
- Machine learning
- Financial market analysis
- Economics and forecasting
- Risk management
