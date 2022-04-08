"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.write("# COVID Dashboard")
st.write("#### Yasamin & Natalia")
df = pd.read_csv(r"time_series_covid19_deaths_global.txt")
df
df.columns
fig = plt.figure()
plt.plot(df[df["Country/Region"]=="France"].iloc[[0]].iloc[:,4:].values[0])


# Plots the chart
st.pyplot(fig)