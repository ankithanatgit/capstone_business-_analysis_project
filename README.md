
# 📊 Business Analysis Capstone Project

**Customer Churn Prediction & Sales Trend Analysis**

This project demonstrates a complete **end-to-end Data Science workflow** from data preprocessing to machine learning deployment with actionable business recommendations.


## 🏢 Business Problem

Customer churn and unpredictable sales trends are major challenges for growing businesses.
This project analyzes customer behavior, predicts churn risk, and identifies monthly sales patterns to help companies take data-driven decisions.


## 🎯 Project Objectives

* Predict customer churn using machine learning
* Analyze monthly sales trends
* Generate business insights & recommendations
* Deploy the churn model using Flask API
* Prepare GitHub-ready documentation & presentation

## 🗂 Project Structure

```
business_analysis_capstone/
│
├── capstone_project.ipynb
├── README.md
├── PROJECT_DOCUMENTATION.md
│
├── data/
│   ├── customer_churn (2).csv
│   ├── sales_data (1).csv
│   └── house_prices (1).csv
│
├── reports/
│   ├── churn_distribution.png
│   ├── monthly_sales_trend.png
│   └── business_recommendations.md
│
├── deployment/
│   ├── app.py
│   ├── churn_model.pkl
│   ├── house_price_model.pkl
│   └── requirements.txt
│
└── presentation/
    └── capstone_presentation.pptx
```

## 🛠 Tools & Technologies

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib
* Flask
* Jupyter Notebook

---

## 🚀 How to Run

### 1. Install Libraries

```
pip install pandas numpy scikit-learn matplotlib flask requests
```

### 2. Run Notebook

```
jupyter notebook
```

Open `capstone_project.ipynb` and run all cells.

---

### 3. Run Flask Deployment

```
cd deployment
python app.py
```

Flask server runs at:

```
http://127.0.0.1:5000
```

---

### 4. Test Prediction API (Python)

Open new Command Prompt:

```
python
```

```python
import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "Tenure": 10,
    "MonthlyCharges": 70,
    "TotalCharges": 700,
    "SeniorCitizen": 0,
    "Contract_One year": 1,
    "Contract_Two year": 0,
    "PaymentMethod_Credit Card": 1,
    "PaymentMethod_Electronic Check": 0,
    "PaperlessBilling_Yes": 1
}

r = requests.post(url, json=data)
print(r.json())
```

---

## 📈 Results

* Churn prediction accuracy ~80%
* Sales peaked in **March**
* Month-to-Month customers show highest churn

---

## 📌 Business Recommendations

* Convert month-to-month users into yearly plans
* Target high-risk churn customers with offers
* Increase marketing during high-sale months

---

## 🏁 Conclusion

This project successfully demonstrates a real-world business data science solution including:

✔ Data analysis
✔ Machine learning model
✔ Deployment using Flask
✔ Live prediction testing
✔ Business strategy development
