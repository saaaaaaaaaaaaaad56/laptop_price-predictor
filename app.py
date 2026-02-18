# streamlit run app.py
import streamlit as st
import pickle

pipe = pickle.load(open("pipe.pkl", "rb"))
df = pickle.load(open("df.pkl", "rb"))

st.title("Laptop Price Predictor")
# streamlit run "files for it/app.py"



# Brand
company = st.selectbox('Brand',df['Company'].unique())


#  Laptop Type
Laptop_type = st.selectbox('Laptop_type',df['TypeName'].unique())


#  Ram
RAM = st.selectbox('Ram(in Gb',df['Ram'].unique())



