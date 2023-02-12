import csv
import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime
import altair as alt


def Prices():
    df = pd.read_csv("./data/ETH_1min.csv")
    st.markdown("# Thierry's performances 📈")
    tab1, tab2 = st.tabs(["Indicators", "Spredsheet"])
    # df = df.drop(columns="BCU/")
    #df = df.set_index("Unix Timestamp")
    with tab2:
        st.write("And here's the data for view:")
        sentence = st.text_input('Type if you want to research any information in the database:')
    # if sentence == df[0]:
        # st.write(my_model.predict(sentence))
    # else:
        st.write(df)
    with tab1:
        st.header("Indicators")
        buta, butb, butc, butd = st.columns(4)
        graph = []
        sentence = st.text_input("Training time")
        option = st.selectbox(
            'Choose a unit:',
            ('Days', 'Weeks', 'Months', 'Years'))
        #df["Unix Timestamp"].dt.tz_localize('Europe/Berlin')
        st.write(df.dtypes)
        if len(sentence) == 0:
            sentence = '1'
        st.write(sentence + ' ' + option)
        unit = 24 * 60
        if option == "Weeks":
            unit *= 7
        elif option == "Months":
            unit *= 30
        elif option == "Year":
            unit *= 365
        unit *= int(sentence)
        with buta:
            if st.checkbox("Open"):
                graph.append("Open")
            elif "Open" in graph:
                graph.remoove("Open")
        with butb:
            if st.checkbox("High"):
                graph.append("High")
            elif "High" in graph:
                graph.remoove("High")
        with butc:
            if st.checkbox("Low"):
                graph.append("Low")
            elif "Low" in graph:
                graph.remoove("Low")
        with butd:
            if st.checkbox("Close"):
                graph.append("Close")
            elif "Close" in graph:
                graph.remoove("Close")
        if len(graph) == 0:
            graph = ['Open', 'High', 'Low', 'Close']
        df = df[graph][-unit:-1]

        lol = alt.Chart(df).mark_line(point=True).encode(
            #alt.Y('graph:Q', axis=alt.Axis(format='%')),
            x='date:T',
            #color=':N'
           # x='date',
            y='price',
            #y=alt.Y('price',scale=alt.Scale(domain=[df[graph].min(), df[graph].max()])),
            #color='symbol',
            #strokeDash='symbol'
        )
        st.altair_chart(lol)

    # with col1:
        # st.checkbox("a", key="disabled")
        # st.checkbox("b", key="horizontal")
        # st.checkbox("c", key="horizontal")
    st.sidebar.markdown("# Thierry's performances 📈")


if __name__ == '__main__':
    Prices()
