import random
import string
from flask import Flask, request, jsonify, Response, render_template
import requests
import json
import validators
import mysql.connector

# options ########
vTotalAPI = "your_api_key" # replace this with your VirusTotal API key
# end of options #

app = Flask(__name__, template_folder="./static/templates/")


database = mysql.connector.connect(
  host="192.168.1.69",
  user="reknag",
  password="reknagDevPassword",
  database="reknag"
)


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


@app.route("/")
def redirectOnHomepage():
    return (render_template("redirect.html",target_url="https://create.reknag.com"),200)


@app.route("/<path:id>")
def gotoLink(id):

    try:
        mycursor = database.cursor()
        mycursor.execute(f"SELECT * FROM URLs WHERE ShortURL LIKE '{id}'")
        url = mycursor.fetchall()
        longURL = str(url[0][2])
    except Exception as e:
        return (f"Error! Refer to documentation. Error details : {e}", 200)

    return (render_template("redirect.html", target_url=longURL))


@app.route("/create/")
def create():

    original_url = request.args.get("url")

    if original_url.startswith("https://") or original_url.startswith("http://"):
        if validators.url(original_url):
            random_string = generate_random_string(6)


            mycursor = database.cursor()
            sql = "INSERT INTO reknag.URLs (ShortURL, TargetURL) VALUES (%s, %s)"
            val = (random_string, original_url)
            mycursor.execute(sql, val)
            database.commit()

            url_final = f"http://reknag.com/{random_string}"

            resp = Response(url_final)
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
        else:
            resp = Response("Invalid URL format")
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
    else:
        original_url = f"https://{original_url}"

        if validators.url(original_url):
            random_string = generate_random_string(6)

            mycursor = database.cursor()
            sql = "INSERT INTO reknag.URLs (ShortURL, TargetURL) VALUES (%s, %s)"
            val = (random_string, original_url)
            mycursor.execute(sql, val)
            database.commit()

            # print(f"\n\n\nYour shortened URL is : http://127.0.0.1:3000/{random_string}")
            # uncomment the line above for debugging purposes

            url_final = f"http://reknag.com/{random_string}"
            resp = Response(url_final)
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
        else:
            resp = Response("Invalid URL format")
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp


@app.route("/lookup/")
def lookup():
    id = request.args.get("id")

    mycursor = database.cursor()
    mycursor.execute(f"SELECT * FROM URLs WHERE ShortURL LIKE '{id}'")
    url = mycursor.fetchall()
    longURL = str(url[0][2])

    # print(f"\n\n\nYour shortened URL is : http://127.0.0.1:3000/{random_string}")
    # uncomment the line above for debugging purposes

    resp = Response(str(longURL))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route("/get_vt_total_link/")
def getvttotallink():
    urltoget = request.args.get("url")

    url = "https://www.virustotal.com/api/v3/urls"

    payload = { "url": f"{urltoget}" }
    headers = {
        "accept": "application/json",
        "x-apikey": f"{vTotalAPI}",
        "content-type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=payload, headers=headers)
    parsed = json.loads(response.text)
    filtered_data = parsed['data']['links']['self']
    parts = filtered_data.split("-")
    id = parts[-2]
    vturl=f"https://www.virustotal.com/gui/url/{id}"

    resp = Response(vturl)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

# kioydiolabs.org 2024