"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.express as px


st.write("# COVID Dashboard")
st.write("#### Yasamin & Natalia")
<<<<<<< HEAD
df = pd.read_csv('owid-covid-data.csv',parse_dates=['date']) 
df
#df.columns
#fig = plt.figure()
#plt.plot(df[df["Country/Region"]=="France"].iloc[[0]].iloc[:,4:].values[0])
# Plots the chart
#st.pyplot(fig)
=======

covid = pd.read_csv(r"data.txt")
covid

covid['date'] = pd.to_datetime(covid['date'])
covid['year'] = covid['date'].dt.year
covid['month'] = covid['date'].dt.month

clist = covid['location'].unique()
country = st.sidebar.selectbox("Select a country:",clist)

fig = px.line(covid[covid['location'] == country], x = "date", y = "new_cases_per_million", title = country)
st.plotly_chart(fig)

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


st.sidebar.checkbox("Show analysis by country", True, key=1)
options = st.multiselect('Which country',covid.location.unique())


df_plot = covid.loc[covid.location == str(options)]
state_data = covid[covid['location'] == options]

select_status = st.sidebar.radio("Covid-19 patient's status", ('Total Cases','New cases', 'New deaths', 'New tests'))

plt.figure(figsize=(15, 8))
plt.plot(df_plot.date,df_plot.new_cases)
plt.title('Evolution of number of new cases for France')
plt.legend(['Number of new cases'])
plt.show
st.pyplot()


def get_total_dataframe(dataset):
    total_dataframe = pd.DataFrame({
    'Status':['Total Cases', 'New cases', 'New deaths','New tests'],
    'Number of cases':(dataset.iloc[0]['total_cases'],
    dataset.iloc[0]['new_cases'], 
    dataset.iloc[0]['new_deaths'],dataset.iloc[0]['new_tests'])})
    return total_dataframe

state_total = get_total_dataframe(state_data)

if st.sidebar.checkbox("Show Analysis by State", True, key=2):
    st.markdown("## **Covid analysis**")
    st.markdown("### Overall Cases, New cases, deaths and " +
    "Deceased cases in %s yet" % (options))
    if not st.checkbox('Hide Graph', False, key=1):
        state_total_graph = px.bar(
        state_total, 
        x='Status',
        y='Number of cases',
        labels={'Number of cases':'Number of cases in %s' % (options)},
        color='Status')
        st.plotly_chart(state_total_graph)


options1 = st.sidebar.selectbox('Select the date', covid.year.unique())

df_plot = covid.loc[covid.year == str(options1)]
state_data = covid[covid['year'] == options1]



'''plt.figure(figsize=(15, 8))
plt.plot(df_plot.date,df_plot.new_cases)
plt.title('Evolution of number of new cases for France')
plt.legend(['Number of new cases'])
plt.show
# Plots the chart
st.pyplot(fig)'''


>>>>>>> 437b8504dda9e438c8961410bfdb2c4bf1f32196
