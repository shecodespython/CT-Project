import streamlit as st
import math

def first_a():
    price = float(st.text_input("Price of an iron: ", '0'))
    prod_cost = float(st.text_input("An iron production cost: ", '0'))
    chance = float(st.text_input("The chance to request a payment deferral: ", '0'))

    st.write("Probability adjusted earnings: ", (((100-chance)/100) * (price - prod_cost) * 1000))

    st.write("Probability adjusted loss: ", (chance/100) * (-prod_cost) * 1000)


def first_b():
    chance = float(st.text_input("The chance to request a payment deferral:  ", '0'))
    prod_cost = float(st.text_input("An iron production cost:  ", '0'))
    st.write("X : ", (((chance/100)*prod_cost + ((100-chance)/100)*prod_cost)/((100-chance)/100)))


def first_c():
    chance = float(st.text_input("The chance to request a payment deferral:   ", '0'))
    prod_cost = float(st.text_input("An iron production cost:   ", '0'))
    st.write("X : ", (((chance/100)*prod_cost + (100-chance)/100*prod_cost)/((100-chance)/100 -0.05)))


def second():
    takeover = int(st.text_input("Company takeover", '0'))
    delay_from = int(st.text_input("Payment delay from", '0'))
    delay_to = int(st.text_input("Payment delay to", '0'))
    cost = float(st.text_input("Cost of short-term funds", '0'))

    if takeover == 0 or delay_from == 0 or delay_to == 0 :
        st.write("")
    else:
        st.write("X = ", ((delay_to * takeover) / delay_from))
        st.write("Increase in percentage : ", ((((delay_to * takeover) / delay_from) - takeover)/takeover)*100)

        st.write("What additional annual financing costs are incurred by the company if the short-term sources cost 7.5%?")
        st.write("Annual financing costs : ", ((((delay_to * takeover) / delay_from) - takeover) * cost)/100)


def third_a():
    s = int(st.text_input("s: ", '0'))
    r = float(st.text_input("r: ", '0'))
    c = float(st.text_input("c: ", '0'))

    if s == 0 or r == 0 or c == 0:
        st.write("")
    else:
        st.write("Q: ", math.sqrt((2*c*s/r)))
        st.write("N: ", s/math.sqrt((2*c*s/r)))
        st.write("Q': ", math.sqrt((2*c*s/r))/2)
        st.write("FK: ", (math.sqrt((2*c*s/r))/2)*r)
        st.write("RK: ", (s/math.sqrt((2*c*s/r)))*c)
        st.write("TK: ", ((math.sqrt((2*c*s/r))/2)*r)+((s/math.sqrt((2*c*s/r)))*c))


def third_b():
    s = int(st.text_input("s:   ", '0'))
    r = float(st.text_input("r:  ", '0'))
    c = float(st.text_input("c:  ", '0'))
    n = float(st.text_input("N:   ", '0'))

    if s == 0 or r == 0 or c == 0 or n == 0:
        st.write("")
    else:
        st.write("Q: ", s/n)
        st.write("Q': ", (s/n)/2)
        st.write("FK: ", ((s/n)/2)*r)
        st.write("RK: ", n*c)
        st.write("TK: ", (((s/n)/2)*r)+(n*c))

def fourth():
    cost = float(st.text_input("Annual order cost: ", '0'))
    book_price = float(st.text_input("Book price: ", '0'))
    c = float(st.text_input("c:   ", '0'))
    interest_rate = float(st.text_input("Interest rate: ", '0'))


    if cost == 0 or book_price == 0 or c == 0:
        st.write("")
    else:
        st.write("S: ", cost/book_price)
        st.write("r: ", book_price * (interest_rate/100))
        st.write("Q: ", math.sqrt((2*c*(cost/book_price))/(book_price*(interest_rate/100))))
        st.write("N: ", (cost/book_price)/ math.sqrt((2*c*(cost/book_price))/(book_price*(interest_rate/100))))
        st.write("FK: ", (((math.sqrt((2*c*(cost/book_price))/(book_price*(interest_rate/100))))/2)*(book_price*(interest_rate/100))))
        st.write("RK: ", ((cost/book_price)/ math.sqrt((2*c*(cost/book_price))/(book_price*(interest_rate/100))))*c)
        st.write("TK: ", (((math.sqrt((2*c*(cost/book_price))/(book_price*(interest_rate/100))))/2)*(book_price*(interest_rate/100)))+(((cost/book_price)/ math.sqrt((2*c*(cost/book_price))/(book_price*(interest_rate/100))))*c))
     