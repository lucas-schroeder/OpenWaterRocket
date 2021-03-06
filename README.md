# OpenWaterRocket

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg?style=flat-square)](https://share.streamlit.io/lucas-schroeder/openwaterrocket/main/src/app.py)
[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python)](https://www.python.org/)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg?style=flat-square)](https://www.python.org/dev/peps/pep-0008/)

Python application for Water Rocket design. Click [here](https://share.streamlit.io/lucas-schroeder/openwaterrocket/main/src/app.py) to access the web app.


> :warning: **This is only a VERY initial prototype!**

## Objectives

The idea of this project is to create a tool for analyzing water rockets designs.

Build with Python and Streamlit, to make it easy for collaboration


## Developing

Create a virtual environment with all requirements.

```cmd
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
```

Run the app

```cmd
streamlit run src/app.py
```


### Testing

```cmd
cd tests
pytest -v
```