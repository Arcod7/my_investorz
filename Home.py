import streamlit as st

import csv
import pandas as pd
import streamlit as st
from PIL import Image
#from Data import *
#from Prices import *

def main():
    st.title("MY INVESTORZ")
    with st.container():
        st.image( 
            "https://i.kym-cdn.com/photos/images/newsfeed/001/499/826/2f0.png",
            caption="https://i.kym-cdn.com/photos/images/newsfeed/001/499/826/2f0.png")
        st.header("*Description:*")
        st.write("Thierry is a trading AI on the Etherium, made for the IA rush.")
    col1, col2, col3, col4, col5 = st.columns(5)
    with st.container():
        st.write("In the project:")
        with col1:
            st.write("Thomas Pommier")
        with col2:
            st.write("Alexandre Douard")
        with col3:
            st.write("Antoine Esman")
        with col4:
            st.write("Samuel Bruschet")
        with col5:
            st.write("Matthias von Rakowski")

if __name__ == '__main__':
    main()
