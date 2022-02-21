# OpenWaterRocket
[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0-lightgrey??style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/2.0.x/)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

Python application for Water Rocket design

## Objectves

The idea of this project is to create a tool for analysing water rockets designs.

Build with Python and flask, to make it easy for colaboration

## Developing

Create a virtual environment with all requirements.

```cmd
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
```

Run the app

```cmd
cd src/
python -m flask run
```


### Testing

```cmd
cd tests
pytest -v
```