import streamlit as st


st.set_page_config(
    page_title="Finance Calculator - Problems",
    page_icon="💰",
)

st.title("📝 Investment Decisions")


with open('main_style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

#Problem 1 - Annual Cost-Equivalent Value

def calculate_annuity_payment(pv_annuity, r, n):
    c = pv_annuity * r / (1 - (1 + r) ** -n)
    return c

def Topic4Problem1():
    st.subheader('1) Annual Cost-Equivalent Value')
    st.markdown("Calculate how much additional revenue a company needs to generate (on average, "
                "each year) to recoup the initial investment, given the initial investment, "
                "the interest rate, time period and cash flow for each period.")
    initial_investment = st.number_input('Enter the initial investment', value=1)
    interest_rate_percentage = st.number_input('Enter the interest rate', value=1)
    interest_rate_decimal = interest_rate_percentage / 100.0
    time_period = st.number_input('Enter the time period', value=1)
    cash_flow = st.number_input('Enter the cash flow', value=1)
    res = ""

    if st.button("Calculate Additional Revenue"):
        additional_revenue = calculate_annuity_payment(initial_investment, interest_rate_decimal, time_period)/cash_flow

        res = f'Initial Investment = ${initial_investment}\n'
        res += f'\nInterest Rate = {interest_rate_decimal}%\n'
        res += f'\nTime Period = {time_period} year(s)\n'
        res += f'\nCash Flow = ${cash_flow}\n'
        res += f' \n-------------------------------------'
        res += f'\nAdditional Revenue = {round(additional_revenue, 4)} $/year'

    st.write(res)

Topic4Problem1()

#Problem 2 - Selection Among Investments with Varying Lifetimes

def calculate_present_value(initial_investment, interest_rate, time_period, cash_flow):
    pv = 0
    discount_factor = 1 / ((1 + interest_rate) ** time_period)

    pv += initial_investment + (cash_flow / interest_rate) * (1 - discount_factor)

    return pv

def Topic4Problem2():
    st.subheader('2) Average Operating Cost')
    st.markdown("Calculate the average operating cost given the initial investment, "
                "the interest rate, time period and cash flow for each period.")
    initial_investment = st.number_input('Enter the initial capital', value=1)
    interest_rate_percentage = st.number_input('Enter the discount rate', value=1)
    interest_rate_decimal = interest_rate_percentage / 100.0
    time_period = st.number_input('Enter the duration', value=1)
    cash_flow = st.number_input('Enter the cash movement ', value=1)

    res = ""

    if st.button("Calculate Average Operating Cost"):
        present_value = calculate_present_value(initial_investment, interest_rate_decimal, time_period, cash_flow)
        average_operating_cost = calculate_annuity_payment(present_value, interest_rate_decimal, time_period)

        res = f'Initial Investment = ${initial_investment}\n'
        res += f'\nInterest Rate = {interest_rate_decimal}%\n'
        res += f'\nTime Period = {time_period} year(s)\n'
        res += f'\nCash Flow = ${cash_flow}\n'
        res += f' \n-------------------------------------'
        res += f'\nAverage Operating Cost = {round(average_operating_cost, 2)} $/year'

    st.write(res)

Topic4Problem2()

#Problem 3 - The Optimal Timing of the Investment

def present_value(net_cash_flow, discount_rate, period):
    pv = net_cash_flow / (1 + discount_rate) ** period
    return pv

def Topic4Problem3():
    st.subheader('3) The Optimal Timing of the Investment')
    st.markdown("Calculate the optimal timing of the investment given the future net values of a product, "
                "the interest rate, and time period.")

    num_periods = st.number_input('Enter the number of future periods', min_value=1, value=5, step=1)

    net_cash_flows = []
    present_values = []

    # Present period (Year 0)
    present_cash_flow = st.number_input("Enter net cash flow for Year 0", value=0.0, step=100.0)
    net_cash_flows.append(present_cash_flow)

    # Future periods (Year 1 to Year num_periods)
    for i in range(num_periods):
        net_cash_flow = st.number_input(f"Enter net cash flow for Year {i + 1}", value=0.0, step=100.0)
        net_cash_flows.append(net_cash_flow)

    discount_rate = st.number_input('Enter the discount rate', value=0.05, step=0.01)

    if st.button("Calculate Optimal Year for Investment"):
        for i in range(num_periods + 1):  # Including the present period
            pv = present_value(net_cash_flows[i], discount_rate, i)
            present_values.append(pv)
            st.write(f"Present Value for Year {i} = ${pv:.2f}")

        st.markdown("---")

        max_pv = max(present_values)
        max_index = present_values.index(max_pv)

        st.write(f"\nThe most cost-effective investment is in Year {max_index}.")

Topic4Problem3()

#Problem 4 - Variable Capacity Utilization

def Topic4Problem4():
    st.subheader('4) Variable Capacity Utilization')
    st.markdown("Calculate the perpetual annuity given the yearly production capacity, "
                "operating cost per product and interest rate.")
    yearly_production_capacity = st.number_input('Enter the yearly production capacity', value=1)
    yearly_operating_cost = st.number_input('Enter the operating cost per product', value=1)
    interest_rate_percentage= st.number_input('Enter the finance rate (in percentage)', value=1)
    interest_rate_decimal = interest_rate_percentage / 100.0

    res = ""

    if st.button("Calculate Perpetual Annuity"):
        perpetual_annuity = (yearly_production_capacity*yearly_operating_cost)/interest_rate_decimal

        res = f'Yearly Production Capacity= {yearly_production_capacity} product/year\n'
        res += f'\nOperating Cost per Product = {yearly_operating_cost} $/product\n'
        res += f'\nInterest Rate = {interest_rate_decimal}\n'
        res += f' \n-------------------------------------'
        res += f'\nPerpetual Annuity = ${round(perpetual_annuity, 2)}'

    st.write(res)

Topic4Problem4()
