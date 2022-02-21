import streamlit as st

menu = st.sidebar.radio(
    "Select step",
    (
        "Introduction",
        "Geometry",
        "Fuel",
    )
)
