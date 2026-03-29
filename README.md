# 🚆 IRCTC Berth Prediction System

## 📌 Overview

This project is a **Machine Learning-based web application** that predicts the likely berth allocation (LB, UB, SL, SU, etc.) for railway passengers based on booking details.

The model is trained on a **synthetic dataset (12,000+ records)** and deployed using **Streamlit** for real-time predictions.

---

## 🎯 Objectives

* Predict berth allocation using passenger and booking data
* Build an end-to-end ML pipeline (Data → Model → Deployment)
* Achieve **95%+ accuracy** using optimized models
* Create an interactive **GUI using Streamlit**

---

## 📊 Dataset Features

* `age`
* `gender`
* `booking_status` (CNF / RAC / WL)
* `quota` (GN / TQ / LD)
* `coach_type` (SL / 3AC / 2AC)
* `booking_time`
* `travel_distance`
* `waiting_list_number`
* `seat_preference`
* `seat_pref_missing` (engineered feature)

### 🎯 Target Variable

* `berth_type` (LB, MB, UB, SL, SU, Side LB, Side UB)

---

## ⚙️ Machine Learning Workflow

### 1. Data Preprocessing

* Handled missing values using `"Unknown"` category
* Added missing indicator feature (`seat_pref_missing`)
* Encoded categorical variables using `LabelEncoder`

### 2. Model Training

* Algorithm used: **XGBoost / Gradient Boosting**
* Train-test split: 80-20
* Feature engineering applied

### 3. Evaluation Metrics

* Accuracy Score
* Weighted F1 Score
* Classification Report

---

## 📈 Model Performance

* ✅ Accuracy: **70%+**
* Balanced predictions after handling class imbalance

---

## 🖥️ Streamlit Web App

### Features:

* User-friendly input form
* Real-time berth prediction
* Encoded input handling
* Predict button for controlled execution

---

## 🚀 How to Run Locally

```bash
git clone <your-repo-link>
cd irctc-berth-prediction
pip install -r requirements.txt
streamlit run app.py
```

---

## ☁️ Deployment (Streamlit Cloud)

1. Push project to GitHub
2. Go to https://share.streamlit.io
3. Connect your repository
4. Deploy `app.py`

---

## 📂 Project Structure

```bash
IRCTC-Berth-Prediction/
│── app.py
│── model.joblib
│── encoders.pkl
│── features.pkl
│── irctc_dataset.csv
│── requirements.txt
│── README.md
```

---

## 🧠 Key Learnings

* Handling missing values without losing information
* Feature engineering for performance improvement
* Avoiding feature mismatch in deployment
* Model interpretability using confusion matrix & feature importance

---

## ⚠️ Disclaimer

This model is trained on **synthetic data** and does not reflect actual IRCTC allocation logic.

---

## 👨‍💻 Author

**Abin Anand**

---

## ⭐ Future Improvements

* Add SHAP explainability
* Improve dataset realism
* Deploy with custom domain
* Add analytics dashboard in Streamlit

---
