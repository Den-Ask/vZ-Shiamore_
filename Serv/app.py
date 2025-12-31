from flask import *
app = Flask(__name__)

@app.route("/")
def home():
    return render_template ("tdm.html")

@app.route("/tdc_0.3.2")
def tdc():
    return render_template ("tdc_0.3.2.html")

@app.route("/conj_auto_0.2.3")
def conj_auto_02():
    return render_template ("conj_auto_0.2.3.html")

app.run(host="0.0.0.0", port=5000)