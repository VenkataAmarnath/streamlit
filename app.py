## https://streamlit.io/

## refer this site for help in streamlit


import streamlit as st
import pandas as pd
import numpy as np

## Title of application
st.title("Hello Streamlit")

## Display simple text
st.write("This is simple text")

## Create simple Dataframe

df=pd.DataFrame({
    'first_column':[1,2,3,4,5],
    'second column':[10,20,30,40,50]
})

## Display dataframe

st.write("Here is the dataframe")
st.write(df)

## create a line chart
chart_data=pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.line_chart(chart_data)