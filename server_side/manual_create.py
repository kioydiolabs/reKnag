import random
import string
import os

original_url = input(f"What is the url you want to shorten? (include https/http) \n>  ")

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

random_string = generate_random_string(6)

os.makedirs(random_string)

html_code = "<!DOCTYPE html>"
html_code += "<html lang=\"en\">"
html_code += "<script src=\"index.js\"></script>"
html_code += "</html>"

js_code = f"window.location.replace(\"{original_url}\")"

with open(f'./{random_string}/index.html', 'w', encoding='utf-8') as file:
    file.write(html_code)
with open(f'./{random_string}/index.js', 'w', encoding='utf-8') as file:
    file.write(js_code)

print(f"\n\n\nYour shortened URL is : http://127.0.0.1:3000/{random_string}")