import csv
import pandas as pd
import streamlit as st
import numpy as np


st.markdown("# Price ❄️")
tab1, tab2 = st.tabs(["Graph", "Spredsheet"])
with tab1:
    st.header("Graph")
    buta, butb, butc = st.columns(3)
    graph = []
    with buta:
        if st.checkbox("a"):
            graph.append("a")
        elif "a" in graph:
            graph.remoove("a")
    with butb:
        if st.checkbox("b"):
            graph.append("b")
        elif "b" in graph:
            graph.remoove("b")
    with butc:
        if st.checkbox("c"):
            graph.append("c")
        elif "c" in graph:
            graph.remoove("c")
    if len(graph) == 0:
        graph = ['a', 'b', 'c']
    chart_data = pd.DataFrame(
        np.random.randn(20, len(graph)),
        columns=graph)
    st.line_chart(chart_data)

with tab2:
    df = pd.read_csv('./data/train.csv')
    df = df.set_index("PassengerId")
    st.write("And here's the data for view:")
    sentence = st.text_input('Type if you want to research any information in the database:')
# if sentence == df[0]:
    # st.write(my_model.predict(sentence))
# else:
    st.write(df)
# with col1:
    # st.checkbox("a", key="disabled")
    # st.checkbox("b", key="horizontal")
    # st.checkbox("c", key="horizontal")
st.sidebar.markdown("# Price ❄️")
