import csv
import pandas as pd
import streamlit as st

st.title("MY_INVESTORZ")
st.markdown("# Data 🎈")
df = pd.read_csv('./data/since_2022.csv')
df = df.set_index("time")
st.write("And here's the data for view:")
sentence = st.text_input('Type if you want to research any information in the database:')
# if sentence == df[0]:
    # st.write(my_model.predict(sentence))
# else:
st.write(df)
st.sidebar.markdown("# Data 🎈")

