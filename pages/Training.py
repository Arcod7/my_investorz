import csv
import pandas as pd
import streamlit as st


def Data():
    st.set_page_config(page_icon="https://www.epitech.eu/fr/wp-content/uploads/Epitech_Technology_equipe_Lyon_Matthieu_Champely_Directeur_pedagogique_regional-1-e1650382218365-150x150.jpg")
    st.title("MY_INVESTORZ")
    st.markdown("# Thierry's training 🤖")
    df = pd.read_csv('./data/out.csv')
    st.write("That's how Thierry is training:")
    butb, butc = st.columns(2)
    graph = []
    # with butb:
        # if st.button("Capital"):
            # graph.append("Capital")
        # elif "Capital" in graph:
            # graph.remoove("Capital")
    # with butc:
        # if st.button("ETH-USD"):
            # graph.append("ETH-USD")
        # elif "ETH-USD" in graph:
            # graph.remoove("ETH-USD")
    # if len(graph) == 0:
        # graph = ['Capital', 'ETH-USD']
    st.write("Capital")
    st.line_chart(df['Capital'])
    st.write("ETH-USD")
    st.line_chart(df['ETH-USD'])
    st.write("Actions")
    chart_data = pd.DataFrame(
        df["Actions"],
        columns = ["Actions"])
    st.bar_chart(chart_data)
    #st.write(df)
    st.sidebar.markdown("# Thierry's training 🤖")

if __name__ == '__main__':
    Data()
