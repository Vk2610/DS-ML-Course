# Chi-Square (χ²) Test

## 📌 Introduction

The **Chi-Square Test** is a statistical test used to determine whether there is a **significant difference between observed and expected frequencies**.

👉 In simple terms:  
It checks whether the difference between actual data and expected data is due to **chance or not**.

---

## 📊 Types of Chi-Square Tests

### 1. Chi-Square Goodness of Fit Test

- Tests if sample data matches a population distribution

👉 Example:  
Is a dice fair?

---

### 2. Chi-Square Test of Independence

- Tests whether two categorical variables are related

👉 Example:  
Is gender related to product preference?

---

## 📐 Formula

χ² = Σ [ (O - E)² / E ]

Where:

- **O** → Observed frequency
- **E** → Expected frequency

---

## ⚙️ Mechanism (Step-by-Step)

### Step 1: State Hypotheses

- **H₀ (Null Hypothesis):** No difference / no association
- **H₁ (Alternative Hypothesis):** Significant difference / association exists

---

### Step 2: Calculate Expected Frequencies

For independence test:
E = (Row Total × Column Total) / Grand Total

---

### Step 3: Compute Chi-Square Statistic

χ² = Σ [ (O - E)² / E ]

---

### Step 4: Determine Degrees of Freedom (df)

- Goodness of Fit → df = n - 1
- Independence Test → df = (rows - 1)(columns - 1)

---

### Step 5: Compare with Critical Value or P-value

- If χ² > critical value → Reject H₀
- OR
- If p-value ≤ α → Reject H₀

---

### Step 6: Conclusion

Interpret results based on hypothesis decision

---

## 📍 Example (Goodness of Fit)

### Problem:

A dice is rolled 60 times with results:

| Outcome | Observed (O) |
| ------- | ------------ |
| 1       | 8            |
| 2       | 10           |
| 3       | 9            |
| 4       | 12           |
| 5       | 11           |
| 6       | 10           |

---

### Step 1: Expected Frequency

Since dice is fair:
E = 60 / 6 = 10

---

### Step 2: Calculate χ²

| Outcome | O   | E   | (O - E)² / E |
| ------- | --- | --- | ------------ |
| 1       | 8   | 10  | 0.4          |
| 2       | 10  | 10  | 0            |
| 3       | 9   | 10  | 0.1          |
| 4       | 12  | 10  | 0.4          |
| 5       | 11  | 10  | 0.1          |
| 6       | 10  | 10  | 0            |

χ² = 0.4 + 0 + 0.1 + 0.4 + 0.1 + 0  
χ² = 1.0

---

### Step 3: Degrees of Freedom

df = 6 - 1 = 5

---

### Step 4: Decision

At α = 0.05, critical value ≈ 11.07

Since 1.0 < 11.07 → Fail to reject H₀

---

### ✅ Result:

The dice is **fair** (no significant difference)

---

## ⚡ Key Assumptions

- Data is categorical
- Observations are independent
- Expected frequency ≥ 5 (preferably)

---

## 📍 Applications

- Survey analysis
- Market research
- Genetics
- Quality control
- Feature selection in Machine Learning

---

## 🆚 Goodness of Fit vs Independence Test

| Feature   | Goodness of Fit           | Independence Test    |
| --------- | ------------------------- | -------------------- |
| Purpose   | Compare with distribution | Check relationship   |
| Variables | One categorical           | Two categorical      |
| Example   | Dice fairness             | Gender vs preference |

---

## 🧠 Interpretation Tip

- Small χ² → Observed ≈ Expected (no difference)
- Large χ² → Big difference (significant)

---

## ✅ Summary

- Chi-Square test compares **observed vs expected values**
- Used for **categorical data analysis**
- Helps in testing **relationships and distributions**

---

# Chi-Square (χ²) Test — Solved Example

## 📌 Problem (Test of Independence)

A survey was conducted to check whether **gender** is related to **product preference**.

### Observed Data (O)

|              | Like Product | Dislike Product | Row Total |
| ------------ | ------------ | --------------- | --------- |
| Male         | 30           | 20              | 50        |
| Female       | 20           | 30              | 50        |
| Column Total | 50           | 50              | 100       |

---

## 🎯 Objective

Test whether **gender and product preference are independent**.

- **H₀ (Null Hypothesis):** Gender and preference are independent
- **H₁ (Alternative Hypothesis):** They are dependent

---

## ⚙️ Step 1: Calculate Expected Frequencies (E)

Formula:
E = (Row Total × Column Total) / Grand Total

### Expected Table

|        | Like Product     | Dislike Product  |
| ------ | ---------------- | ---------------- |
| Male   | (50×50)/100 = 25 | (50×50)/100 = 25 |
| Female | (50×50)/100 = 25 | (50×50)/100 = 25 |

---

## ⚙️ Step 2: Compute χ² Value

Formula:
χ² = Σ [ (O - E)² / E ]

| Cell             | O   | E   | (O - E)² / E |
| ---------------- | --- | --- | ------------ |
| Male - Like      | 30  | 25  | (5²)/25 = 1  |
| Male - Dislike   | 20  | 25  | (5²)/25 = 1  |
| Female - Like    | 20  | 25  | (5²)/25 = 1  |
| Female - Dislike | 30  | 25  | (5²)/25 = 1  |

χ² = 1 + 1 + 1 + 1  
χ² = 4

---

## ⚙️ Step 3: Degrees of Freedom

df = (rows - 1)(columns - 1)  
df = (2 - 1)(2 - 1) = 1

---

## ⚙️ Step 4: Decision Rule

- Significance level α = 0.05
- Critical value (χ²₀.₀₅,₁) ≈ 3.84

---

## ⚙️ Step 5: Conclusion

Since:
χ² = 4 > 3.84

👉 **Reject H₀**

---

## ✅ Final Result

There is a **significant relationship** between gender and product preference.

---

## 🧠 Interpretation

- Males tend to like the product more
- Females tend to dislike it more
- The difference is **not due to chance**

---

## 📌 Key Takeaways

- Chi-square test checks **association between categorical variables**
- Compare calculated χ² with critical value
- If χ² is larger → variables are **dependent**

---
