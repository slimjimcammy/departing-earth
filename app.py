from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import json
import requests
from story import guessConstellation, makeStory
from transformations import transformerstar
from PIL import Image

app = Flask(__name__)
cors = CORS(app)

@app.route("/planetparams", methods=["GET"])
@cross_origin()
def getPlanetParams():
    url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,sy_dist,dec,ra+from+ps&format=json"
    error = {"error": "API request failed"}
    try:
        response = requests.get(url)
        code = response.status_code

        return response.json() if code == 200 else None
    except requests.exceptions.RequestException as e:
        return None

@app.route("/planetfacts", methods=["GET"])
@cross_origin()
def getPlanetFacts():
    url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,disc_year,pl_orbper,st_logg+from+ps&format=json"
    error = {"error": "API request failed"}
    try:
        response = requests.get(url)
        code = response.status_code

        return response.json() if code == 200 else None
    except requests.exceptions.RequestException as e:
        return None
    
@app.route("/stardata", methods=["GET"])
@cross_origin()
def getStarData():
    url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+hostname,ra,dec,sy_dist+from+stellarhosts&format=json"
    error = {"error": "API request failed"}
    try:
        response = requests.get(url)
        code = response.status_code

        return response.json() if code == 200 else None
    except requests.exceptions.RequestException as e:
        return None

@app.route("/guess", methods=["POST"])
@cross_origin()
def getConstellationGuess():
    image_file = request.files['doodle'] 
    guess = guessConstellation(image_file)
    return makeStory(guess)

@app.route("/transform", methods=["POST"])
@cross_origin()
def changeParams():
    params = request.get_json()
    coords = []
    # {
    #     planet: {
    #         ra_e: 
    #     }
    #     stars: [
    #         {
    #             ra_s
    #         },

    #     ]
    # }
    ra_e = planet.get('ra_e')
    dec_e = planet.get('dec_e')
    dist_e = planet.get('dist_e')
    for star in params.stars:
        ra_s = star.get('ra_s')
        dec_s = star.get('dec_s')
        dist_s = star.get('dist_s')
        currCoordinates = transformerstar(ra_e, dec_e, dist_e, 
                                          ra_s, dec_s, dist_s)
        coords.append(currCoordinates)
    
    return json.dumps(coords)
    

