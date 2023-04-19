import streamlit as st #library which is used to turns data scripts into web page
import numpy as np #library used for working with arrays
import pandas as pd #library for data analysis 
import matplotlib.pyplot as plt # To visualize graphs
from sklearn.linear_model import LinearRegression

#Write arguments to the webpage
st.write("""
#  Marks Prediction App
This app predicts the **Marks** scored by the student on the basis of
**Time** spend to study the Subject
""")

#To have a sidebar in our webpage with arguments
st.sidebar.markdown('''
            Simple Marks Prediction App using Linear Regression 
            \n Applied Stats Project \n
            Team members - Ananya Singh \n 
            Shreenidhi Batta \n 
            Aryan Mankotia
    ''')

#Function to input from user
def user_input():
    hr = st.number_input("Number of Hours of Study")
    hr = np.array([[hr]]).astype(np.float64)
    return hr

pred = user_input()

#Loading dataset
data = pd.read_csv("marks.csv")
X = data.iloc[:, 0].values.reshape(-1, 1) # values converts it into a numpy array
Y = data.iloc[:, 1].values.reshape(-1, 1) # -1 means that calculate the dimension of rows, but have 1 column
LR = LinearRegression() # create object for the class
LR.fit(X, Y) # perform linear regression(training and testing)
Y_pred = LR.predict(X) # make predictions
plt.scatter(X,Y)
plt.title("Relation between Marks and Time spend to study that subject")
plt.xlabel("Time – spend on the subject in hrs")
plt.ylabel("Marks of the subject")
plt.plot(X, Y_pred, color='red')
plt.show()


prediction = round(float(LR.predict(pred)),2)   #round(number, digits)

if pred > 8.5:
    st.button("Predict")
    st.success("The Predicted Percentage is 99.00")
else:
    st.button("Predict")
    st.success("The Predicted Percentage is {}".format(prediction))
 