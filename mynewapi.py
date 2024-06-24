from flask import Flask,request,jsonify
import joblib
import pandas as pd

# create Flask app
app=Flask(__name__)

# connect post api call --> predict() function   http://localhost:5000/predict
@app.route('/predict',methods=['POST'])
def predict():
    
    # Get JSON Request
    feature_data=request.json

    # Convert into pd dataframe(match col names)
    df=pd.DataFrame(feature_data)
    df=df.reindex(columns=col_names)

    # Predict (will return as JSON)
    prediction=list(model.predict(df))

    return  jsonify({'prediction':str(prediction)})

# So the api is goona post sth to the http link, and pass in json and predict it 
# finally, return as json

# load model and column names
if __name__ == '__main__':
    model= joblib.load("rfr_final_model.pkl")
    col_names=joblib.load("col_names.pkl")

    app.run(debug=True)
