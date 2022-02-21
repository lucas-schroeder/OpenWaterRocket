from flask import Flask

app = Flask("OpenWaterRocket")

@app.route("/")
def index():
    return "Wellcome"