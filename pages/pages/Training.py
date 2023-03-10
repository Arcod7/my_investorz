import csv
import pandas as pd
import streamlit as st


def Data():
    st.title("MY_INVESTORZ")
    st.markdown("# Thierry's training 🤖")
    df = pd.read_csv('./data/out.csv')
    st.write("That's how Tireey is training:")
    butb, butc = st.columns(2)
    graph = []
    with butb:
        if st.button("Capital"):
            graph.append("Capital")
        elif "Capital" in graph:
            graph.remoove("Capital")
    with butc:
        if st.button("ETH-USD"):
            graph.append("ETH-USD")
        elif "ETH-USD" in graph:
            graph.remoove("ETH-USD")
    if len(graph) == 0:
        graph = ['Capital', 'ETH-USD']
    st.line_chart(df[graph])
    chart_data = pd.DataFrame(
        df["Actions"],
        columns = ["Actions"])
    st.bar_chart(chart_data)
    st.write(df)
    st.sidebar.markdown("# Thierry's training 🤖")

if __name__ == '__main__':
    Data()
