import streamlit as st
import pandas as pd

st.title("Placement Data Analyzer")

uploaded_file = st.file_uploader("Upload placement CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Dataset Preview:")
    st.dataframe(df)

    if "CTC" in df.columns:
        st.subheader("CTC Distribution")
        st.bar_chart(df["CTC"])
    else:
        st.warning("Please ensure there is a 'CTC' column in the dataset.")
else:
    st.info("Upload a CSV file to analyze placement data.")
