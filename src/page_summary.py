import json
import streamlit as st
from water_rocket import WaterRocket
from copy import deepcopy


def page_summary(wr: WaterRocket) -> None:
    wr = deepcopy(wr)
    rocket_data = json.dumps(wr.__dict__, indent=4)

    st.download_button(
        label="Download data",
        data=rocket_data,
        file_name="water_rocket_model.json",
        mime="text/plain",
    )
    st.json(rocket_data)
