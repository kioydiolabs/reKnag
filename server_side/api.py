import random
import string
import os
from flask import Flask, request, jsonify, Response
import requests
import json
import validators

# options ########
https = False
domain = "reknag.com" # this can also be an IP #
localhost = False # setting this to true will ignore the domain #
# end of options #

app = Flask(__name__)

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


@app.route("/create/")
def create():

    original_url = request.args.get("url")

    if original_url.startswith("https://") or original_url.startswith("http://"):
        if validators.url(original_url):
            random_string = generate_random_string(6)

            os.makedirs(f"/var/www/html/{random_string}")

            html_code = "<!DOCTYPE html>"
            html_code += "<html lang=\"en\">"
            html_code += "<script src=\"index.js\"></script>"
            html_code += "</html>"

            js_code = f"window.location.replace(\"{original_url}\")"

            with open(f'/var/www/html/{random_string}/index.html', 'w', encoding='utf-8') as file:
                file.write(html_code)
            with open(f'/var/www/html/{random_string}/index.js', 'w', encoding='utf-8') as file:
                file.write(js_code)

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
    else:
        original_url = f"https://{original_url}"

        if validators.url(original_url):
            random_string = generate_random_string(6)

            os.makedirs(f"/var/www/html/{random_string}")

            html_code = "<!DOCTYPE html>"
            html_code += "<html lang=\"en\">"
            html_code += "<script src=\"index.js\"></script>"
            html_code += "</html>"

            js_code = f"window.location.replace(\"{original_url}\")"

            with open(f'/var/www/html/{random_string}/index.html', 'w', encoding='utf-8') as file:
                file.write(html_code)
            with open(f'/var/www/html/{random_string}/index.js', 'w', encoding='utf-8') as file:
                file.write(js_code)

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

    with open(f"/var/www/html/{id}/index.js", "r") as file:
        jscont = file.read()

    #jscont = str(open(f"/var/www/html/{id}/index.js"))

    char = len(jscont)-2
    url = jscont[25:char]

    # print(f"\n\n\nYour shortened URL is : http://127.0.0.1:3000/{random_string}")
    # uncomment the line above for debugging purposes

    return Response(url, mimetype='text/txt')


@app.route("/get_vt_total_link/")
def getvttotallink():
    urltoget = request.args.get("url")

    url = "https://www.virustotal.com/api/v3/urls"

    payload = { "url": f"{urltoget}" }
    headers = {
        "accept": "application/json",
        "x-apikey": "your_virustotal_api_key",
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

# Version 0124.b-prod
# For more info visit ksdocs.kioydiolabs.org