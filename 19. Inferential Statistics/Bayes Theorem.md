# Bayes' Theorem

## 📌 Introduction

**Bayes' Theorem** is a fundamental concept in probability theory that helps us update the probability of an event based on new evidence.

👉 In simple terms:  
It tells us how to revise existing predictions when new data is available.

---

## 📐 Formula

\[
P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}
\]

Where:

- **P(A|B)** → Posterior probability (probability of A given B)
- **P(B|A)** → Likelihood (probability of B given A)
- **P(A)** → Prior probability (initial belief about A)
- **P(B)** → Evidence (total probability of B)

---

## 🧠 Intuition

Bayes' Theorem helps answer:

> "Given that event B has occurred, what is the probability that A was the cause?"

---

## ⚙️ Components Explained

### 1. Prior Probability (P(A))

- Initial belief before seeing evidence

### 2. Likelihood (P(B|A))

- How likely the evidence is if A is true

### 3. Evidence (P(B))

- Total probability of observing the evidence

### 4. Posterior Probability (P(A|B))

- Updated belief after considering evidence

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
- Test is 99% accurate:
  - P(Positive | Disease) = 0.99
  - P(Positive | No Disease) = 0.01

👉 Question:  
If a person tests positive, what is the probability they actually have the disease?

---

### Step 1: Define Events

- D = Disease
- T = Positive Test

---

### Step 2: Apply Bayes' Theorem

\[
P(D|T) = \frac{P(T|D) \cdot P(D)}{P(T)}
\]

---

### Step 3: Calculate P(T)

\[
P(T) = P(T|D) \cdot P(D) + P(T|\neg D) \cdot P(\neg D)
\]

\[
P(T) = (0.99 \cdot 0.01) + (0.01 \cdot 0.99)
\]

\[
P(T) = 0.0099 + 0.0099 = 0.0198
\]

---

### Step 4: Final Calculation

\[
P(D|T) = \frac{0.99 \cdot 0.01}{0.0198}
\]

\[
P(D|T) = \frac{0.0099}{0.0198} = 0.5
\]

---

### ✅ Result:

Even after testing positive, the probability of actually having the disease is **50%**.

👉 This shows how rare events affect probabilities.

---

## ⚡ Key Insights

- High accuracy does not guarantee high certainty
- Prior probability plays a crucial role
- Useful in decision-making under uncertainty

---

## 📍 Applications

- Medical diagnosis
- Spam filtering (Email classification)
- Machine Learning (Naive Bayes algorithm)
- Fraud detection
- Risk analysis

---

## 🆚 Conditional Probability vs Bayes' Theorem

| Feature  | Conditional Probability | Bayes' Theorem      |
| -------- | ----------------------- | ------------------- | ----------------------- |
| Purpose  | Basic probability       | Reverse probability |
| Formula  | P(A                     | B)                  | Uses prior + likelihood |
| Use Case | Direct calculation      | Updating beliefs    |

---

## 🧠 Real-Life Intuition

Imagine:

- You see smoke (evidence)
- What is the probability of fire (cause)?

Bayes' theorem helps answer this logically.

---

## ✅ Summary

- Bayes' Theorem updates probabilities using new evidence
- Combines prior knowledge with observed data
- Widely used in statistics, AI, and real-world decision making

---
