
import streamlit as st 
from streamlit_option_menu import option_menu

def create_sidebar (): 
    with st.sidebar:

        selected = option_menu(
            menu_title="PVT Toolkit",
            options=[
                "Home",
                "Critical Properties",
                "Z-Factor",
                
                "Unit converter",
                
            ],
            icons=[
                "house",
                "thermometer-half",
                "graph-up",
                
                "calculator",
                
            ],
            menu_icon="droplet-half",
            default_index=0
        )
    return selected

