💎 Diamond Price Prediction

An end-to-end **Machine Learning regression project** that predicts the price of a diamond based on its physical and categorical characteristics.  
The project follows **industry-style ML architecture**, with a modular pipeline, logging, exception handling, and multiple UI options for inference.

---

## 🚀 Project Highlights

- End-to-end ML pipeline (ingestion → transformation → training → prediction)
- Modular and reusable codebase
- Custom logging and exception handling
- Multiple app interfaces:
  - **Streamlit** (`app.py`)
  - **Gradio** (`app_gradio.py`)
- Production-ready folder structure
- Easily extendable to FastAPI / Docker / CI-CD

---

## 📂 Project Structure

```

DiamondPricePred/
│
├── app.py                      # Streamlit application
├── app_gradio.py               # Gradio application
│
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
│   ├── utils.py
│   ├── logger.py
│   └── exception.py
│
├── artifacts/                  # Saved models, preprocessors, datasets
├── logs/                       # Log files
├── notebooks/                  # EDA & experimentation notebooks
├── config/                     # Configuration files (optional)
│
├── requirements.txt
├── setup.py
└── README.md

````

---

## 📊 Dataset Description

The dataset contains information about diamonds with the following features:

### Numerical Features
- `carat` – weight of the diamond
- `depth` – total depth percentage
- `table` – width of the top of the diamond
- `x` – length (mm)
- `y` – width (mm)
- `z` – depth (mm)

### Categorical Features
- `cut` – quality of the cut
- `color` – diamond color grading
- `clarity` – clarity measurement

### Target
- `price` – price of the diamond

---

## ⚙️ Machine Learning Pipeline

1. **Data Ingestion**
   - Reads raw dataset
   - Splits into train and test sets
   - Saves artifacts

2. **Data Transformation**
   - Numerical scaling
   - Categorical encoding
   - Preprocessor saved for reuse

3. **Model Training**
   - Regression model training
   - Model evaluation
   - Best model saved

4. **Prediction Pipeline**
   - Loads trained model & preprocessor
   - Ensures schema consistency
   - Generates predictions

---

## 🖥️ Running the Applications

### 🔹 1. Streamlit App

```bash
streamlit run app.py
````

* Interactive UI
* Ideal for demos and portfolios

---

### 🔹 2. Gradio App

```bash
python app_gradio.py
```

* Lightweight interface
* Easy sharing and rapid testing

---

## 📦 Installation & Setup

### 1️⃣ Create virtual environment

```bash
python -m venv venv
```

### 2️⃣ Activate environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🧪 Train the Model

Run the training pipeline:

```bash
python src/pipeline/training_pipeline.py
```

This will generate:

* Processed datasets
* Trained model
* Preprocessor artifacts

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-Learn
* Streamlit
* Gradio
* Logging & Custom Exceptions

---

## 🧠 Design Philosophy

* Frontend (UI) is **decoupled** from ML logic
* Same prediction pipeline works with:

  * Streamlit
  * Gradio
  * Flask / FastAPI (future)
* Clean separation of concerns enables easy scaling

---

## 📈 Future Improvements

* Dockerization
* CI/CD pipeline
* FastAPI backend
* Cloud deployment (AWS / Azure / GCP)
* Model monitoring & retraining

---

## 👤 Author

**Ashutosh Pandey**
Machine Learning & Data Science Enthusiast

---

## ⭐ If you like this project

Give it a ⭐ on GitHub — it motivates continuous improvement!
