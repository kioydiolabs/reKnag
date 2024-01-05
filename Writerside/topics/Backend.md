# Backend

The backend uses Python and the Flask module.

The script begins by initiating an API endpoint on /create. This will accept GET requests.
<code-block lang="python">@app.route("/create/")
def create():</code-block>

It then retrieves the parameter "URL"
<code-block lang="python">original_url = request.args.get("url")</code-block>

It will then create a randomly generated string of letters and digits of a specified length.
<code-block lang="python">def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
random_string = generate_random_string(6)</code-block>

It then creates a directory in the root directory of the web server with the randomly generated string as it's name.
<code-block lang="python">os.makedirs("/var/www/html/random_string")</code-block>

It also creates 2 variables, one called `js_code` and one called `html_code`.
The variables contain HTML code for the `index.html` page that will be created in the randomly generated directory, as well as a single line of JavaScript code which is the line that is responsible for actually redirecting the user to the target URL.
<code-block lang="python"><![CDATA[html_code = "<!DOCTYPE html>"
html_code += "<html lang=\"en\">"
html_code += "<script src=\"index.js\"></script>"
html_code += "</html>"
js_code = f"window.location.replace(\"{original_url}\")"]]></code-block>

It will then save the variables as an index.js and index.html file in the randomly generated directory under the the root directory of the web server.
<code-block lang="python">with open(f'/var/www/html/index.html', 'w', encoding='utf-8') as file:
    file.write(html_code)
with open(f'/var/www/html/index.js', 'w', encoding='utf-8') as file:
    file.write(js_code)
</code-block>

Finally, the API will return the short URL
<code-block lang="python">url_final = f"http://127.0.0.1/{random_string}"
return Response(url_final, mimetype='text/txt')</code-block>