import streamlit as st

st.set_page_config(
    page_title="Finance Calculator - Problems",
    page_icon="💰",
)

st.title("📝 WACC, CAPM and Tax Savings")


with open('main_style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

#Problem 1 - Cost of Equity

def Topic10Problem1():
    st.subheader('1) Capital Asset Pricing Model (CAPM) - Cost of Equity (Expected Return on Equity, rE)')
    st.markdown("*Note that a similar formula can be applied to calculate the cost of dept (rD).")
    st.markdown("Calculate the Expected Return on Equity given the risk-free rate, "
                "the systematic risk (beta of the stock) and the expected market return.")
    risk_free_rate = st.number_input('Enter the risk-free rate', value=1.0)
    beta_of_the_stock = st.number_input('Enter the beta of the stock', value=1.0)
    expected_market_return = st.number_input('Enter the expected market return', value=1.0)

    res = ""

    if st.button("Calculate Expected Return on Equity"):
        capital_asset_pricing_model = risk_free_rate + beta_of_the_stock*(expected_market_return-risk_free_rate)

        res += f'Risk-Free Rate = {risk_free_rate}%\n'
        res += f'\nBeta of The Stock = {beta_of_the_stock}\n'
        res += f'\nExpected Market Return = {expected_market_return}%\n'
        res += f' \n-------------------------------------'
        res += f'\nExpected Return on Equity = {round(capital_asset_pricing_model, 2)}%'

    st.write(res)

Topic10Problem1()

#Problem 2 - Beta of a Leveraged Company's Assets

def Topic10Problem2():
    st.subheader('2) Beta of a Leveraged Company\'s Assets (βA)')
    st.markdown("Calculate the beta of the assets given the beta of equity, "
                "the market value of equity, the total market value of equity and debt, "
                "the beta of debt and the market value of debt.")
    beta_of_equity = st.number_input('Enter the beta of equity', value=1.0)
    market_value_of_equity = st.number_input('Enter the market value of equity', value=1.0)
    total_market_value_of_equity_and_debt = st.number_input('Enter the total market value of equity and debt', value=1.0)
    beta_of_debt = st.number_input('Enter the beta of debt', value=1.0)
    market_value_of_debt = st.number_input('Enter the market value of debt', value=1.0)

    res = ""

    if st.button("Calculate Beta of Assets"):
        beta_of_assets = beta_of_equity*market_value_of_equity/total_market_value_of_equity_and_debt + beta_of_debt*market_value_of_debt/total_market_value_of_equity_and_debt

        res = f'Beta of Equity = {beta_of_equity}%\n'
        res += f'\nMarket Value of Equity = ${market_value_of_equity}\n'
        res += f'\nTotal Market Value of Equity and Debt = ${total_market_value_of_equity_and_debt}\n'
        res += f'\nBeta of Debt = {beta_of_debt}%\n'
        res += f'\nMarket Value of Debt = ${market_value_of_debt}\n'
        res += f' \n-------------------------------------'
        res += f'\nWeighted Average Cost of Capital = {round(beta_of_assets, 2)}%'

    st.write(res)

Topic10Problem2()

#Problem 3 - WACC

def Topic10Problem3():
    st.subheader('3) Weighted Average Cost of Capital (WACC/rA)')
    st.markdown("Calculate the Weighted Average Cost of Capital given the cost of equity, "
                "the market value of equity, the total market value of equity and debt, "
                "the cost of debt and the market value of debt.")
    cost_of_equity = st.number_input('Enter the cost of equity', value=1.0)
    market_value_of_equity = st.number_input('Enter the equity market value', value=1.0)
    total_market_value_of_equity_and_debt = st.number_input('Enter the total market value (of equity and debt)', value=1.0)
    cost_of_debt = st.number_input('Enter the cost of debt', value=1.0)
    market_value_of_debt = st.number_input('Enter the dept market value', value=1.0)

    res = ""

    if st.button("Calculate WACC"):
        weighted_average_cost_of_capital = cost_of_equity*market_value_of_equity/total_market_value_of_equity_and_debt + cost_of_debt*market_value_of_debt/total_market_value_of_equity_and_debt

        res = f'Cost of Equity = {cost_of_equity}%\n'
        res += f'\nMarket Value of Equity = ${market_value_of_equity}\n'
        res += f'\nTotal Market Value of Equity and Debt = ${total_market_value_of_equity_and_debt}\n'
        res += f'\nCost of Debt = {cost_of_debt}%\n'
        res += f'\nMarket Value of Debt = ${market_value_of_debt}\n'
        res += f' \n-------------------------------------'
        res += f'\nWeighted Average Cost of Capital = {round(weighted_average_cost_of_capital, 2)}%'

    st.write(res)

Topic10Problem3()

#Problem 4 - WACC Calculation Using Corporate Tax Rate

def Topic10Problem4():
    st.subheader('4) Weighted Average Cost of Capital (WACC/rA) Using the Corporate Tax Rate (TC)')
    st.markdown("Calculate the expected return on assets given the cost of equity, "
                "the market value of equity, the total market value of equity and debt, "
                "the cost of debt, corporate tax rate, and the market value of debt.")

    cost_of_equity = st.number_input('Enter the equity cost', value=1.0)
    market_value_of_equity = st.number_input('Enter the market value for the equity', value=1.0)
    total_market_value_of_equity_and_debt = st.number_input('Enter the total market value', value=1.0)
    cost_of_debt = st.number_input('Enter the debt cost', value=1.0)
    corporate_tax_rate = st.number_input('Enter the corporate tax rate', value=1.0)
    market_value_of_debt = st.number_input('Enter the market value for the debt', value=1.0)

    res = ""

    if st.button("Calculate Expected Return on Assets"):
        E_per_V = market_value_of_equity / total_market_value_of_equity_and_debt
        D_per_V = market_value_of_debt / total_market_value_of_equity_and_debt
        corporate_tax_rate_decimal = corporate_tax_rate / 100
        expected_return_on_assets = cost_of_equity * E_per_V + cost_of_debt * (1 - corporate_tax_rate_decimal) * D_per_V

        res = f'Cost of Equity = {cost_of_equity}%\n'
        res += f'\nMarket Value of Equity = ${market_value_of_equity}\n'
        res += f'\nTotal Market Value of Equity and Debt = ${total_market_value_of_equity_and_debt}\n'
        res += f'\nCost of Debt = {cost_of_debt}%\n'
        res += f'\nCorporate Tax Rate = {corporate_tax_rate}%\n'
        res += f'\nMarket Value of Debt = ${market_value_of_debt}\n'
        res += f' \n-------------------------------------'
        res += f'\nExpected Return on Assets = {round(expected_return_on_assets, 2)}%'

    st.write(res)

Topic10Problem4()

#Problem 5 - Tax Savings

def calculate_taxes(ebit, interest_rate, profit_tax_rate):
    # Calculations

    interest_rate_decimal = interest_rate / 100
    profit_tax_rate_decimal = profit_tax_rate / 100

    interest = ebit * interest_rate_decimal
    ebt = ebit - interest
    profit_tax = ebt * profit_tax_rate_decimal
    shareholders_income = ebit - profit_tax
    combined_income = shareholders_income + interest
    tax_savings_due_to_interest = interest * profit_tax_rate_decimal

    return [
        ("Earnings Before Interest and Tax", ebit),
        ("Interest Rate", interest_rate),
        ("Profit Tax Rate", profit_tax_rate),
        ("Interest", interest),
        ("EBT", ebt),
        ("Profit Tax", profit_tax),
        ("Shareholders' Income", shareholders_income),
        ("Combined Income", combined_income),
        ("Tax Savings due to Interest", tax_savings_due_to_interest)
    ]


def Topic10Problem5():
    st.subheader('5) Tax Savings')
    st.markdown("Calculate the tax savings given the earnings before interest and tax,"
                " interest rate and profit tax rate.")

    ebit = st.number_input("Enter the earnings before interest and tax:", value=0.0)
    interest_rate = st.number_input("Enter the interest rate:", value=0.0)
    profit_tax_rate = st.number_input("Enter the profit tax rate:", value=0.0)

    if st.button("Calculate Taxes"):
        results = calculate_taxes(ebit, interest_rate, profit_tax_rate)
        df = pd.DataFrame(results, columns=["Name", "Value"])
        st.dataframe(df)

Topic10Problem5()

#Problem 6 - Present Value of Tax Savings

def Topic10Problem6():
    st.subheader('6) Present Value of Tax Savings')
    st.markdown("Calculate the present value of tax savings given the loan,interest rate and corporate tax rate.")

    loan = st.number_input("Enter the value of the loan:", value=0.0)
    interest_rate = st.number_input("Enter the loan's interest rate:", value=0.0)
    corporate_tax_rate = st.number_input("Enter the corporate tax rate:", value=0.0)

    st.markdown("*For calculating the present value the maturity and repayment of the loan "
                "need to be specified. In this calculator the loan has 1 year maturity and "
                "no repayment until maturity. For calculating various present values, go to Topic 1")

    res = ""

    if st.button("Calculate PV of Tax Savings"):
        interest = loan * (interest_rate/100)
        tax_savings = interest * (corporate_tax_rate/100)
        tax_savings_pv = tax_savings / (1 + interest_rate/100)

        res = f'Loan = ${loan}\n'
        res += f'\nInterest Rate = {interest_rate}%\n'
        res += f'\nCorporate Tax Rate = {corporate_tax_rate}%\n'
        res += f'\n-------------------------------------\n'
        res += f'Present Value of Tax Savings\n = ${round(tax_savings_pv, 2)}'

    st.write(res)

Topic10Problem6()
