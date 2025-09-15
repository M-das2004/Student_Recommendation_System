import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Sample dataset
data = {
    'Quant': [7, 3, 2, 1, 4, 5],
    'Verbal': [3, 8, 7, 2, 4, 5],
    'Science': [8, 2, 1, 1, 6, 4],
    'Commerce': [2, 4, 9, 9, 5, 3],
    'General': [4, 6, 5, 2, 5, 3],
    'Recommended Stream': ['Science', 'Arts', 'Arts', 'Commerce', 'General', 'Science']
}

df = pd.DataFrame(data)

X = df[['Quant', 'Verbal', 'Science', 'Commerce', 'General']]
y = df['Recommended Stream']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the model
joblib.dump(model, 'stream_predictor.pkl')
print("Model trained and saved as stream_predictor.pkl")
