# Confidence Interval & Margin of Error

## 📌 Introduction

In statistics, **Confidence Interval (CI)** and **Margin of Error (MOE)** are used to estimate a population parameter (like mean or proportion) from sample data.

👉 In simple terms:  
Instead of giving a single value, we give a **range of values** where the true value is likely to lie.

---

## 📊 Confidence Interval (CI)

### 🔹 Definition

A **Confidence Interval** is a range of values used to estimate an unknown population parameter with a certain level of confidence.

👉 Example:
Instead of saying average = 50  
We say → average is between **45 and 55 (95% confidence)**

---

### 📐 General Formula

Confidence Interval = Estimate ± Margin of Error

---

### 📌 Common Confidence Levels

- 90% Confidence Level
- 95% Confidence Level (most common)
- 99% Confidence Level

👉 Higher confidence → wider interval

---

## 📏 Margin of Error (MOE)

### 🔹 Definition

The **Margin of Error** tells how much the estimate can vary from the true population value.

👉 It defines the **radius of the confidence interval**

---

### 📐 Formula (for Mean)

MOE = Z \* (σ / √n)

Where:

- **Z** → Z-score (based on confidence level)
- **σ** → Population standard deviation
- **n** → Sample size

---

### 📊 Common Z-values

| Confidence Level | Z-value |
| ---------------- | ------- |
| 90%              | 1.645   |
| 95%              | 1.96    |
| 99%              | 2.576   |

---

## ⚙️ Step-by-Step Calculation

1. Choose confidence level
2. Find corresponding Z-value
3. Calculate standard error → (σ / √n)
4. Compute margin of error
5. Construct interval → Estimate ± MOE

---

## 📍 Example

### Problem:

- Sample mean (x̄) = 100
- Standard deviation (σ) = 15
- Sample size (n) = 25
- Confidence level = 95%

---

### Step 1: Z-value

For 95% → Z = 1.96

---

### Step 2: Calculate MOE

MOE = 1.96 _ (15 / √25)  
MOE = 1.96 _ (15 / 5)  
MOE = 1.96 \* 3  
MOE = 5.88

---

### Step 3: Confidence Interval

CI = 100 ± 5.88

CI = (94.12 , 105.88)

---

### ✅ Result:

We are **95% confident** that the true population mean lies between **94.12 and 105.88**

---

## ⚡ Key Insights

- Larger sample size → smaller margin of error
- Higher confidence level → larger margin of error
- More variability (σ) → wider interval

---

## 🆚 Confidence Interval vs Margin of Error

| Feature | Confidence Interval | Margin of Error     |
| ------- | ------------------- | ------------------- |
| Meaning | Range of values     | Half-width of range |
| Formula | Estimate ± MOE      | Z \* (σ / √n)       |
| Purpose | Estimate parameter  | Measure uncertainty |

---

## 📍 Real-Life Examples

- Election polls (e.g., ±3%)
- Survey results
- Quality testing in manufacturing
- Scientific experiments

---

## 🧠 Interpretation Tip

A 95% confidence level means:

> If we repeat the experiment many times, 95% of the intervals will contain the true value.

---

## ✅ Summary

- Confidence Interval gives a **range estimate**
- Margin of Error shows **uncertainty in estimate**
- Both are essential for **statistical inference and decision making**

---
