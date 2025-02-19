import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot
import seaborn as sns
sns.set()

st.title("CAPSTONE FINANCIAL REPORTS")

st.image("FINANCIAL.jpg")


data=pd.read_csv("CAPSTONEDATA.csv")
st.write("Sales Per Country")

st.line_chart(data,x="COUNTRY",y="PROFITAFTERTAX")


st.divider()

import matplotlib.pyplot as plt

# Data
data=pd.read_csv("CAPSTONEDATA.csv")

# Create bar chart
plt.bar('Country','PROFITAFTERTAX')

# Labels and title
plt.xlabel('country')
plt.ylabel('PROFITAFTERTAX')


# Show plot
plt.show()



