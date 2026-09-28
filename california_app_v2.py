import numpy as np
import sklearn
import joblib
import streamlit as st

#-------------------------------
obj = joblib.load("california.joblib")
model = obj['model']
columns = obj['columns']
#-------------------------------
In=[]
for i in obj['columns']:
    v=st.number_input(f"Enter value for {i}")
    In.append(v)
Input=np.array([In])
out=model.predict(Input)
    
if st.button("Click"):
    st.success(f"The median house value is: {round(out[0],2)}")