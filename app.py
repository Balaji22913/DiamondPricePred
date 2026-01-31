import streamlit as st
import pandas as pd
from src.pipeline.prediction_pipeline import PredictPipeline

st.set_page_config(page_title="Diamond Price Prediction", page_icon="💎")

st.title("💎 Diamond Price Prediction")

# ---- Numerical inputs
carat = st.number_input("Carat", min_value=0.1, max_value=5.0, step=0.01)
depth = st.number_input("Depth", min_value=50.0, max_value=70.0)
table = st.number_input("Table", min_value=50.0, max_value=70.0)
x = st.number_input("X (length in mm)", min_value=0.0, max_value=10.0)
y = st.number_input("Y (width in mm)", min_value=0.0, max_value=10.0)
z = st.number_input("Z (depth in mm)", min_value=0.0, max_value=10.0)

# ---- Categorical inputs
cut = st.selectbox("Cut", ["Fair", "Good", "Very Good", "Premium", "Ideal"])
color = st.selectbox("Color", ["D", "E", "F", "G", "H", "I", "J"])
clarity = st.selectbox(
    "Clarity",
    ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
)

if st.button("Predict Price"):
    input_df = pd.DataFrame({
        "carat": [carat],
        "depth": [depth],
        "table": [table],
        "x": [x],
        "y": [y],
        "z": [z],
        "cut": [cut],
        "color": [color],
        "clarity": [clarity]
    })

    pipeline = PredictPipeline()
    result = pipeline.predict(input_df)

    st.success(f"💰 Estimated Diamond Price: ₹ {int(result[0])}")
