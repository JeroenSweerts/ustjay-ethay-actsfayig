import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


@app.route('/')
def home():

    post_url = 'https://hidden-journey-62459.herokuapp.com/piglatinize/'
    fact = get_fact()
    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {'input_text': fact }
    post_request = requests.post(post_url, headers=headers, data=payload)    
    return Response(post_request.url)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)
