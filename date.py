import csv
import pandas as pd
import streamlist as st

def date():
    st.markdown("# Main page 🎈")
    st.title("""
    MY_INVESTOR
    """)
    df = pd.read_csv('./data/train.csv')
    df = df.set_index("PassengerId")
    st.write("And here's the data for view:")
    #st.write(pd.read_csv(StringIO(view_csv)))
    st.write(df)
    st.sidebar.markdown("# Main page 🎈")

