"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\yasam\Covid-Dashboard-NY\time_series_covid19_confirmed_global.txt")
df