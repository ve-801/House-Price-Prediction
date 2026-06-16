from flask import Flask
import joblib

app = Flask(__name__)

model = joblib.load("src/gbr.pkl")

@app.route("/")
def home():
    return "House Price Prediction App is Running"

if __name__ == "__main__":
    app.run()
