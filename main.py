from flask import Flask, request
from urllib.parse import urlparse
import foodnetwork

app = Flask(__name__)

def process_url(url:str):
    domain = urlparse(url).hostname

    if "foodnetwork.com" in domain:
        result = foodnetwork.scrape_foodNetwork(url)
        if result != "error getting recipe" or result != "failed to fetch recipe":
            return result.toDict()
        return result
    return {"error": "passed in url is not supported"}

@app.route('/fetch', methods=['POST'])
def fetch():
    request_data = request.get_json()
    url = request_data['url']

    if url == None:
        return {"error": "no url was passed in"}

    result = process_url(url)
    return result


if __name__ == '__main__':
    app.run(debug=True, port=25565)