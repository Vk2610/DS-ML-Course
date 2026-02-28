import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data
def load_data():
  iris = load_iris()
  df = pd.DataFrame(iris.data, columns=iris.feature_names)
  df['species'] = iris.target
  return df, iris.target_names

df,target_name=load_data()

model=RandomForestClassifier()
model.fit(df.iloc[:,:-1],df['species'])

st.sidebar.title("Input features")
sepal_length=st.sidebar.slider("Sepal Length",df['sepal length (cm)'].min(),df['sepal length (cm)'].max(),df['sepal length (cm)'].mean())
sepal_width=st.sidebar.slider("Sepal Width",df['sepal width (cm)'].min(),df['sepal width (cm)'].max(),df['sepal width (cm)'].mean())
petal_length=st.sidebar.slider("Petal Length",df['petal length (cm)'].min(),df['petal length (cm)'].max(),df['petal length (cm)'].mean())
petal_width=st.sidebar.slider("Petal Width",df['petal width (cm)'].min(),df['petal width (cm)'].max(),df['petal width (cm)'].mean())

input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

# prediction


prediction=model.predict(input_data)
prediction_proba=model.predict_proba(input_data)

st.subheader("Prediction")
st.write(target_name[prediction[0]])

st.subheader("Prediction Probability")
st.write(prediction_proba)