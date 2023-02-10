import streamlit as st
#import tableauserverclient as TSC
import pandas as pd
import csv

def main_page():
    st.markdown("# Main page 🎈")
    # st.title("""
    # MY_INVESTOR
    # """)
    # df = pd.read_csv('./data/train.csv')
    # df = df.set_index("PassengerId")
    # st.write("And here's the data for view:")
    # #st.write(pd.read_csv(StringIO(view_csv)))
    # st.write(df)
    st.sidebar.markdown("# Main page 🎈")

def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}
