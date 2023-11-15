import streamlit as st
import subprocess


st.set_page_config(
    page_title="Finance Calculator",
    page_icon="💰",
)

st.title("🏠 Homepage")

#Using CSS file
with open('main_style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

