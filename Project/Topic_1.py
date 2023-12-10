import streamlit as st

st.set_page_config(
    page_title="Finance Calculator - Problems",
    page_icon="💰",
)

st.title("📝 PV, FV and NPV")


with open('main_style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


# Calculator Functions

def fv_calc(c0, n, r):
    return c0 * pow((1 + r / 100), n)

def pv_calc(cn, n, r):
    return cn / pow((1 + r / 100), n)

def r_calc(cn, c0, n):
    return (pow(cn / c0, 1 / n) - 1) * 100

def pv_perp_calc(c, r):
    return c / (r / 100)

def c_perp_calc(c0, r):
    return c0 * (r / 100)

def r_perp_calc(c0, c):
    return (c / c0) * 100

def pv_inc_ann_calc(c, r, g):
    return c / (r / 100 - g / 100)

def c_inc_ann_calc(c0, r, g):
    return c0 * (r / 100 - g / 100)

def r_inc_ann_calc(c, c0, g):
    return (c / c0 + g / 100) * 100

def g_inc_ann_calc(c, c0, r):
    return (r / 100 - c / c0) * 100

def pv_ann_calc(c, r, n):
    return (c / (r / 100)) * (1 - 1 / pow((1 + r / 100), n))

def c_ann_calc(c0, r, n):
    return (c0 * (r / 100) * pow((1 + r / 100), n)) / (pow((1 + r / 100), n) - 1)

def npv_calc(c0, i0, c, r, n):
    n = int(n)
    npv = c0 - i0
    for i in range(n):
        npv =  npv + (c[i] / pow((1 + r / 100), i + 1))
    return npv

def npv_var_r_calc(c0, i0, c, r, n):
    n = int(n)
    npv = c0 - i0
    for i in range(n):
        f = 1
        for j in range(i + 1):
            f =  f * (1 + r[j] / 100)
        npv =  npv + (c[i] / f)
    return npv





# Problem forms

# FV
with st.form("FV"):
    st.write(f"#### 1) Future Value (FV/Cn) - Calculation")
    
    col1, col2 = st.columns(2)

    with col1:
        c0 = st.number_input("C0/PV: ", value=1)
        n = st.number_input("n: ", value=1)

    with col2:
        r = st.number_input("r (%): ", value=1)

    submitted = st.form_submit_button("Calculate FV")

if submitted:
    st.write(f"##### The future value of this amount of money is: {fv_calc(c0, n, r):.2f}")



# PV
with st.form("PV"):
    st.write(f"#### 2) Present Value (PV/C0) - Calculation")

    col1, col2 = st.columns(2)


    with col1:
        cn = st.number_input("Cn/FV: ", value=1)
        r = st.number_input("r (%): ", value=1)


    with col2:
        n = st.number_input("n: ", value=1)

    submitted = st.form_submit_button("Calculate PV")

if submitted:
    st.write(f"##### The present value of this amount of money is: {pv_calc(cn, n, r):.2f}")



# r
with st.form("r"):
    st.write(f"#### 3) Discount/Interest Rate (r) - Calculation")

    col1, col2 = st.columns(2)


    with col1:
        cn = st.number_input("Cn/FV: ", value=1)
        n = st.number_input("n: ", value=1)

    with col2:    
        c0 = st.number_input("C0/PV: ", value=1)

    submitted = st.form_submit_button("Calculate r")

if submitted:
    st.write(f"##### The interest/discount rate is: {r_calc(cn, c0, n):.2f} %")



# PV perp
with st.form("PV Perpetuity"):
    st.write(f"#### 4) Present Value (PV/C0) of a Perpetuity - Calculation")
    
    col1, col2 = st.columns(2)

    with col1:
        c = st.number_input("C: ", value=1)

    with col2:
        r = st.number_input("r (%): ", value=1)

    submitted = st.form_submit_button("Calculate PV")

if submitted:
    st.write(f"##### The present value of this perpetuity is: {pv_perp_calc(c, r):.2f}")



# C perp
with st.form("C Perpetuity"):
    st.write(f"#### 5) Yearly amount (C) of a Perpetuity - Calculation")

    col1, col2 = st.columns(2)

    with col1:
        c0 = st.number_input("C0/PV: ", value=1)

    with col2:
        r = st.number_input("r (%): ", value=1)

    submitted = st.form_submit_button("Calculate C")

if submitted:
    st.write(f"##### The yearly amount of this perpetuity is: {c_perp_calc(c0, r):.2f}")



# r perp
with st.form("r Perpetuity"):
    st.write(f"#### 6) Interest/Discount Rate (r) of a Perpetuity - Calculation")
    
    col1, col2 = st.columns(2)

    with col1:
        c0 = st.number_input("C0/PV: ", value=1)
    
    with col2:
        c = st.number_input("C: ")

    submitted = st.form_submit_button("Calculate r")

if submitted:
    st.write(f"##### The interest/discount rate of this perpetuity is: {r_perp_calc(c0, c):.2f} %")



# PV inc ann
with st.form("PV Increasing Annuity"):
    st.write(f"#### 7) Present Value (PV) of a Increasing Annuity - Calculation")
    
    col1, col2 = st.columns(2)

    with col1:
        c = st.number_input("C: ", value=1)
        g = st.number_input("g (%): ", value=1)

    with col2:
        r = st.number_input("r (%): ", value=1)

    submitted = st.form_submit_button("Calculate PV")

if submitted:
    st.write(f"##### The present value of this increasing annuity is: {pv_inc_ann_calc(c, r, g):.2f}")



# C inc ann
with st.form("C Increasing Annuity"):
    st.write(f"#### 8) Yearly Value (C) of a Increasing Annuity - Calculation")
    
    col1, col2 = st.columns(2)

    with col1:
        c0 = st.number_input("C0/PV: ", value=1)
        g = st.number_input("g (%): ", value=1)

    with col2:
        r = st.number_input("r (%): ", value=1)

    submitted = st.form_submit_button("Calculate C")

if submitted:
    st.write(f"##### The yearly amount of this increasing annuity is: {c_inc_ann_calc(c0, r, g):.2f}")



# r inc ann
with st.form("r Increasing Annuity"):
    st.write(f"#### 9) Interest/Discount Rate (r) of a Increasing Annuity - Calculation")
    
    col1, col2 = st.columns(2)

    with col1:
        c = st.number_input("C: ", value=1)
        g = st.number_input("g (%): ", value=1)

    with col2:
        c0 = st.number_input("C0/PV: ", value=1)

    submitted = st.form_submit_button("Calculate r")

if submitted:
    st.write(f"##### The interest/discount rate of this increasing annuity is: {r_inc_ann_calc(c, c0, g):.2f} %")



# g inc ann
with st.form("g Increasing Annuity"):
    st.write(f"#### 10) Growth Rate (g) of a Increasing Annuity - Calculation")
    
    col1, col2 = st.columns(2)

    with col1:
        c = st.number_input("C: ", value=1)
        r = st.number_input("r (%): ", value=1)
    
    with col2:
        c0 = st.number_input("C0/PV: ", value=1)

    submitted = st.form_submit_button("Calculate g")

if submitted:
    st.write(f"##### The growth rate of this increasing annuity is: {g_inc_ann_calc(c, c0, r):.2f} %")



# PV ann
with st.form("PV Annuity"):
    st.write(f"#### 11) Present Value (PV) of an Annuity - Calculation")

    col1, col2 = st.columns(2)

    with col1:
        c = st.number_input("C: ", value=1)
        n = st.number_input("n: ", value=1)
    
    with col2:
        r = st.number_input("r (%): ", value=1)

    submitted = st.form_submit_button("Calculate PV")

if submitted:
    st.write(f"##### The present value of this annuity is: {pv_ann_calc(c, r, n):.2f}")



# C ann
with st.form("C Annuity"):
    st.write(f"#### 12) Yearly Amount (C) of an Annuity - Calculation")
    
    col1, col2 = st.columns(2)

    with col1:
        c0 = st.number_input("C0/PV: ", value=1)
        n = st.number_input("n: ", value=1)
    
    with col2:
        r = st.number_input("r (%): ", value=1)

    submitted = st.form_submit_button("Calculate C")

if submitted:
    st.write(f"##### The yearly amount of this annuity is: {c_ann_calc(c0, r, n):.2f}")



# NPV
with st.form("NPV"):
    st.write(f"#### 13) Net Present Value (NPV) - Calculation")
    
    col1, col2 = st.columns(2)

    with col1:
        i0 = st.number_input("I0: ", value=1)
        r = st.number_input("r (%): ", value=1)

    with col2:
        c0 = st.number_input("C0: ", value=1)
        n = st.number_input("n: ", value=1)
    
    c = []
    for i in range(int(n)):
        key = i
        ci = st.number_input(f"C{i + 1}: ", key=key)
        c.append(ci)
   
    submitted = st.form_submit_button("Calculate NPV")

if submitted:
    st.write(f"##### The net present value is: {npv_calc(c0, i0, c, r, n):.2f}")



# NPV variable r
with st.form("NPV variable r"):
    st.write(f"#### 14) Net Present Value (NPV) with Variable r - Calculation")
    
    col1, col2 = st.columns(2)

    with col1:
        i0 = st.number_input("I0: ", value=1)
        n = st.number_input("n: ", value=1)

    with col2:
        c0 = st.number_input("C0: ", value=1)
    
    c = []
    r = []
    for i in range(int(n)):
        key = f"c_{i}"
        ci = st.number_input(f"C{i + 1}: ", key=key,)
        c.append(ci)

    for i in range(int(n)):
        key = f"f_{i}"
        fi = st.number_input(f"f{i + 1}: ", key=key, value=1)
        r.append(fi)
   
    submitted = st.form_submit_button("Calculate NPV")

if submitted:
    st.write(f"##### The net present value is: {npv_var_r_calc(c0, i0, c, r, n):.2f}")