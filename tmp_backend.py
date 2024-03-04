# %%
import pickle
from flask import Flask, request, render_template, jsonify, make_response, send_file
import os
from flask_cors import CORS, cross_origin
import random
import requests

# %%
# For CORS Protocal
app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")
CORS(app)
# %%
'''
Interface...
'''
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")

@app.route('/api/random')
def random_number():
    print('>>>Hi!')
    response = {
        'randomNumber': random.randint(1, 100)
    }
    return jsonify(response)

@app.route('/api/intermediate-predict', methods=['POST', 'GET'])
def forward_predict():
    payload = request.get_json()
    external_url = 'http://140.114.80.46:5556/api/predict'
    response = requests.post(external_url, json=payload)
    return jsonify(response.json())
# @app.route('/api/intermediate-predict', methods=['POST', 'GET'])
# def forward_predict():
#     print('>>>>>Hello!')
#     return jsonify({"message": "Test response"})



# %%

if __name__ == "__main__":
        port = int(os.environ.get("PORT", 8080))
    #    app.run(host='0.0.0.0', port=port, debug=True, ssl_context=('cert.pem', 'key.pem'))
        app.run(host='0.0.0.0', port=port, debug=True)