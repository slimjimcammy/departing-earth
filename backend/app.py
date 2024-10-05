from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/test")
def test():
    return "<h1>Test successful!</h1>"

@app.route("/stardata", methods=["GET"])
def getStarData():
    url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,sy_dist,dec,rastr,disc_year,pl_orbper,sy_vmag,sy_kmag,st_logg+from+ps&format=json"
    print("in stardata")
    error = {"error": "API request failed"}
    try:
        response = requests.get(url)
        code = response.status_code

        return jsonify(response.json()), 200 if code == 200 else error, code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500



