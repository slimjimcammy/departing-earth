from flask import Flask

app = Flask(__name__)

@app.route("/test")
def test():
    return "<h1>Test successful!</h1>"

# @app.route("/stardata", "POST")
# def getStarData: