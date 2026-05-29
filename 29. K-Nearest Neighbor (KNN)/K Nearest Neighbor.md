# Introduction to K-Nearest Neighbors (KNN)

## What is K-Nearest Neighbors (KNN)?

K-Nearest Neighbors (KNN) is one of the simplest and most intuitive Machine Learning algorithms used for both:

- Classification Problems
- Regression Problems

KNN is a **supervised learning algorithm**, meaning it learns from labeled training data.

Unlike many other algorithms, KNN does not build a mathematical model during training. Instead, it stores the entire training dataset and makes predictions by finding the nearest data points to a new observation.

Because of this, KNN is known as a:

> **Lazy Learning Algorithm** or **Instance-Based Learning Algorithm**

---

# Real-Life Intuition

Imagine you move to a new neighborhood and want to know whether the area is safe.

You ask the people living nearest to you:

- If most neighbors say the area is safe → you conclude it is safe.
- If most neighbors say it is unsafe → you conclude it is unsafe.

KNN works exactly the same way.

It predicts a new data point based on the labels of its nearest neighbors.

---

# Why is it Called K-Nearest Neighbors?

- **K** = Number of nearest neighbors considered.
- **Nearest** = Closest data points based on distance.
- **Neighbors** = Existing training examples.

Example:

If K = 5

The algorithm finds the 5 nearest data points and uses their labels to make a prediction.

---

# How KNN Works

Suppose we have two classes:

- Red Circle
- Blue Square

A new data point arrives.

The algorithm:

### Step 1

Choose a value of K.

Example:

```text
K = 3
```

### Step 2

Calculate distance from the new point to every training point.

### Step 3

Sort distances in ascending order.

### Step 4

Select the K nearest neighbors.

### Step 5

Perform voting.

If majority belong to Red Circle:

```text
Prediction = Red Circle
```

If majority belong to Blue Square:

```text
Prediction = Blue Square
```

---

# Distance Metrics in KNN

Distance calculation is the most important part of KNN.

---

## 1. Euclidean Distance

Most commonly used distance metric.

Formula:

```math
d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}
```

### Example

Point A = (2,3)

Point B = (6,7)

Distance:

```math
d = \sqrt{(6-2)^2 + (7-3)^2}
```

```math
d = \sqrt{16+16}
```

```math
d = \sqrt{32}
```

```math
d \approx 5.66
```

---

## 2. Manhattan Distance

Measures distance along grid lines.

Formula:

```math
d = |x_2-x_1| + |y_2-y_1|
```

### Example

A = (2,3)

B = (6,7)

```math
d = |6-2| + |7-3|
```

```math
d = 4+4
```

```math
d = 8
```

---

## 3. Minkowski Distance

Generalized form of Euclidean and Manhattan distance.

Formula:

```math
d = \left(\sum |x_i-y_i|^p\right)^{1/p}
```

Special cases:

- p = 1 → Manhattan Distance
- p = 2 → Euclidean Distance

---

# KNN Classification Example

Suppose we want to predict whether a fruit is:

- Apple
- Orange

Training Data:

| Weight (g) | Color Score | Fruit  |
| ---------- | ----------- | ------ |
| 150        | 7           | Apple  |
| 170        | 8           | Apple  |
| 130        | 5           | Orange |
| 120        | 4           | Orange |

New Fruit:

```text
Weight = 160g
Color Score = 7
```

---

## Step 1: Choose K

```text
K = 3
```

---

## Step 2: Calculate Distances

Distance from new fruit to all training fruits.

Suppose results are:

| Fruit  | Distance |
| ------ | -------- |
| Apple  | 10       |
| Apple  | 15       |
| Orange | 32       |
| Orange | 40       |

---

## Step 3: Select Nearest 3 Neighbors

Nearest neighbors:

```text
Apple
Apple
Orange
```

---

## Step 4: Voting

Votes:

```text
Apple = 2
Orange = 1
```

Prediction:

```text
Apple
```

---

# KNN Regression Example

KNN can also predict numerical values.

Suppose:

| House Size (sq ft) | Price ($) |
| ------------------ | --------- |
| 1000               | 100000    |
| 1200               | 120000    |
| 1500               | 150000    |

Predict price for:

```text
1300 sq ft
```

Nearest houses:

```text
120000
150000
100000
```

Average:

```math
\frac{120000+150000+100000}{3}
```

```math
=123333
```

Predicted Price:

```text
$123,333
```

---

# Choosing the Right Value of K

Choosing K is very important.

---

## Small K

Example:

```text
K = 1
```

Advantages:

- Captures local patterns.

Disadvantages:

- Sensitive to noise.
- Can overfit.

---

## Large K

Example:

```text
K = 25
```

Advantages:

- More stable.

Disadvantages:

- May miss important patterns.
- Can underfit.

---

# Rule of Thumb

Common formula:

```math
K = \sqrt{N}
```

Where:

- N = Number of training samples

Example:

```math
N = 100
```

```math
K = \sqrt{100}
```

```math
K = 10
```

---

# Importance of Feature Scaling

KNN depends heavily on distance calculations.

Suppose:

| Feature | Value  |
| ------- | ------ |
| Age     | 25     |
| Salary  | 500000 |

Salary dominates Age because its scale is much larger.

This can produce incorrect predictions.

Therefore feature scaling is mandatory.

Common methods:

- Standardization
- Normalization
- Min-Max Scaling

---

# Computational Complexity

Training Phase:

```text
O(1)
```

Almost no training required.

---

Prediction Phase:

```text
O(N)
```

Need to compare with every training point.

This makes KNN slower for very large datasets.

---

# Advantages of KNN

## 1. Easy to Understand

Simple and intuitive algorithm.

---

## 2. No Training Required

Stores training data directly.

---

## 3. Works for Classification and Regression

Very versatile.

---

## 4. Handles Non-Linear Data

Can model complex decision boundaries.

---

## 5. Naturally Multi-Class

Can classify multiple classes without modification.

---

# Disadvantages of KNN

## 1. Slow Prediction

Must calculate distances to all points.

---

## 2. Memory Intensive

Stores the entire dataset.

---

## 3. Sensitive to Noise

Outliers can affect predictions.

---

## 4. Sensitive to Feature Scaling

Requires normalization.

---

## 5. Curse of Dimensionality

Performance decreases as features increase.

---

# Curse of Dimensionality

As dimensions increase:

- Distances become less meaningful.
- Data points become sparse.
- Nearest neighbors become difficult to identify.

Example:

A dataset with:

```text
2 Features → Works Well
```

```text
100 Features → Performance Drops
```

This phenomenon is called:

> Curse of Dimensionality

---

# Applications of KNN

## 1. Recommendation Systems

Suggesting:

- Movies
- Products
- Music

---

## 2. Medical Diagnosis

Disease prediction based on similar patients.

---

## 3. Image Recognition

Classifying images based on nearest examples.

---

## 4. Handwriting Recognition

Digit recognition systems.

---

## 5. Fraud Detection

Finding suspicious transactions.

---

# KNN Workflow

## Step 1

Collect labeled data.

---

## Step 2

Clean dataset.

---

## Step 3

Perform feature scaling.

---

## Step 4

Choose K value.

---

## Step 5

Calculate distances.

---

## Step 6

Find nearest neighbors.

---

## Step 7

Perform voting (classification) or averaging (regression).

---

## Step 8

Evaluate performance.

Metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- RMSE (for regression)

---

# Comparison with Other Algorithms

| Algorithm           | Training Speed | Prediction Speed | Complexity |
| ------------------- | -------------- | ---------------- | ---------- |
| KNN                 | Very Fast      | Slow             | Simple     |
| Logistic Regression | Fast           | Fast             | Medium     |
| Decision Tree       | Medium         | Fast             | Medium     |
| Random Forest       | Slow           | Fast             | High       |
| SVM                 | Medium         | Medium           | High       |

---

# Summary

K-Nearest Neighbors (KNN) is a simple yet powerful supervised learning algorithm that makes predictions based on the nearest training examples.

Key concepts:

- Distance-based learning
- Classification and Regression
- No explicit training phase
- Sensitive to feature scaling
- Choice of K is critical

Despite being one of the oldest Machine Learning algorithms, KNN remains highly useful for understanding fundamental concepts of similarity-based learning.

---

# Key Takeaways

- KNN is a supervised learning algorithm.
- Uses nearest neighbors for prediction.
- Works for classification and regression.
- Distance metrics are crucial.
- Feature scaling is mandatory.
- Small K may overfit.
- Large K may underfit.
- Easy to implement and understand.

---

# Conclusion

K-Nearest Neighbors is often one of the first Machine Learning algorithms learned by beginners because of its simplicity and intuitive nature.

It teaches important Machine Learning concepts such as:

- Distance measurement
- Similarity learning
- Classification
- Regression
- Feature scaling

Although modern datasets often require more sophisticated algorithms, KNN remains an excellent foundation for understanding how Machine Learning models make predictions based on patterns in data.
