import streamlit as st
import pandas as pd

data=pd.read_csv("capstone.csv")
st.table(data)