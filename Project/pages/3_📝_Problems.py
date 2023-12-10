import streamlit as st
import subprocess

st.set_page_config(
    page_title="Finance Calculator - Problems",
    page_icon="💰",
)

st.title("📝 Problems")


with open('main_style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)




def run_streamlit_app(file_path):
    subprocess.run(["streamlit", "run", file_path])

st.write("Please select a problem topic: ")

col1, col2 = st.columns(2)


with col1:
    st.write("1. Topic - PV, FV and NPV")
    st.write("2. Topic - NPV Competitors")
    st.write("3. Topic - Investment Decisions")
    st.write("4. Topic - Dividend Policy")
    st.write("5. Topic - Credit Policy")
    st.write("6. Topic - WACC, CAPM and Tax Savings")
    st.write("7. Topic - Commercial Credit Policy and Inventory Management")

with col2:
    if st.button("Topic 1"):
        run_streamlit_app("Topic_1.py")
    elif st.button("Topic 2"):
        run_streamlit_app("Topic_2.py")
    elif st.button("Topic 3"):
        run_streamlit_app("Topic_3.py")
    elif st.button("Topic 4"):
        run_streamlit_app("Topic_4.py")
    elif st.button("Topic 5"):
        run_streamlit_app("Topic_5.py")
    elif st.button("Topic 6"):
        run_streamlit_app("Topic_6.py")
    elif st.button("Topic 7"):
        run_streamlit_app("Topic_7.py")



