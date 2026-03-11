# Measure of Dispersion

## Definition

Measures of Dispersion describe how much the data values are **spread out around the central value (mean)**.  
They help in understanding the **variability or consistency** of a dataset.

Common measures of dispersion:

- Range
- Variance
- Standard Deviation
- Interquartile Range (IQR)

---

# 1. Range

Range is the difference between the **maximum and minimum value** in a dataset.

## Formula

Range = Maximum − Minimum

## Example

Data: 5, 8, 12, 20, 25

Maximum = 25  
Minimum = 5

Range = 25 − 5 = **20**

---

# 2. Variance

Variance measures the **average squared deviation of each data point from the mean**.

## Population Variance

\sigma^2 = \frac{\sum (X_i - \mu)^2}{N}

Where

- \( \sigma^2 \) = population variance
- \( X_i \) = population value
- \( \mu \) = population mean
- \( N \) = population size

### Example

Population Data: 2, 4, 6, 8

Mean \( \mu \) = 5

| Xi  | Xi − μ | (Xi − μ)² |
| --- | ------ | --------- |
| 2   | -3     | 9         |
| 4   | -1     | 1         |
| 6   | 1      | 1         |
| 8   | 3      | 9         |

Σ(Xi − μ)² = 20

Population Variance = 20 / 4 = **5**

---

## Sample Variance

::contentReference[oaicite:1]{index=1}

Where

- \( s^2 \) = sample variance
- \( \bar{x} \) = sample mean
- \( n \) = sample size

### Example

Sample Data: 3, 5, 7

Mean \( \bar{x} \) = 5

| Xi  | Xi − x̄ | (Xi − x̄)² |
| --- | ------ | --------- |
| 3   | -2     | 4         |
| 5   | 0      | 0         |
| 7   | 2      | 4         |

Σ(Xi − x̄)² = 8

Sample Variance = 8 / (3 − 1) = **4**

---

# 3. Standard Deviation

Standard deviation is the **square root of variance** and shows how much values deviate from the mean.

## Population Standard Deviation

\[
\sigma = \sqrt{\frac{\sum (X_i - \mu)^2}{N}}
\]

Example:  
Population variance = 5

σ = √5 ≈ **2.24**

---

## Sample Standard Deviation

\[
s = \sqrt{\frac{\sum (X_i - \bar{x})^2}{n-1}}
\]

Example:  
Sample variance = 4

s = √4 = **2**

---

# 4. Interquartile Range (IQR)

IQR measures the **spread of the middle 50% of the data**.

## Formula

IQR = Q3 − Q1

Where

- Q1 = first quartile (25th percentile)
- Q3 = third quartile (75th percentile)

## Example

Data: 2, 4, 6, 8, 10, 12, 14

Q1 = 4  
Q3 = 12

IQR = 12 − 4 = **8**

---

# Applications

Measures of dispersion are used in:

- Data analysis
- Finance risk analysis
- Machine learning
- Quality control
- Comparing consistency of datasets
