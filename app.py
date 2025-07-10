import streamlit as st
import os
from datetime import datetime

def load_summary(date_str):
    filename = f"output/daily_summary_{date_str}.txt"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return f.read()
    else:
        return None

st.set_page_config(page_title="Daily Sports Summary", layout="centered")
st.title("📅 Daily Sports Summary")

selected_date = st.date_input("Select a date", datetime.now())
date_str = selected_date.strftime("%Y-%m-%d")

summary_text = load_summary(date_str)

if summary_text:
    st.markdown(f"```\n{summary_text}\n```")
else:
    st.info(f"No summary available for {date_str}. Please run the pipeline for this date.")