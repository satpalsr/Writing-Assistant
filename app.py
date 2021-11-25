import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

from happytransformer import TTSettings
beam_settings = TTSettings(num_beams=5, min_length=1, max_length=20)

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = str(request.form['Input_text'])
    output = model.generate_text(int_features, args=beam_settings)

    return render_template('index.html', prediction_text='{}'.format(output.text))

if __name__ == "__main__":
    app.run(debug=True)