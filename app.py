from flask import Flask, jsonify, request
import requests
from story import guessConstellation, makeStory
from PIL import Image

app = Flask(__name__)

@app.route("/test")
def test():
    return "<h1>Test successful!</h1>"

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
    # expects the image
    imageFile = request.form['filename']
    publicURL = uploadToFirebase(bucket, imageFile)
    return guessConstellation(imageURL)

@app.route("/story", methods=["POST"])
def getStory():
    print("in story")
    guess = request.args.get('guess')
    print(guess)
    return makeStory(guess)
