from water_rocket import WaterRocket
import streamlit as st
from page_introduction import page_introduction
from page_propulsion import page_propulsion
from page_summary import page_summary


def main():
    st.set_page_config(
        page_title="Open Water Rocket",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            "Get help": "https://github.com/lucas-schroeder/OpenWaterRocket/wiki",
            "Report a bug": "https://github.com/lucas-schroeder/OpenWaterRocket/issues",
            "About": """
                ## Who are we?
                 
                I'm a mechanical engineering, and this is a personal project.

                ---
                ## Want to see the code (and help)?

                The code for this app is in [this repository](https://github.com/lucas-schroeder/OpenWaterRocket)

                ---
                
                """
        }
    )

    if "wr" not in st.session_state:
        st.session_state.wr = WaterRocket()

    page = st.sidebar.radio(
        label="Select step",
        options=(
            "Introduction",
            "Propulsion",
            "Summary"
        ),
        index=0,
    )

    if page == "Introduction":
        st.session_state.wr = page_introduction(st.session_state.wr)

    if page == "Propulsion":
        st.session_state.wr = page_propulsion(st.session_state.wr)

    if page == "Summary":
        page_summary(st.session_state.wr)


if __name__ == "__main__":
    main()
