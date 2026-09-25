import streamlit as st
from utils.validation import safe_float

def value_input(
    label,
    value="",
    min_value = None,
    max_value = None,
    key=None,
    help=None,
    units=None,
    suffix = None,
    required = True
):

    col1, col2, col3 = st.columns([1.5, 2, 1.2])

    with col1:
        st.markdown(label)

    with col2:
        text = st.text_input(
            label="",
            value=str(value),
            key=key,
            help=help,
            label_visibility="collapsed",
        )
        number = None
        text = text.strip ()

        if text == "": 
            if required : 
                st.error ("This field should not be empty.")
            else : 
                number = 0

        else :
            number = safe_float (text)
            if number == None : 
                st.error ("Only numbers are allowed.")
            else : 
                if min_value is not None and number<min_value : 
                    st.error (f"{label} must be greater than or equal to {min_value}.")
                    number = None
                elif max_value is not None and number > max_value : 
                    st.error (f"{label} must be less than or equal to {max_value}.")
                    number = None

    with col3:
        unit = None
        if units:
            unit = st.selectbox(
                label="",
                label_visibility="collapsed",
                options=units,
                key=f"{key}_unit",
            )
        elif suffix : 
            st.markdown(
            f"<div style='padding-top:8px'>{suffix}</div>",
            unsafe_allow_html=True
        )
        
        

    return number, unit