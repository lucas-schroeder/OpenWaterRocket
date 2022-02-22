import streamlit as st
from water_rocket import WaterRocket
from copy import deepcopy


def page_propulsion(wr: WaterRocket) -> WaterRocket:
    wr = deepcopy(wr)

    wr.initial_pressure = st.number_input(
        label="Initial pressure (bar)",
        min_value=0.0,
        max_value=None,
        value=wr.initial_pressure,
        step=0.1,
    )

    wr.water_ratio = st.slider(
        label="Water ration (% of volume)",
        min_value=0,
        max_value=100,
        value=wr.water_ratio,
        step=1,
    )

    return wr
