from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("churn_model.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return jsonify({"Churn_Prediction": int(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
