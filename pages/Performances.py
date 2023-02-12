import csv
import pandas as pd
import streamlit as st
import numpy as np
import datetime as ntm
from datetime import datetime
import altair as alt


def Prices():
    st.set_page_config(page_title = "Thierry",page_icon="https://www.epitech.eu/fr/wp-content/uploads/Epitech_Technology_equipe_Lyon_Matthieu_Champely_Directeur_pedagogique_regional-1-e1650382218365-150x150.jpg")
    df = pd.read_csv("./data/ETH_1H_data.csv")
    dg = pd.read_csv("./data/perf.csv")
    st.markdown("# Thierry's performances 📈")
    tab1, tab2, tab3 = st.tabs(["Indicators", "Spreadsheet", "Performances"])
    # df = df.drop(columns="BCU/")
    #df = df.set_index("Unix Timestamp")
    with tab2:
        st.header("Spreadsheet")
        year = st.sidebar.selectbox("Choose a year to start", range(2016, 2024))
        selected = st.sidebar.multiselect("select data", sorted(df.columns), sorted(df.columns))
        st.write("And here's the data for view:")
    # if sentence == df[0]:
        # st.write(my_model.predict(sentence))
    # else:
        st.write(df[selected])
    with tab1:
        st.header("Indicators")
        buta, butb, butc, butd = st.columns(4)
        graph = []
        date = st.date_input("Choose from when you want the Data", ntm.date(2016, 5, 1))
        option = st.selectbox(
            'Choose a unit:',
            ('Days', 'Hours', 'Weeks', 'Months', 'Years'))
        #df["Unix Timestamp"].dt.tz_localize('Europe/Berlin')
        unit = 24
        if option == "Hours":
            unit = 1
        if option == "Weeks":
            unit *= 7
        elif option == "Months":
            unit *= 30
        elif option == "Years":
            unit *= 365
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
        date_time = datetime.timestamp(datetime(date.year, date.month, date.day))
        copy_df = df.drop(df.index[(df.index % unit != 0)])
        copy_df = copy_df.set_index("Date")
        copy_df = copy_df.loc[copy_df["Unix Timestamp"] >= date_time]

        # df = df[graph][-unit:-1]

        #lol = alt.Chart(df).mark_line(point=True).encode(
            #alt.Y('graph:Q', axis=alt.Axis(format='%')),
         #   x='date:T',
            #color=':N'
           # x='date',
         #   y='price',
            #y=alt.Y('price',scale=alt.Scale(domain=[df[graph].min(), df[graph].max()])),
            #color='symbol',
            #strokeDash='symbol'
        #)
        #st.altair_chart(lol)
        st.line_chart(copy_df[graph])
    with tab3:
        st.header("Performances")
        st.subheader("\taccording to *Epochs*")
        st.line_chart(dg[["Train"]])
        st.line_chart(dg["Test"])
        st.line_chart(dg["Train_Score"])
    # with col1:
        # st.checkbox("a", key="disabled")
        # st.checkbox("b", key="horizontal")
        # st.checkbox("c", key="horizontal")
    st.sidebar.markdown("# Thierry's performances 📈")


if __name__ == '__main__':
    Prices()
