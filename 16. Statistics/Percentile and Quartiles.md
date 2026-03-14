# Percentiles and Quartiles

## Percentile

### Definition

A **Percentile** is a statistical measure indicating the value below which a given percentage of observations in a dataset falls. For example, the **80th percentile** means **80% of the data values are below that value** and **20% are above it**.

### Formula for Percentile Position

Pₖ = (k/100) × (n + 1)

Where:

- **Pₖ** = k-th percentile
- **k** = desired percentile (e.g., 25, 50, 90)
- **n** = number of observations

---

## Example of Percentile

Ordered dataset of exam scores:  
10, 15, 20, 25, 30, 35, 40, 45, 50, 55

Number of observations:  
n = 10

### Find the 25th Percentile

P25 = (25/100) × (10 + 1)  
P25 = 0.25 × 11  
P25 = 2.75

The value lies between the **2nd and 3rd observations**, so the **25th percentile lies between 15 and 20**.

---

# Quartiles

## Definition

**Quartiles** divide a dataset into **four equal parts**, helping describe the **spread and distribution of the data**.

There are **three quartiles**:

| Quartile | Meaning                                    |
| -------- | ------------------------------------------ |
| Q1       | First Quartile (25th percentile)           |
| Q2       | Second Quartile (Median / 50th percentile) |
| Q3       | Third Quartile (75th percentile)           |

---

## Quartile Formulas

Q1 = (n + 1) / 4  
Q2 = (n + 1) / 2  
Q3 = 3(n + 1) / 4

Where **n** = number of observations.

---

# Example of Quartiles

Dataset:  
5, 8, 12, 15, 18, 20, 22, 25, 30

Number of observations:  
n = 9

### First Quartile (Q1)

Q1 = (9 + 1) / 4  
Q1 = 10 / 4  
Q1 = 2.5

Q1 lies between the **2nd and 3rd values**:

Q1 = (8 + 12) / 2 = 10

---

### Second Quartile (Q2 / Median)

Q2 = (9 + 1) / 2  
Q2 = 5

The **5th value = 18**

Median = 18

---

### Third Quartile (Q3)

Q3 = 3(9 + 1) / 4  
Q3 = 30 / 4  
Q3 = 7.5

Q3 lies between the **7th and 8th values**:

Q3 = (22 + 25) / 2 = 23.5

---

# Summary

| Measure    | Description                       |
| ---------- | --------------------------------- |
| Percentile | Divides data into 100 equal parts |
| Quartiles  | Divide data into 4 equal parts    |
| Q1         | 25th percentile                   |
| Q2         | Median (50th percentile)          |
| Q3         | 75th percentile                   |

---

# Applications

- Exam score analysis
- Data distribution analysis
- Box plot visualization
- Statistical comparison of datasets
