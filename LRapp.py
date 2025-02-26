
import pickle
import streamlit as st
import pandas as pd

# load the file that contains the model (model.pkl)
with open("LR_model.pkl", "rb") as f:
  model = pickle.load(f)

# give the Streamlit app page a title
st.title("Laptop Price Prediction")

# Reverse mappings
ram_mapping = {0: "4", 1: "8", 2: "16", 3: "32", 4: "64"}
processor_mapping = {0: "Ryzen 3", 1: "Ryzen 5", 2: "Ryzen 7", 3: "Ryzen 9", 4: "Intel i3", 5: "Intel i5", 6: "Intel i7", 7: "Intel i9"}
resolution_mapping = {0: "1366x768", 1: "1920x1080", 2: "2560x1440", 3: "3840x2160"}

# Display radio buttons for user selection
selected_ram = st.radio("Select RAM(GB)", list(ram_mapping.values()))
selected_processor = st.radio("Select Processor", list(processor_mapping.values()))
selected_resolution = st.radio("Select Resolution", list(resolution_mapping.values()))

# Convert back to numeric for prediction
selected_ram_encoded = {v: k for k, v in ram_mapping.items()}[selected_ram]
selected_processor_encoded = {v: k for k, v in processor_mapping.items()}[selected_processor]
selected_resolution_encoded = {v: k for k, v in resolution_mapping.items()}[selected_resolution]

# After selesting price, the user then submits the price value
if st.button("Predict"):
  # take the price value, and format the value the right way
  prediction = model.predict([[selected_ram_encoded, selected_processor_encoded, selected_resolution_encoded]])[0].round(2)
  st.write("The predicted price of laptop is", prediction, "dollars")
