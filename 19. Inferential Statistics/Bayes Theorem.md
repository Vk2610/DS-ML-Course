# Bayes' Theorem

## 📌 Introduction

**Bayes' Theorem** is a fundamental concept in probability that helps us update the probability of an event based on new evidence.

👉 In simple terms:  
It tells us how to revise our belief when new information is available.

---

## 📐 Formula

P(A | B) = (P(B | A) \* P(A)) / P(B)

Where:

- **P(A | B)** → Posterior probability (probability of A given B)
- **P(B | A)** → Likelihood (probability of B given A)
- **P(A)** → Prior probability (initial belief about A)
- **P(B)** → Evidence (total probability of B)

---

## 🧠 Intuition

Bayes' Theorem answers:

> "Given that event B has occurred, what is the probability that A caused it?"

---

## ⚙️ Components Explained

### 1. Prior Probability (P(A))

- Initial assumption before observing data

### 2. Likelihood (P(B | A))

- How likely the evidence is if A is true

### 3. Evidence (P(B))

- Total probability of observing the evidence

### 4. Posterior Probability (P(A | B))

- Updated probability after considering evidence

---

## 📊 Step-by-Step Working

1. Start with prior probability
2. Multiply by likelihood
3. Divide by total probability of evidence
4. Get updated probability (posterior)

---

## 📍 Example (Medical Test)

### Problem:

- 1% of people have a disease → P(D) = 0.01
- Test accuracy:
  - P(Positive | Disease) = 0.99
  - P(Positive | No Disease) = 0.01

👉 Question:  
If a person tests positive, what is the probability they actually have the disease?

---

### Step 1: Define Events

- D = Disease
- T = Positive Test

---

### Step 2: Calculate Total Probability of Positive Test

P(T) = (P(T | D) _ P(D)) + (P(T | not D) _ P(not D))

P(T) = (0.99 _ 0.01) + (0.01 _ 0.99)  
P(T) = 0.0099 + 0.0099  
P(T) = 0.0198

---

### Step 3: Apply Bayes' Theorem

P(D | T) = (P(T | D) \* P(D)) / P(T)

P(D | T) = (0.99 \* 0.01) / 0.0198  
P(D | T) = 0.0099 / 0.0198  
P(D | T) = 0.5

---

### ✅ Result:

Even after testing positive, the probability of actually having the disease is **50%**.

👉 This happens because the disease is rare.

---

## ⚡ Key Insights

- High test accuracy ≠ high certainty
- Prior probability plays a major role
- Important in decision-making under uncertainty

---

## 📍 Applications

- Medical diagnosis
- Email spam filtering
- Machine Learning (Naive Bayes)
- Fraud detection
- Risk analysis

---

## 🆚 Conditional Probability vs Bayes' Theorem

## 🆚 Conditional Probability vs Bayes' Theorem

| Feature  | Conditional Probability | Bayes' Theorem          |
| -------- | ----------------------- | ----------------------- |
| Purpose  | Direct probability      | Reverse probability     |
| Formula  | P(A \| B)               | Uses prior + likelihood |
| Use Case | Basic problems          | Updating beliefs        |

---

## 🧠 Real-Life Intuition

Imagine:

- You see smoke (evidence)
- What is the probability of fire (cause)?

Bayes' Theorem helps answer this logically.

---

## ✅ Summary

- Bayes' Theorem updates probability using new evidence
- Combines prior knowledge with observed data
- Widely used in statistics, AI, and real-world applications

---
