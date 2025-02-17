import streamlit as st
import numpy as np
import time
import pandas as pd
import plotly.express as px

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

with st.sidebar:
    st.header("Введите признаки: ")
    island = st.selectbox("Island", ('Torgersen', 'Dream', 'Biscore'))
    bill_length_mn = st.slider('Bill length (mn)', 32.1, 59.6, 44.5)
    bill_depth_mn = st.slider('Bill depth (mn)', 13.1, 21.5, 17.3)
    flipper_length_mn = st.slider('flipper length (mn)', 32.1, 59.6, 44.5)
    body_mass_g = st.slider('Body mass (g)',  32.1, 59.6, 44.5)
    gender = st.selectbox('Gender', ('female', 'male'))

st.subheader('Data Vis')
fig = px.scatter(
    df,
    x = 'bill_length_mn',
    y = 'bill_depth_mn',
    color = 'island',
    title = 'Bill length vs. Bill Depth by Island'
)

st.plotly_chart(fig)

fig2 = px.histogram(
    df,
    x = 'body_mass_g',
    nbins=30, 
    title = 'Distribution of Body Mass'
)

st.plotly_chart(fig2)



