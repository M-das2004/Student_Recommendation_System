from flask import Flask, request, jsonify
import joblib
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend (running on file:// or localhost) to access this backend

# Load trained ML model
model_path = os.path.join(os.path.dirname(__file__), "stream_predictor.pkl")
model = joblib.load(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = [
        data.get("quant", 0),
        data.get("verbal", 0),
        data.get("science", 0),
        data.get("commerce", 0),
        data.get("general", 0)
    ]
    prediction = model.predict([features])[0]

    college_map = {
        "Science": "IITs, AIIMS, IISERs",
        "Commerce": "SRCC, Narsee Monjee, LSR",
        "Arts": "JNU, DU, Presidency College",
        "General": "DU, BHU, Civil Services Prep Colleges"
    }

    return jsonify({
        "recommended_stream": prediction,
        "college_suggestions": college_map.get(prediction, "Explore options")
    })

if __name__ == '__main__':
    app.run(debug=True)
