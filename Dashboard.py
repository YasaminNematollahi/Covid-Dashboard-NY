"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.write("# COVID Dashboard")
st.write("#### Yasamin & Natalia")
df = pd.read_csv('owid-covid-data.csv',parse_dates=['date']) 
df
options=st.selectbox("Choose the value", df.location.unique,format_func=lambda x: display[x])
df_plot = df.loc[df.location == str(options)]

plt.figure(figsize=(15, 8))
plt.plot(df_plot.date,df_plot.new_cases)
plt.title('Evolution of number of new cases for France')
plt.legend(['Number of new cases'])
plt.show
#df.columns
#fig = plt.figure()
#plt.plot(df[df["Country/Region"]=="France"].iloc[[0]].iloc[:,4:].values[0])
# Plots the chart
st.pyplot(fig)
