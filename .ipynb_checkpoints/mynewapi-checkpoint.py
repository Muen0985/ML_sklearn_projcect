from flask import Flask,request,jsonify
import joblib
import pandas as pd

# create Flask app
app=Flask(__name__)

# connect post api call --> predict() function

# http://localhost:5000/predict
@app.route('/predict',)
def predict():
    
    return  # PREDICTION
# load model and column names
