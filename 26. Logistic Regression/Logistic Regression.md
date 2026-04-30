# Logistic Regression

Logistic Regression is a supervised machine learning algorithm used for classification tasks, especially when the target variable is categorical and often binary.[1][2] It estimates the probability of an outcome and maps that probability to a class label, commonly using a threshold such as 0.5.[3][4]

## Overview

Unlike linear regression, which predicts continuous values, logistic regression predicts probabilities between 0 and 1.[5][3] It uses the logistic or sigmoid function to transform a linear combination of input features into an output probability.[1][6]

## How It Works

Given input features, logistic regression computes a linear score:

```text
z = w1x1 + w2x2 + ... + b
```

That score is passed through the sigmoid function:

```text
p = 1 / (1 + e^-z)
```

The result is a probability value that can be converted into a class prediction.[1][3]

## Types

- **Binary logistic regression**: Used when there are two possible classes, such as spam or not spam.[5][2]
- **Multiclass logistic regression**: Used when there are more than two classes; implementations often support one-vs-rest or multinomial settings.[7][8]

## Common Applications

- Email spam detection.[3]
- Disease prediction in healthcare.[5][2]
- Customer churn prediction.[3]
- Loan approval or credit risk classification.[3]

## Advantages

- Simple and fast to train for many classification problems.[7]
- Produces probability outputs that are easy to interpret.[3]
- Works well as a baseline model for classification tasks.[6][4]
- Supports regularization in common libraries such as scikit-learn.[7]

## Limitations

- Assumes a linear relationship between input features and the log-odds of the outcome.[9][3]
- May underperform on highly complex non-linear problems.[5]
- Performance can depend on feature scaling and solver choice in practical implementations.[8][7]

## Example in Python

```python
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

X, y = load_iris(return_X_y=True)
model = LogisticRegression(random_state=0)
model.fit(X, y)

predictions = model.predict(X[:5])
probabilities = model.predict_proba(X[:5])
```

Scikit-learn provides a `LogisticRegression` class with support for regularization, multiple solvers, and probability prediction methods such as `predict_proba`.[7]

## Key Terms

- **Sigmoid function**: Converts any real-valued score into a number between 0 and 1.[6][3]
- **Log-odds (logit)**: The logarithm of the odds, modeled as a linear function of the features.[9][3]
- **Regularization**: A technique used to reduce overfitting, commonly available as L1 or L2 penalties.[10][7]

## When to Use

Use logistic regression when the goal is classification, the dataset is reasonably structured, and interpretability matters.[5][2] It is especially useful as a strong baseline before trying more complex machine learning models.
