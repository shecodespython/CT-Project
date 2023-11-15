import streamlit as st

st.set_page_config(
    page_title="Finance Calculator - Problems",
    page_icon="💰",
)

st.title("📝 Dividend Policy")


with open('main_style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


# Calculator Functions

def sp_calc(epv, n):
    return epv / n

def n_calc(epv, sp):
    return epv / sp

def epv_calc(sp, n):
    return sp * n

def epv_aft_div_pay_calc(epv, sum):
    return epv - sum

def sp_aft_div_pay_calc(epv, sp, sum):
    return epv_aft_div_pay_calc(epv, sum) / n_calc(epv, sp)

def n_aft_is_calc(epv, sp, n, sum):
    return n + sum / sp

def epv_aft_st_bb(epv, sum):
    return epv - sum

def n_aft_st_bb(sp, n, sum):
    return n - sum / sp

def sp_aft_st_bb(epv, sp, n, sum):
    return epv_aft_st_bb(epv, sum) / n_aft_st_bb(sp, n, sum)

def ds_when_ye(sum, n):
    return sum / n

def sp_when_ye(sum, n, ye):
    return ds_when_ye(sum, n) / (ye / 100)

def epv_when_ye(sum, n, ye):
    return sp_when_ye(sum, n, ye) * n

def n_aft_spl(n, np):
    return  n * np

def eq_aft_spl(n, sp, np):
    return n * fv / n_aft_spl(n, np)

def sp_aft_spl(n, fv, np):
    return n * sp / n_aft_spl(n, np)

def n_aft_cons(n, np):
    return  n / np

def eq_aft_cons(n, sp, np):
    return n * fv / n_aft_cons(n, np)

def sp_aft_cons(n, fv, np):
    return n * sp / n_aft_cons(n, np)



# Problem forms

# Stock Price
with st.form("Stock Price"):
    st.write(f"Stock Price - Calculation")
    
    epv = st.number_input("Enterprise value: ")
    n = st.number_input("Number of Stocks: ")

    submitted = st.form_submit_button("Calculate SP")

if submitted:
    st.write(f"The stock price is: {sp_calc(epv, n):.2f}")



# Number of Stocks
with st.form("Number of Stocks"):
    st.write(f"Number of Stocks - Calculation")
    
    epv = st.number_input("Enterprise value: ")
    sp = st.number_input("Stock Price: ")

    submitted = st.form_submit_button("Calculate n")

if submitted:
    st.write(f"The number of stocks is: {n_calc(epv, sp):.2f}")



# Enterprise Value
with st.form("Enterprise Value"):
    st.write(f"Enterprise Value - Calculation")
    
    sp = st.number_input("Stock Price: ")
    n = st.number_input("Number of Stocks: ")

    submitted = st.form_submit_button("Calculate EPV")

if submitted:
    st.write(f"The enterprise value is: {epv_calc(sp, n):.2f}")



# Enterprise Value, Stock Price and Number of Stocks after Dividend Payment
with st.form("Enterprise Value, Stock Price and Number of Stocks after Dividend Payment"):
    st.write(f"Enterprise Value, Stock Price and Number of Stocks after Dividend Payment - Calculation")
    
    epv = st.number_input("Enterprise value before payment: ")
    sp = st.number_input("Stock Price before payment: ")
    sum = st.number_input("Sum paid as dividends: ")

    submitted = st.form_submit_button("Calculate")

if submitted:
    st.write(f"The enterprise value after dividend payment is: {epv_aft_div_pay_calc(epv, sum):.2f}")
    st.write(f"The stock price after dividend payment is: {sp_aft_div_pay_calc(epv, sp, sum):.2f}")
    st.write(f"The number of stocks after dividend payment is: {n_calc(epv, sp):.2f}")



# Enterprise Value, Stock Price and Number of Stocks after Stock Issuance
with st.form("Enterprise Value, Stock Price and Number of Stocks after Stock Issuance"):
    st.write(f"Enterprise Value, Stock Price and Number of Stocks after Stock Issuance - Calculation")
    
    epv = st.number_input("Enterprise value before issuance: ")
    sp = st.number_input("Stock Price before issuance: ")
    n = st.number_input("Number of stocks before issuance: ")
    sum = st.number_input("Value issued: ")

    submitted = st.form_submit_button("Calculate")

if submitted:
    st.write(f"The enterprise value after after stock issuance is: {epv:.2f}")
    st.write(f"The stock price after stock issuance is: {sp:.2f}")
    st.write(f"The the number of stocks after stock issuance is: {n_aft_is_calc(epv, sp, n, sum):.2f}")




# Enterprise Value, Stock Price and Number of Stocks after Stock Buyback
with st.form("Enterprise Value, Stock Price and Number of Stocks after Stock Buyback"):
    st.write(f"Enterprise Value, Stock Price and Number of Stocks after Stock Buyback - Calculation")
    
    epv = st.number_input("Enterprise value before buyback: ")
    sp = st.number_input("Stock Price before buyback: ")
    n = st.number_input("Number of stocks before buyback: ")
    sum = st.number_input("Value issued: ")

    submitted = st.form_submit_button("Calculate")

if submitted:
    st.write(f"The enterprise value after after stock buyback is: {epv_aft_st_bb(epv, sum):.2f}")
    st.write(f"The stock price after stock buyback is: {sp_aft_st_bb(epv, sp, n, sum):.2f}")
    st.write(f"The the number of stocks after stock buyback is: {n_aft_st_bb(sp, n, sum):.2f}")



# Enterprise Value, Stock Price, Number of Stocks and Dividend if there is a Yield Expectation
with st.form("Enterprise Value, Stock Price, Number of Stocks and Dividend if there is a Yield Expectation"):
    st.write(f"Enterprise Value, Stock Price, Number of Stocks and Dividend if there is a Yield Expectation - Calculation")
    
    n = st.number_input("Number of stocks: ")
    sum = st.number_input("Sum paid as dividends: ")
    ye = st.number_input("Investors' yield expectation (%): ")

    submitted = st.form_submit_button("Calculate")

if submitted:
    st.write(f"The enterprise value after dividend payment is: {epv_when_ye(sum, n, ye):.2f}")
    st.write(f"The stock price after dividend payment is: {sp_when_ye(sum, n, ye):.2f}")
    st.write(f"The number of stocks after dividend payment is: {n:.2f}")
    st.write(f"The dividend/share payment is: {ds_when_ye(sum, n):.2f}")



# Change in Equity and Stock Price when the stocks are split into n parts
with st.form("Change in Equity and Stock Price when the stocks are split into n parts"):
    st.write(f"Change in Equity and Stock Price when the stocks are split into n parts - Calculation")
    
    n = st.number_input("Number of stocks: ")
    sp = st.number_input("Stock price: ")
    fv = st.number_input("Face value: ")
    np = st.number_input("n: ")

    submitted = st.form_submit_button("Calculate")

if submitted:
    st.write(f"The equity after the split is: {eq_aft_spl(n, sp, np):.2f}")
    st.write(f"The stock price after the split is: {sp_aft_spl(n, fv, np):.2f}")
    st.write(f"The number of stocks after the split is: {n_aft_spl(n, np):.2f}")



# Change in Equity and Stock Price when the stocks are consolidated from n parts
with st.form("Change in Equity and Stock Price when the stocks are consolidated from n parts"):
    st.write(f"Change in Equity and Stock Price when the stocks are consolidated from n parts - Calculation")
    
    n = st.number_input("Number of stocks: ")
    sp = st.number_input("Stock price: ")
    fv = st.number_input("Face value: ")
    np = st.number_input("n: ")

    submitted = st.form_submit_button("Calculate")

if submitted:
    st.write(f"The equity after the consolidation is: {eq_aft_cons(n, sp, np):.2f}")
    st.write(f"The stock price after the consolidation is: {sp_aft_cons(n, fv, np):.2f}")
    st.write(f"The number of stocks after the consolidation is: {n_aft_cons(n, np):.2f}")
