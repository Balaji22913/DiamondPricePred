import gradio as gr
import pandas as pd
from src.pipeline.prediction_pipeline import PredictPipeline


def predict_price(
    carat, depth, table, x, y, z, cut, color, clarity
):
    # Create input dataframe
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

    return f"💰 Estimated Diamond Price: ₹ {int(result[0])}"


with gr.Blocks(title="Diamond Price Prediction 💎") as demo:
    gr.Markdown("# 💎 Diamond Price Prediction")
    gr.Markdown("Enter diamond details to predict its price")

    with gr.Row():
        carat = gr.Number(label="Carat", value=0.5)
        depth = gr.Number(label="Depth", value=60.0)
        table = gr.Number(label="Table", value=55.0)

    with gr.Row():
        x = gr.Number(label="X (length in mm)", value=5.0)
        y = gr.Number(label="Y (width in mm)", value=5.0)
        z = gr.Number(label="Z (depth in mm)", value=3.0)

    with gr.Row():
        cut = gr.Dropdown(
            ["Fair", "Good", "Very Good", "Premium", "Ideal"],
            label="Cut",
            value="Ideal"
        )
        color = gr.Dropdown(
            ["D", "E", "F", "G", "H", "I", "J"],
            label="Color",
            value="G"
        )
        clarity = gr.Dropdown(
            ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"],
            label="Clarity",
            value="VS1"
        )

    predict_btn = gr.Button("Predict Price 💰")
    output = gr.Textbox(label="Prediction Result")

    predict_btn.click(
        fn=predict_price,
        inputs=[carat, depth, table, x, y, z, cut, color, clarity],
        outputs=output
    )


if __name__ == "__main__":
    demo.launch()
