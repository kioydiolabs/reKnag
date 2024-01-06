import random
import string
import os
from flask import Flask, request, jsonify, Response

app = Flask(__name__)

@app.route("/create/")
def create():

    original_url = request.args.get("url")

    def generate_random_string(length):
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string

    random_string = generate_random_string(6)

    os.makedirs("/var/www/html/random_string")

    html_code = "<!DOCTYPE html>"
    html_code += "<html lang=\"en\">"
    html_code += "<script src=\"index.js\"></script>"
    html_code += "</html>"

    js_code = f"window.location.replace(\"{original_url}\")"

    with open(f'/var/www/html/index.html', 'w', encoding='utf-8') as file:
        file.write(html_code)
    with open(f'/var/www/html/index.js', 'w', encoding='utf-8') as file:
        file.write(js_code)

    # print(f"\n\n\nYour shortened URL is : http://127.0.0.1:3000/{random_string}")
    # uncomment the line above for debugging purposes

    url_final = f"http://127.0.0.1/{random_string}"

    return Response(url_final, mimetype='text/txt')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

# Version 0124.b-prod
# For more info visit ksdocs.kioydiolabs.org