import streamlit as st
import numpy_financial as npf


st.set_page_config(
    page_title="Finance Calculator - Problems",
    page_icon="💰",
)

st.title("📝 NPV Competitors")



#Style
with open('main_style.css') as f:
     css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

with open('problems2.css') as f:
     css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


#Problem 1 - Return on Book Value/Book Value Return
def Topic3Problem1():
    st.markdown('#### 1) Return on Book Value (ROBV)')
    st.markdown("Calculate the return on book value when given the average expected profit "
                "(after amortization and after-tax) from the investment's implementation "
                "and the average book value of the investment.")
    
    col1, col2 = st.columns(2)

    with col1:
        average_expected_profit = st.number_input('Enter the average expected profit', value=1)
    
    with col2:
        average_book_value = st.number_input('Enter the average book value', value=1)

    res = ""

    if st.button("Calculate Book Value Return"):
        book_value_return = average_expected_profit / average_book_value

        res = f'##### Average Expected Profit = ${average_expected_profit}\n'
        res += f'\n ##### Average Book Value = ${average_book_value}\n'
        res += f'\n ##### Return on Book Value = {round(book_value_return * 100, 2)}%'

    st.write('\n')
    st.write(res)
    st.write('\n')  
    st.write('\n')
    st.write('\n')

Topic3Problem1()

#Problem 2 - Payback Period
def Topic3Problem2():
    st.markdown('#### 2) Payback Period (PBP/PP)')
    st.markdown("Calculate the payback period for the investment to recover its initial investment"
                " given the initial investment value and annual cash flow.")
    
    col1, col2 = st.columns(2)

    with col1:
        initial_investment = st.number_input('Enter the initial investment', value=1)
    
    with col2:
        annual_cash_flow = st.number_input('Enter the annual cash flow', value=1)

    res = ""

    if st.button("Calculate Payback Period"):
        payback_period = initial_investment/annual_cash_flow

        res = f'##### Initial Investment = ${initial_investment}\n'
        res += f'\n##### Annual Cash Flow = ${annual_cash_flow}\n'
        res += f'\n##### Payback Period = {round(payback_period, 2)} year(s)'

    st.write('\n')
    st.write(res)
    st.write('\n')  
    st.write('\n')
    st.write('\n')

Topic3Problem2()

#Problem 3 - Profitability Index
def Topic3Problem3():
    st.markdown('#### 3) Profitability Index (PI)')
    st.markdown("Calculate the profitability index given the net present value and initial investment of a project.")

    col1, col2 = st.columns(2)

    with col1:
        net_present_value = st.number_input('Enter the net present value', value=1)
    
    with col2:
        initial_investment = st.number_input('Enter the initial capital', value=1)

    res = ""

    if st.button("Calculate Profitability Index"):
        profitability_index = net_present_value/initial_investment

        res = f'##### Net Present Value = ${net_present_value}\n'
        res += f'\n##### Initial Investment = ${initial_investment}\n'
        res += f'\n##### Profitability Index = {round(profitability_index, 2)}'

    st.write('\n')
    st.write(res)
    st.write('\n')  
    st.write('\n')
    st.write('\n')

Topic3Problem3()

#Problem 4 - Internal Rate of Return

def Topic3Problem4():
    st.markdown('#### 4) Internal Rate of Return (IRR)')
    st.markdown("Calculate the internal rate of return given the initial investment, time period, "
                "interest rate and cash flow for each period.")
    
    col1, col2 = st.columns(2)

    with col1:
        initial_investment = st.number_input("Initial Investment", value=1)
    
    with col2:
        time_period = st.number_input("Time Period", min_value=1, value=1)

    with col1:
        cash_flows = [st.number_input(f"Year {t+1} Cash Flow", key=f"cf_{t}") for t in range(time_period)]

    res = ""

    # Calculate IRR
    if st.button("Calculate IRR"):
        cash_flows = [-initial_investment] + cash_flows  # Include the initial investment as a negative cash flow
        irr = npf.irr(cash_flows)

        # Update the result string
        res = f'##### Initial Investment = ${initial_investment}\n'
        res += f'\n##### Time Period = {time_period} year(s)\n'
        res += f'\n##### Cash Flows = {", ".join(map(str, cash_flows[1:]))}\n'
        res += f'\n##### Internal Rate of Return (IRR) = {irr:.2%}'

    st.write('\n')
    st.write(res)
    st.write('\n')  
    st.write('\n')
    st.write('\n')

Topic3Problem4()
