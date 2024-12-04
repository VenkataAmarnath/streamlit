# we try to create some interactive applications

import streamlit as st
import pandas as pd

st.title("Streamlit text input")

name=st.text_input("Enter your name: ")

if name:
    st.write(f"Hello {name}")


## Use slider

age=st.slider("Select your age:",0,100,25) # range(0 to 100), 25 is the default value as soon as web page loads
st.write(f"Your age is {age}.")


options=['Python','Java','C++','Javascript']
choice=st.selectbox("Choose your favourite language",options)
st.write(f"You selected {choice}.")


# for file upload

uploaded_file=st.file_uploader("choose a csv file",type='csv')

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)