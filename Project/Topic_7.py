import streamlit as st
from Topic_7_problems import *

st.set_page_config(
    page_title="Finance Calculator - Problems",
    page_icon="💰",
)

st.title("📝 Commercial Credit Policy and Inventory Management")


with open('main_style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

with open('topic7.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.write("1. A manufacturing company sells its irons at a wholesale price of 50 dollars. The iron production cost is $40. There is a 25% chance that a dealer who orders 1000 irons and he asks for a payment deferment, he goes bankrupt the following year.")
st.write("a. Do we accept the order? (We assume that all traders are 1000 at the same time he orders a piece of iron and either pays everything or nothing.)")
first_a()

st.write("b. What is the minimum price at which an iron must be sold in order for the order to be accepted?")
first_b()

st.write("c. If we want to achieve a profit in proportion to sales of 5%, how big should the sales bevprice?")
first_c()

st.write("2. Let's say that a company currently has 15,000 lei in accounts receivable. For what value and how much percent, if the company increases the average payment delay from 35 days to 45 per day (assuming all other factors remain the same)? How old is she additional financing costs arise for the company, if the cost of short-term funds 7.5%?")
second()

st.write("3. A bookstore is experiencing steady demand for Game of Thrones. The business sells 100 copies of the book a year. The storage costs of the set are 4 lei/book. All orders a there is a fixed cost of 2 lei from the publisher.")
st.write("a. How many books should I order in one order? How many orders should the shop place? year? What is the store's average inventory? What is the cost of keeping stock (total cost)?")
third_a()

st.write("b. If you order 5 times a year, i.e. N = 5, you will have too many books in stock, they will be high storage and financing costs:")
third_b()

st.write("4. The bookstore is experiencing an increase in demand for the Game of Thrones book. From now on from then on, it is expected to sell books worth 4,320 lei per year. The price of a book is 20 lei. The order costs remain at the level of 2 lei. The book has no storage cost, but it does annual interest rate 30%. How many orders should the store place in a year? How many books should one order when ordering? What is the cost of keeping stock (total cost)?")
fourth()