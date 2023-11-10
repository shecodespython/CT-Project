import streamlit as st
import subprocess

st.set_page_config(
    page_title="Finance Calculator - Problems",
    page_icon="💰",
)

st.title("📝 Problems Page")


with open('main_style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

with open('problems.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


def run_streamlit_app(file_path):
    subprocess.run(["streamlit", "run", file_path])

st.write("Please select a problem: ")

col1, col2 = st.columns(2)


with col1:
    st.write("1. Seminar - Title")
    st.write("2. Seminar - Title")
    st.write("3. Seminar - Title")
    st.write("4. Seminar - Title")
    st.write("5. Seminar - Title")
    st.write("6. Seminar - Title")
    st.write("7. Seminar - Title")
    st.write("8. Seminar - Title")
    st.write("9. Seminar - Title")
    st.write("10. Seminar - Title")
    st.write("11. Seminar - Title")
    st.write("12. Seminar - Title")

with col2:
    if st.button("Problem 1"):
        run_streamlit_app("Problem_1.py")
    elif st.button("Problem 2"):
        run_streamlit_app("Problem_2.py")
    elif st.button("Problem 3"):
        run_streamlit_app("Problem_3.py")
    elif st.button("Problem 4"):
        run_streamlit_app("Problem_4.py")
    elif st.button("Problem 5"):
        run_streamlit_app("Problem_5.py")
    elif st.button("Problem 6"):
        run_streamlit_app("Problem_6.py")
    elif st.button("Problem 7"):
        run_streamlit_app("Problem_7.py")
    elif st.button("Problem 8"):
        run_streamlit_app("Problem_8.py")
    elif st.button("Problem 9"):
        run_streamlit_app("Problem_9.py")
    elif st.button("Problem 10"):
        run_streamlit_app("Problem_10.py")
    elif st.button("Problem 11"):
        run_streamlit_app("Problem_11.py")
    elif st.button("Problem 12"):
        run_streamlit_app("Problem_12.py")