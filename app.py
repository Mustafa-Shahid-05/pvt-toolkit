import streamlit as st
from components.sidebar import create_sidebar
from screens import (home , z_factor, 
                    critical , converter , 
                   )
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.set_page_config(
    page_title="PVT Toolkit",
    page_icon="🛢️",
    layout="wide"
)

selected = create_sidebar()

match selected: 
    case "Home": 
        home.show()
    case "Z-Factor": 
        z_factor.show()
    case "Critical Properties" : 
        critical.show()
  
    case "Unit converter":
        converter.show()
    