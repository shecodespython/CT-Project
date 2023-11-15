import streamlit as st
from Topic_5_problems import *

st.set_page_config(
    page_title="Finance Calculator - Problems",
    page_icon="💰",
)

st.title("📝 Credit Policy")


with open('main_style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


with open('topic5.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


st.write("1. A company is fully financing itself through its own shares. There are 1,000 _ shares in circulation, each worth 10 _ dollars. The company expects to earn 1,500 _ dollars in annual revenue, although this amount is not guaranteed. However, we can confirm that all profits will be distributed to shareholders in the form of dividends. For now, let's ignore taxes.")
st.write("a. Let's calculate the market value of the company.")
first_a()

st.write("b. Calculate the earnings per share and dividend yield for 500, 1,000, 1,500, and 2,000 _ dollar operating profits.")
first_b()

st.write("c. The company's managers are considering financing the company equally with debt and equity. They plan to issue $5,000 _ worth of bonds with a 10% _ interest rate and use the proceeds to buy back 500 _ shares of stock. How will this affect the company's market value? What about the earnings per share and dividend yield under different operating profit scenarios?")
first_c()

st.write("d. Suppose an investor wants to increase their expected return on investment without taking into account the risk that the company may not take out a loan. Assume the investor has $10 _ available to invest. How can they do this?")
first_d()

st.write("2. A company is currently financed entirely by equity capital. The share capital is expected return is 16% _. The company wants to exchange 30% _ of its share capital with a loan. The loan interest rate is 10% _. What is the expected return on share capital after taking out a loan? What is the company's weighted average cost after taking out a loan?")
second()

st.write("3. A company's foreign capital/own capital ratio is currently 0.7 _ . The cost of the loan is 11% _, the shareholders return expected by 14% _. What should the company do if it decides that from now on 45% _ do you want to finance the company with your own capital, without changing the value of the company? How would the return required by shareholders change?")
third()

st.write("5. A company's stock and bonds have a market value of 50  _ million dollars and 30 _ million dollars, respectively. The investors they currently expect a return of 16% _ for stocks and 8%  _ for bonds. What would happen with the expected return on the stock if the company issues an additional 10 _ million dollars worth of stock and use this money to repay debt?")
fifth()