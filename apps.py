from flask import Flask, request, jsonify
from model.model import Model
import json


app = Flask(__name__)
model = Model() 

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello Flask!"

@app.route('/predict', methods=['POST'])
def predict():
    request_json = request.json
    print(request_json)
    
    prediction= model.predict(request_json.get('image'))

    # return json.dumps(prediction)
    return jsonify(prediction)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)