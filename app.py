from flask import Flask, render_template, request
import json
from web3 import Web3, HTTPProvider

w3 = Web3(HTTPProvider("http://localhost:7545"))
app = Flask(__name__)


@app.route("/")
def index():
    print(w3.isConnected())
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)