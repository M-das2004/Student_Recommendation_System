# 🎓 Student Recommendation Website

This project is a *Student Recommendation Website* that helps students discover suitable colleges based on their aptitude scores. It combines a user-friendly frontend with a machine learning–powered backend that analyzes data to provide personalized college recommendations.


## 📁 Project Structure

project-root/
│
├── frontend/
│ ├── apti.html # Aptitude test input page
│ ├── main.html # Main navigation page
│ ├── index.html # Homepage
│ ├── near.html # Page showing nearby colleges
│ ├── Timeline.html # Timeline for application process
│ └── college.html # Display of recommended colleges
│
├── backend/
│ ├── app.py # Flask app to serve the model and APIs
│ ├── train_model.py # Python script to train the ML model
│ ├── stream_predictor.pkl # Pickled ML model file
│ └── aptitude_scores.csv # Dataset used for training the model
│
└── README.md # Project documentation file
