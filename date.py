import csv
import pandas as pd
import streamlit as st

def date():
    st.title("""
    MY_INVESTOR
    """)
    st.markdown("# Data 🎈")
    df = pd.read_csv('./data/train.csv')
    df = df.set_index("PassengerId")
    st.write("And here's the data for view:")
    #st.write(pd.read_csv(StringIO(view_csv)))
    #if :
        #st.dataframe(df.style.highlight_max(axis=0))
    st.write(df)
    st.sidebar.markdown("# Data 🎈")

