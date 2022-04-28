"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import datetime as dt

#cashing
@st.cache(allow_output_mutation = True)
def readdata(url): 
    data = pd.read_csv(url)
    data["date"] = pd.to_datetime(data["date"]).dt.date
    return data

st.write("# COVID Dashboard")
st.write("#### Yasamin & Natalia")

#read data with function readdata
covid = readdata('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')
covid

#pick up the date
start_date = min(covid['date'])
end_date = max(covid['date'])


st.write("##### Date range")
start_date2, end_date2 = st.date_input("Pick a date range", [start_date, end_date])
covid1 = covid.loc[(covid.date >= start_date2) & (covid.date <= end_date2)]


#select the location
clist = covid['location'].unique()
st.sidebar.header("Country")
country = st.sidebar.multiselect("Select a country:",clist, default = ["Iran"])

#select the mode for data Covid cases or deaths
st.sidebar.header("Mode")
mode = st.sidebar.radio(" Select the mode for displaying", ("Covid-19 cases","Covid-19 deaths"))
st.sidebar.header("Type of data")
typemode = st.sidebar.radio(" Select the type of data for displaying", ("New","Total","Average"))

if mode == "Covid-19 cases":
  if typemode == "New":
    fig = px.line(covid1[ covid1['location'].isin(country) ], x = "date", y = "new_cases_per_million", title = " and ".join(country), color = "location")
  elif typemode == "Total":
    fig = px.line(covid1[ covid1['location'].isin(country) ], x = "date", y = "total_cases_per_million", title = " and ".join(country), color = "location")    
  elif typemode == "Average":
    fig = px.line(covid1[ covid1['location'].isin(country) ], x = "date", y = "new_cases_smoothed_per_million", title = " and ".join(country), color = "location")
elif mode == "Covid-19 deaths":
  if typemode == "New":
    fig = px.line(covid1[ covid1['location'].isin(country) ], x = "date", y = "new_deaths_per_million", title = " and ".join(country), color = "location")
  elif typemode == "Total":
    fig = px.line(covid1[ covid1['location'].isin(country) ], x = "date", y = "total_deaths_per_million", title = " and ".join(country), color = "location")    
  elif typemode == "Average":
    fig = px.line(covid1[ covid1['location'].isin(country) ], x = "date", y = "new_deaths_smoothed_per_million", title = " and ".join(country), color = "location")

st.plotly_chart(fig)
