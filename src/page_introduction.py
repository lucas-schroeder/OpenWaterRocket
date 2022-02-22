from io import StringIO
import json
import streamlit as st
from water_rocket import WaterRocket


def page_introduction(wr: WaterRocket) -> WaterRocket:
    st.title("Open Water Rocket")

    st.write("""
        ## Objectives
        
        The goal of this app to provide a simple platform for analysing
        water rocket design.
    
        """
             )

    st.warning("This is only a VERY initial prototype!")

    st.write("""
        ---
        ## Load data
        
        You can load a .json file with your project data,
        or you may configure it in the tabs in the sidebar.

        """
             )

    data = st.file_uploader(
        label="Upload json file",
        type="json",
        accept_multiple_files=False,
    )

    if data:
        st.write("""
            ---
            ## Loaded Data

            Data loaded successfully.
            """
                 )
        data_str = StringIO(data.getvalue().decode("utf-8")).read()
        data_json = json.loads(data_str)
        st.json(data_json)
        wr = WaterRocket(**data_json)

    return wr
