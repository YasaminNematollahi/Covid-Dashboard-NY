"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
st.write("# COVID Dashboard")
st.write("#### Yasamin & Natalia")

covid = pd.read_csv(r"C:\Users\yasam\Covid-Dashboard-NY\data.txt")
covid

covid['date'] = pd.to_datetime(covid['date'])
covid['year'] = covid['date'].dt.year
covid['month'] = covid['date'].dt.month

clist = covid['location'].unique()
country = st.sidebar.multiselect("Select a country:",clist, default = ["Iran"])

fig = px.line(covid[ covid['location'].isin(country) ], x = "date", y = "new_cases_per_million", title = " and ".join(country), color='location')
st.plotly_chart(fig)

st.slider("Time slider", min_value = min(covid['date']), max_value = max(covid["date"]),step = 1, value=covid['date'], format="MM/DD/YY")

fig1 = px.line(covid[ covid['location'].isin(country) ], x = "date", y = "new_deaths_per_million")
st.plotly_chart(fig1)

select_status = st.sidebar.radio("Covid-19 patient's status", ('Total Cases','New cases', 'New deaths', 'New tests'))

'''df1 = covid.groupby(by='continent')['people_fully_vaccinated_per_hundred'].sum()
df2 = df1.reset_index()
explode = (0, 0, 0, 0,0,0)  
labels =tuple(df2['continent'])
data = df2['people_fully_vaccinated_per_hundred']

fig1, ax1 = plt.subplots(figsize=(10, 8))
ax1.pie(data, explode=explode, labels=labels, autopct='%1.1f%%', radius=10000,
shadow=True, startangle=90)
ax1.axis('equal')  


st.pyplot(fig1)'''


'''st.sidebar.checkbox("Show analysis by country", True, key=1)
options = st.multiselect('Which country',covid.location.unique())


df_plot = covid.loc[covid.location == str(options)]
state_data = covid[covid['location'] == options]

select_status = st.sidebar.radio("Covid-19 patient's status", ('Total Cases','New cases', 'New deaths', 'New tests'))
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
'''