"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import datetime as dt

#cashing data
@st.cache(allow_output_mutation = True)

# function for reading data from url
def readdata(url): 
    data = pd.read_csv(url)
    return data

st.write("# COVID Dashboard")
st.write("#### Yasamin & Natalia")

#read data with function readdata
covid = readdata('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')
covid

covid['date'] = pd.to_datetime(covid['date'])
covid['year'] = covid['date'].dt.year
covid['month'] = covid['date'].dt.month

#select the location
clist = covid['location'].unique()
country = st.sidebar.multiselect("Select a country:",clist, default = ["Iran"])

format="MM/DD/YY"
start_date = min(covid['date'])
end_date = max(covid['date'])
#start_dt = st.sidebar.date_input('Start date', value=covid['date'].min())
#end_dt = st.sidebar.date_input('End date', value=covid['date'].max())
st.write(start_date)
st.write(end_date)
#slider = st.slider('Select date', min_value=start_date, value=end_date ,max_value=end_date)
start_date2, end_date2 = st.date_input("Pick a date range", [start_date, end_date])
covid1 = covid.loc[(covid.date >= pd.to_datetime(start_date2)) & (covid.date <= pd.to_datetime(end_date2))]
#covid1

# select the mode for data
mode = st.sidebar.radio("Select the mode for displaying", ("Covid-19 new cases", "Covid-19 cumulated number", "Covid-19 Weekly cases", "Covid-19 Deaths"))

if mode == "Covid-19 new cases":
  fig = px.line(covid1[ covid1['location'].isin(country) ], x = "date", y = "new_cases_per_million", title = " and ".join(country), color = "location")
elif mode == "Covid-19 cumulated number":
  fig = px.line(covid1[ covid1['location'].isin(country) ], x = "date", y = "total_cases_per_million", title = " and ".join(country), color = "location")
elif mode == "Covid-19 Weekly cases":
  fig = px.line(covid1[ covid1['location'].isin(country) ], x = "date", y = "weekly_hosp_admissions", title = " and ".join(country), color = "location")
elif mode == "Covid-19 Deaths":
  fig = px.line(covid1[ covid1['location'].isin(country) ], x = "date", y = "total_deaths_per_million", title = " and ".join(country), color = "location")
st.plotly_chart(fig)






#st.slider("Time slider", min_value=min(covid['date']), max_value=max(covid["date"]), format="MM/DD/YY - hh:mm")



st.sidebar.checkbox("Show analysis by country", True, key=1)
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