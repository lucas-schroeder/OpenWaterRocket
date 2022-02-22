from water_rocket import WaterRocket
import streamlit as st
from page_introduction import page_introduction
from page_propulsion import page_propulsion
from page_summary import page_summary


def main():
    if "wr" not in st.session_state:
        st.session_state.wr = WaterRocket()

    page = st.sidebar.radio(
        label="Select step",
        options=(
            "Introduction",
            "Propulsion",
            "Summary"
        ),
        index=2,
    )

    if page == "Introduction":
        st.session_state.wr = page_introduction(st.session_state.wr)

    if page == "Propulsion":
        st.session_state.wr = page_propulsion(st.session_state.wr)

    if page == "Summary":
        page_summary(st.session_state.wr)


if __name__ == "__main__":
    main()
