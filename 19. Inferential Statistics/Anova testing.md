# Hypothesis Testing in ANOVA (with Example)

## 📌 Introduction
**ANOVA (Analysis of Variance)** is used to test whether the means of **three or more groups** are equal.

👉 In hypothesis testing, ANOVA checks:
> "Is the difference between group means statistically significant?"

---

## 🎯 Hypotheses in ANOVA

- **H₀ (Null Hypothesis):** All group means are equal  
  μ₁ = μ₂ = μ₃ = ... = μₖ  

- **H₁ (Alternative Hypothesis):** At least one mean is different  

---

## 📐 Test Statistic

F = MSB / MSW  

Where:
- **MSB** → Mean Square Between groups  
- **MSW** → Mean Square Within groups  

👉 Larger F → greater difference between groups  

---

## ⚙️ Mechanism (Step-by-Step Hypothesis Testing)

### Step 1: State Hypotheses
Define H₀ and H₁  

---

### Step 2: Choose Significance Level
Usually α = 0.05  

---

### Step 3: Calculate Group Means & Overall Mean

---

### Step 4: Compute Variations
- SSB (Between groups)  
- SSW (Within groups)  

---

### Step 5: Compute Mean Squares
- MSB = SSB / df_between  
- MSW = SSW / df_within  

---

### Step 6: Calculate F-statistic
F = MSB / MSW  

---

### Step 7: Decision Rule
- If F > F-critical → Reject H₀  
- Else → Fail to reject H₀  

---

## 📍 Solved Example

### Problem:
Test whether the mean marks of students from 3 groups are equal.

| Group A | Group B | Group C |
|--------|--------|--------|
| 10     | 20     | 30     |
| 12     | 22     | 32     |
| 14     | 24     | 34     |

---

## ⚙️ Step 1: Hypotheses
- H₀: μ₁ = μ₂ = μ₃  
- H₁: At least one mean is different  

---

## ⚙️ Step 2: Means
- Mean A = 12  
- Mean B = 22  
- Mean C = 32  
- Overall Mean = 22  

---

## ⚙️ Step 3: Between-Group Variation (SSB)

SSB = 3[(12−22)² + (22−22)² + (32−22)²]  
SSB = 3[100 + 0 + 100]  
SSB = 600  

---

## ⚙️ Step 4: Within-Group Variation (SSW)

Group A: (10−12)² + (12−12)² + (14−12)² = 4 + 0 + 4 = 8  
Group B: 4 + 0 + 4 = 8  
Group C: 4 + 0 + 4 = 8  

SSW = 8 + 8 + 8 = 24  

---

## ⚙️ Step 5: Degrees of Freedom
- df_between = k - 1 = 3 - 1 = 2  
- df_within = N - k = 9 - 3 = 6  

---

## ⚙️ Step 6: Mean Squares
- MSB = 600 / 2 = 300  
- MSW = 24 / 6 = 4  

---

## ⚙️ Step 7: F-statistic
F = 300 / 4 = 75  

---

## ⚙️ Step 8: Decision
At α = 0.05, F-critical (2,6) ≈ 5.14  

Since:
F = 75 > 5.14  

👉 Reject H₀  

---

## ✅ Final Conclusion
There is a **significant difference** between the group means.

---

## 🧠 Interpretation
- The variation between groups is much larger than within groups  
- Hence, the difference is **not due to chance**

---

## ⚡ Key Points
- ANOVA tests **equality of multiple means**  
- Uses **F-statistic for decision making**  
- Reject H₀ if F is large  

---

## 🆚 ANOVA Hypothesis vs Other Tests

| Test Type        | Hypothesis Structure                  |
|------------------|--------------------------------------|
| Z-test / T-test  | μ = μ₀                               |
| Chi-square       | Observed = Expected                  |
| ANOVA            | μ₁ = μ₂ = μ₃ = ... = μₖ              |

---

## 📍 Applications
- Comparing teaching methods  
- Product performance analysis  
- Clinical trials  
- Machine Learning experiments  

---

## ✅ Summary
- ANOVA is used for hypothesis testing of **multiple means**  
- Based on comparing **between vs within variance**  
- Decision depends on **F-value**

---