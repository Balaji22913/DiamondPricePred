💎 Diamond Price Prediction

An end-to-end Machine Learning project that predicts the **price of a diamond** based on its physical and categorical attributes.  
The project follows an **industry-style ML pipeline architecture** and uses **Streamlit** for interactive prediction.

---

## 🚀 Project Overview

The goal of this project is to build a robust ML system that:

- Ingests raw diamond data
- Performs data preprocessing and feature engineering
- Trains a regression model
- Saves trained artifacts (model & preprocessor)
- Provides predictions through a user-friendly **Streamlit web app**

The ML logic is completely **decoupled from the frontend**, making it easy to switch between Flask, Streamlit, or FastAPI.

---

## 🧠 Features Used

### Numerical Features
- `carat`
- `depth`
- `table`
- `x` (length in mm)
- `y` (width in mm)
- `z` (depth in mm)

### Categorical Features
- `cut`
- `color`
- `clarity`

---

## 🏗️ Project Structure

```

DiamondPricePred/
│
├── app.py                     # Streamlit application
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── training_pipeline.py
│   │   └── prediction_pipeline.py
│   │
│   ├── logger.py               # Logging configuration
│   └── exception.py            # Custom exception handling
│
├── artifacts/                  # Saved models & preprocessors
├── logs/                       # Log files
├── notebooks/                  # EDA & experimentation notebooks
├── config/                     # Configuration files (optional)
├── requirements.txt
├── setup.py
└── README.md

````

---

## ⚙️ ML Pipeline Flow

1. **Data Ingestion**
   - Reads raw CSV data
   - Saves raw, train, and test datasets

2. **Data Transformation**
   - Numerical scaling
   - Categorical encoding
   - Saves preprocessing pipeline

3. **Model Training**
   - Trains regression model
   - Evaluates performance
   - Saves trained model

4. **Prediction Pipeline**
   - Loads preprocessor & model
   - Validates input schema
   - Returns price prediction

---

## 🖥️ Streamlit Application

The Streamlit app allows users to:

- Enter diamond features interactively
- Get real-time price predictions
- Run locally without backend server setup

### ▶️ Run the App

```bash
streamlit run app.py
````

---

## 🧪 How to Train the Model

Run the training pipeline:

```bash
python src/pipeline/training_pipeline.py
```

This will generate:

* `artifacts/train.csv`
* `artifacts/test.csv`
* `artifacts/preprocessor.pkl`
* `artifacts/model.pkl`

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/DiamondPricePred.git
cd DiamondPricePred
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Logging & Custom Exceptions

---

## 🎯 Key Highlights

* Modular, production-style ML architecture
* Frontend independent ML pipeline
* Robust exception handling & logging
* Easy to extend to MLOps (Docker, CI/CD, FastAPI)

---


## 🙌 Author

**Ashutosh Pandey**

Feel free to ⭐ the repository if you find this project useful!
