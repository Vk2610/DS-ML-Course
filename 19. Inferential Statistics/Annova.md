# ANOVA (Analysis of Variance)

## 📌 Introduction

**ANOVA (Analysis of Variance)** is a statistical method used to compare the **means of three or more groups** to determine if at least one group mean is significantly different.

👉 In simple terms:  
It tells whether the differences between group averages are **real or due to chance**.

---

## 🎯 Objective

- Test if multiple group means are equal
- Avoid multiple t-tests (which increase error)

---

## 📊 Types of ANOVA

### 1. One-Way ANOVA

- Compares means of groups based on **one factor**

👉 Example: Comparing marks of students from 3 different classes

---

### 2. Two-Way ANOVA

- Compares means based on **two factors**

👉 Example: Effect of gender and study method on performance

---

## 📐 Hypotheses

- **H₀ (Null Hypothesis):** All group means are equal
- **H₁ (Alternative Hypothesis):** At least one mean is different

---

## 📐 Key Concept

ANOVA compares:

- **Between-group variation** (differences among group means)
- **Within-group variation** (variation inside each group)

---

## 📐 Formula

F = (Between-group variance) / (Within-group variance)

👉 If F is large → significant difference exists

---

## ⚙️ Mechanism (Step-by-Step)

### Step 1: State Hypotheses

Define H₀ and H₁

---

### Step 2: Calculate Group Means and Overall Mean

---

### Step 3: Calculate Variations

- Sum of Squares Between (SSB)
- Sum of Squares Within (SSW)

---

### Step 4: Compute Mean Squares

- MSB = SSB / df_between
- MSW = SSW / df_within

---

### Step 5: Calculate F-statistic

F = MSB / MSW

---

### Step 6: Decision

- If F > critical value → Reject H₀
- Else → Fail to reject H₀

---

## 📍 Example

### Problem:

Test whether the average marks of students from 3 groups are equal.

| Group A | Group B | Group C |
| ------- | ------- | ------- |
| 10      | 20      | 30      |
| 12      | 22      | 32      |
| 14      | 24      | 34      |

---

### Step 1: Calculate Means

- Mean A = 12
- Mean B = 22
- Mean C = 32
- Overall Mean = 22

---

### Step 2: Calculate SSB (Between)

SSB = 3[(12−22)² + (22−22)² + (32−22)²]  
SSB = 3[100 + 0 + 100]  
SSB = 600

---

### Step 3: Calculate SSW (Within)

Group A: (10−12)² + (12−12)² + (14−12)² = 4 + 0 + 4 = 8  
Group B: 4 + 0 + 4 = 8  
Group C: 4 + 0 + 4 = 8

SSW = 8 + 8 + 8 = 24

---

### Step 4: Degrees of Freedom

- df_between = k - 1 = 3 - 1 = 2
- df_within = N - k = 9 - 3 = 6

---

### Step 5: Mean Squares

- MSB = 600 / 2 = 300
- MSW = 24 / 6 = 4

---

### Step 6: F-value

F = 300 / 4 = 75

---

### Step 7: Decision

F is very large → Reject H₀

---

## ✅ Result

There is a **significant difference** between group means.

---

## ⚡ Assumptions

- Samples are independent
- Data is normally distributed
- Variances are equal (homogeneity)

---

## 🆚 ANOVA vs T-Test

| Feature       | T-Test         | ANOVA                  |
| ------------- | -------------- | ---------------------- |
| Groups        | 2              | 3 or more              |
| Purpose       | Compare means  | Compare multiple means |
| Error Control | Less efficient | More efficient         |

---

## 📍 Applications

- Education (student performance)
- Business (product comparison)
- Medicine (drug effectiveness)
- Machine Learning (feature comparison)

---

## 🧠 Interpretation Tip

- Small F → groups are similar
- Large F → at least one group differs

---

## ✅ Summary

- ANOVA compares **multiple group means**
- Uses variance to detect differences
- Helps avoid repeated t-tests
- Decision based on **F-statistic**

---
