import csv
import pandas as pd
import streamlit as st
import numpy as np

def price():
    st.markdown("# Price ❄️")
    chart_data = pd.DataFrame(
        np.random.randn(20),
        columns=['a'])
    st.line_chart(chart_data)
    st.sidebar.markdown("# Price ❄️")
