import time
import requests
import os
import json

from flask import Flask

app = Flask(__name__)

@app.route('/retail')
def retail():
    r = requests.get(os.getenv("RETAIL_API_URL") + "orders?filter[customFields][site_lead_id][min]=1&limit=20&apiKey=" + os.getenv("RETAIL_TOKEN"))
    return json.loads(r.text)

@app.route('/')
def run():
    r = requests.post(os.getenv("API_URL"), headers = {'Token': os.getenv("TOKEN")})
    return json.loads(r.text)
