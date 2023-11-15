import streamlit as st


st.set_page_config(
    page_title="Finance Calculator - Problems",
    page_icon="💰",
)

st.title("📝 NPV Competitors")


with open('main_style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
