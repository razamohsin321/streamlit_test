import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Geochemistry')

st.write('*Data Science Course 2024*')

df = pd.read_csv('data/Bastar Craton.csv')

cat_names = df.columns.tolist()[27:]

col1, col2 = st.columns(2)

with col1:
    el1 = st.selectbox('Select Element 1' , cat_names)
    el2 = st.selectbox('Select Element 2' , cat_names)

with col2: 
    fig = plt.figure()
    plt.scatter(df[el1]/10000, (df[el2]/1000))
    st.pyplot(fig)

st.dataframe(df)

    

