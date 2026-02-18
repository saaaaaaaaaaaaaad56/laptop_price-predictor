import streamlit as st
import pickle

pipe = pickle.load(open("pipe.pkl", "rb"))
df = pickle.load(open("df.pkl", "rb"))

st.title("Laptop Price Predictor")
# streamlit run "files for it/app.py"