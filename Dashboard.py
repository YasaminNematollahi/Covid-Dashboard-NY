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


#select the location
clist = covid['location'].unique()
country = st.sidebar.multiselect("Select a country:",clist, default = ["Iran"])

#format="MM/DD/YY"
start_date = min(covid['date'])
end_date = max(covid['date'])

start_date2, end_date2 = st.date_input("Pick a date range", [start_date, end_date])
covid1 = covid.loc[(covid.date >= pd.to_datetime(start_date2)) & (covid.date <= pd.to_datetime(end_date2))]


# select the mode for data
mode = st.sidebar.radio(" Select the mode for displaying", ("Covid-19 cases","Covid-19 rolling average", "Covid-19 cumulated","Covid-19 deaths"))
#submode = st.si

if mode == "Covid-19 cases":
  fig = px.line(covid1[ covid1['location'].isin(country) ], x = "date", y = "new_cases_per_million", title = " and ".join(country), color = "location")
elif mode == "Covid-19 cumulated":
  fig = px.line(covid1[ covid1['location'].isin(country) ], x = "date", y = "total_cases_per_million", title = " and ".join(country), color = "location")
elif mode == "Covid-19 rolling average":
  fig = px.line(covid1[ covid1['location'].isin(country) ], x = "date", y = "new_cases_smoothed_per_million", title = " and ".join(country), color = "location")
elif mode == "Covid-19 deaths":
  fig = px.line(covid1[ covid1['location'].isin(country) ], x = "date", y = "total_deaths_per_million", title = " and ".join(country), color = "location")
st.plotly_chart(fig)
