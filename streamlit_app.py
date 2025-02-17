import streamlit as st
import numpy as np
import time
import pandas as pd

st.title('My first webste')

st.write('Тут  я задеплою модель')

df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")

with st.expander('Date'):
    st.write('X')
    X_row = df.drop('species', axis=1)
    st.dataframe(X_row)

    st.write('y')
    y_row = df.species
    st.dataframe(y_row)
