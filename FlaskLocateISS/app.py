import json
import urllib.request
import webbrowser

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/locate")
def locate():
    resp = urllib.request.urlopen('http://api.open-notify.org/iss-now.json')
    obj = json.loads(resp.read())
    lat = obj['iss_position']['latitude']
    long = obj['iss_position']['longitude']
    current_position_url = 'https://www.openstreetmap.org/?mlat=' + str(lat) + '&mlon=' + str(
        long) + '#map=3/' + str(
        lat) + '/' + str(long)
    webbrowser.open_new(current_position_url)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=5001)
