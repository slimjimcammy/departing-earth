from flask import Flask, jsonify, request
import json
import requests
from story import guessConstellation, makeStory
from transformations import transformerstar
from PIL import Image

app = Flask(__name__)

@app.route("/planetdata", methods=["GET"])
def getPlanetData():
    url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,sy_dist,dec,ra,disc_year,pl_orbper,sy_vmag,sy_kmag,st_logg+from+ps&format=json"
    error = {"error": "API request failed"}
    try:
        response = requests.get(url)
        code = response.status_code

        return response.json() if code == 200 else None
    except requests.exceptions.RequestException as e:
        return None
    
@app.route("/stardata", methods=["GET"])
def getStarData():
    url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+hostname,ra,dec,sy_dist,sy_vmag,sy_kmag+from+stellarhosts&format=json"
    error = {"error": "API request failed"}
    try:
        response = requests.get(url)
        code = response.status_code

        return response.json() if code == 200 else None
    except requests.exceptions.RequestException as e:
        return None

@app.route("/guess", methods=["POST"])
def getConstellationGuess():
    payload = request.get_json()
    guess = guessConstellation(payload)
    return makeStory(guess)

@app.route("/transform", methods=["POST"])
def changeParams():
    params = request.get_json()
    coords = []
    for param in params:
        ra_e = param.get('ra_e')
        dec_e = param.get('dec_e')
        dist_e = param.get('dist_e')
        ra_s = param.get('ra_s')
        dec_s = param.get('dec_s')
        dist_s = param.get('dist_s')
        currCoordinates = transformerstar(ra_e, dec_e, dist_e, 
                                          ra_s, dec_s, dist_s)
        coords.append(currCoordinates)
    
    return json.dumps(coords)
    

