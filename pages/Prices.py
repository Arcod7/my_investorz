import csv
import pandas as pd
import streamlit as st
import numpy as np


def Prices():
    st.markdown("# Price ❄️")
    tab1, tab2 = st.tabs(["Graph", "Spredsheet"])
    df = pd.read_csv('./data/since_2022.csv')
    with tab2:
        df = df.set_index("time")
        st.write("And here's the data for view:")
        sentence = st.text_input('Type if you want to research any information in the database:')
    # if sentence == df[0]:
        # st.write(my_model.predict(sentence))
    # else:
        st.write(df)
    with tab1:
        st.header("Graph")
        buta, butb, butc, butd = st.columns(4)
        graph = []
        with buta:
            if st.checkbox("sma"):
                graph.append("sma")
            elif "sma" in graph:
                graph.remoove("sma")
        with butb:
            if st.checkbox("sd"):
                graph.append("sd")
            elif "sd" in graph:
                graph.remoove("sd")
        with butc:
            if st.checkbox("lb"):
                graph.append("lb")
            elif "lb" in graph:
                graph.remoove("lb")
        with butd:
            if st.checkbox("ub"):
                graph.append("ub")
            elif "ub" in graph:
                graph.remoove("ub")
        if len(graph) == 0:
            graph = ['sma', 'sd', 'lb', 'ub']
        df = df[graph]
        st.line_chart(df)

    # with col1:
        # st.checkbox("a", key="disabled")
        # st.checkbox("b", key="horizontal")
        # st.checkbox("c", key="horizontal")
    st.sidebar.markdown("# Price ❄️")


if __name__ == '__main__':
    Prices()
