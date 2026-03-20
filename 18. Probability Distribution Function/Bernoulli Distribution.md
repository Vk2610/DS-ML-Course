# Bernoulli Distribution

## 1. Definition

The **Bernoulli Distribution** is a discrete probability distribution that models a random experiment with only **two possible outcomes**:

- Success (1)
- Failure (0)

It is one of the simplest distributions in probability theory.

---

## 2. Notation

A random variable \( X \) follows a Bernoulli distribution if:

\[
X \sim \text{Bernoulli}(p)
\]

Where:

- \( p \) = probability of success (1)
- \( 1 - p \) = probability of failure (0)

---

## 3. Probability Mass Function (PMF)

\[
P(X = x) =
\begin{cases}
p & \text{if } x = 1 \\
1 - p & \text{if } x = 0
\end{cases}
\]

Or in compact form:

\[
P(X = x) = p^x (1 - p)^{1 - x}, \quad x \in \{0,1\}
\]

---

## 4. Mean (Expected Value)

\[
E(X) = p
\]

---

## 5. Variance

\[
Var(X) = p(1 - p)
\]

---

## 6. Standard Deviation

\[
\sigma = \sqrt{p(1 - p)}
\]

---

## 7. Properties

- Only **two outcomes**: 0 or 1
- It is a special case of the **Binomial Distribution** with \( n = 1 \)
- Used for modeling binary experiments
- Completely defined by a single parameter \( p \)

---

## 8. Examples

### Example 1: Coin Toss

Let:

- Success = Head (1)
- Failure = Tail (0)
- \( p = 0.5 \)

Then:

- \( P(X = 1) = 0.5 \)
- \( P(X = 0) = 0.5 \)

---

### Example 2: Exam Pass/Fail

Let:

- Success = Pass (1)
- Failure = Fail (0)
- \( p = 0.7 \)

Then:

- \( P(X = 1) = 0.7 \)
- \( P(X = 0) = 0.3 \)

---

### Example 3: Light Bulb Test

Let:

- Success = Bulb works (1)
- Failure = Bulb defective (0)
- \( p = 0.9 \)

---

## 9. Real-Life Applications

- Coin toss experiments
- Yes/No surveys
- Pass/Fail results
- Quality testing (defective or not)
- Machine learning (binary classification)

---

## 10. Relation with Binomial Distribution

If we repeat a Bernoulli experiment **n times**, it becomes a:

\[
\text{Binomial Distribution}
\]

So,

- Bernoulli = Single trial
- Binomial = Multiple trials

---

## 11. Key Summary

| Concept         | Value                 |
| --------------- | --------------------- |
| Type            | Discrete Distribution |
| Outcomes        | 0 or 1                |
| Parameter       | \( p \)               |
| Mean            | \( p \)               |
| Variance        | \( p(1 - p) \)        |
| Special Case Of | Binomial (n = 1)      |

---

## 12. Visualization Insight

- If \( p \) is high → more chances of success (1)
- If \( p \) is low → more chances of failure (0)

---

## 13. Conclusion

The Bernoulli distribution is the **foundation of many statistical models**.  
It is simple but extremely powerful in modeling **binary outcomes** and is widely used in statistics, data science, and machine learning.

---
