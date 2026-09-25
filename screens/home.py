import streamlit as st


def show():

    st.title("PVT Toolkit")

    st.write(
        "A simple collection of petroleum engineering tools "
        "for PVT and reservoir calculations."
    )

    st.divider()

    st.markdown(
        """
        ### Welcome

        PVT Toolkit provides practical tools for working with
        petroleum engineering properties and unit conversions.

        Use the sidebar to access the available calculations.
        """
    )

    st.divider()

    st.markdown(
        """
        **Developed by Mustafa Shahid**  
        Petroleum Engineering Student
        """
    )