import streamlit as st
import math

def first_a():
    with st.form('1'):
        col1, col2 = st.columns(2)

        with col1:
            price = float(st.number_input("Price of an iron: ", value=1))
            chance = float(st.number_input("The chance to request a payment deferral: ", value=1))
        
        with col2:
            prod_cost = float(st.number_input("An iron production cost: ", value=1))

        submitted = st.form_submit_button("Calculate")

    if submitted:
        st.write("##### Probability adjusted earnings: ", (((100-chance)/100) * (price - prod_cost) * 1000))

        st.write("##### Probability adjusted loss: ", (chance/100) * (-prod_cost) * 1000)

    st.write('\n')
    st.write('\n')


def first_b():
    with st.form('1.2'):
        col1, col2 = st.columns(2)

        with col1:
            chance = float(st.number_input("The chance to request a payment deferral:  ", value=1))
        
        with col2:
            prod_cost = float(st.number_input("An iron production cost:  ", value=1))
    
        submitted = st.form_submit_button("Calculate")

    if submitted:
        st.write("##### X : ", (((chance/100)*prod_cost + ((100-chance)/100)*prod_cost)/((100-chance)/100)))

    st.write('\n')
    st.write('\n')


def first_c():
    with st.form('1.3'):
        col1, col2 = st.columns(2)

        with col1:
            chance = float(st.number_input("The chance to request a payment deferral:   ", value=1))
        
        with col2:
            prod_cost = float(st.number_input("An iron production cost:   ", value=1))

        submitted = st.form_submit_button("Calculate")

    if submitted:
        st.write("##### X : ", (((chance/100)*prod_cost + (100-chance)/100*prod_cost)/((100-chance)/100 -0.05)))

    st.write('\n')
    st.write('\n')

def second():
    with st.form('2'):
        col1, col2 = st.columns(2)

        with col1:
            takeover = int(st.number_input("Company takeover", value=1))
            delay_to = int(st.number_input("Payment delay to", value=1))
        
        with col2:
            delay_from = int(st.number_input("Payment delay from", value=1))
            cost = float(st.number_input("Cost of short-term funds", value=1))

        submitted = st.form_submit_button("Calculate")

    if submitted:
        st.write("##### X = ", ((delay_to * takeover) / delay_from))
        st.write("##### Increase in percentage : ", ((((delay_to * takeover) / delay_from) - takeover)/takeover)*100)

        st.write("##### What additional annual financing costs are incurred by the company if the short-term sources cost 7.5%?")
        st.write("##### Annual financing costs : ", ((((delay_to * takeover) / delay_from) - takeover) * cost)/100)

    st.write('\n')
    st.write('\n')

def third_a():
    with st.form('3'):
        col1, col2 = st.columns(2)

        with col1:
            s = int(st.number_input("s: ", value=1))
            c = float(st.number_input("c: ", value=1))
        
        with col2:
            r = float(st.number_input("r: ", value=1))

        submitted = st.form_submit_button("Calculate")

    if submitted:
        st.write("##### Q: ", math.sqrt((2*c*s/r)))
        st.write("##### N: ", s/math.sqrt((2*c*s/r)))
        st.write("##### Q': ", math.sqrt((2*c*s/r))/2)
        st.write("##### FK: ", (math.sqrt((2*c*s/r))/2)*r)
        st.write("##### RK: ", (s/math.sqrt((2*c*s/r)))*c)
        st.write("##### TK: ", ((math.sqrt((2*c*s/r))/2)*r)+((s/math.sqrt((2*c*s/r)))*c))

    st.write('\n')
    st.write('\n')

def third_b():
    with st.form('3.1'):
        col1, col2 = st.columns(2)

        with col1:
            s = int(st.number_input("s:   ", value=1))
            c = float(st.number_input("c:  ", value=1))
        
        with col2:
            r = float(st.number_input("r:  ", value=1))
            n = float(st.number_input("N:   ", value=1))
        
        submitted = st.form_submit_button("Calculate")

    if submitted:
        st.write("Q: ", s/n)
        st.write("Q': ", (s/n)/2)
        st.write("FK: ", ((s/n)/2)*r)
        st.write("RK: ", n*c)
        st.write("TK: ", (((s/n)/2)*r)+(n*c))

    st.write('\n')
    st.write('\n')


def fourth():
    with st.form('3.2'):
        col1, col2 = st.columns(2)

        with col1:
            cost = float(st.number_input("Annual order cost: ", value=1))
            c = float(st.number_input("c:   ", value=1))
        
        with col2:
            book_price = float(st.number_input("Book price: ", value=1))
            interest_rate = float(st.number_input("Interest rate: ", value=1))

        submitted = st.form_submit_button("Calculate")

    if submitted:
        st.write("S: ", cost/book_price)
        st.write("r: ", book_price * (interest_rate/100))
        st.write("Q: ", math.sqrt((2*c*(cost/book_price))/(book_price*(interest_rate/100))))
        st.write("N: ", (cost/book_price)/ math.sqrt((2*c*(cost/book_price))/(book_price*(interest_rate/100))))
        st.write("FK: ", (((math.sqrt((2*c*(cost/book_price))/(book_price*(interest_rate/100))))/2)*(book_price*(interest_rate/100))))
        st.write("RK: ", ((cost/book_price)/ math.sqrt((2*c*(cost/book_price))/(book_price*(interest_rate/100))))*c)
        st.write("TK: ", (((math.sqrt((2*c*(cost/book_price))/(book_price*(interest_rate/100))))/2)*(book_price*(interest_rate/100)))+(((cost/book_price)/ math.sqrt((2*c*(cost/book_price))/(book_price*(interest_rate/100))))*c))
     
    st.write('\n')
    st.write('\n')