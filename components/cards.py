import streamlit as st
from contextlib import contextmanager


@contextmanager
def card(title: str, icon: str = ""):

    with st.container(border=True):
        if icon:
            st.subheader(f"{icon} {title}")
        else:
            st.subheader(title)

        st.divider()
        yield