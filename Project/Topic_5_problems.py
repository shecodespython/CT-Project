import streamlit as st

def first_a():
    with st.form('1a'):
        col1, col2 = st.columns(2)
        with col1:
            title1 = st.number_input('Number of shares: ', value=1)
            
        with col2:
            title2 = st.number_input('Price of a share: ', value=1)
            market_value = title1*title2

        submitted = st.form_submit_button("Calculate")
        
        
    
    if submitted:
        st.write("##### Market value of the company= ", market_value)



def first_b():
    with st.form('1b'):
        col1, col2 = st.columns(2)

        with col1:
            title1 = st.number_input('Operating profits: ', value= 1)

        with col2: 
            title2 = st.number_input('Number of shares : ', value = 1)

        submitted = st.form_submit_button("Calculate")


    if submitted:
        operating_income = float(title1)
        number_of_share = float(title2)
        st.write("##### EPS= ", (operating_income/number_of_share))

    

def first_c():
    with st.form('1c'):
        title1 = st.number_input(' Operating profits : ', value = 1)
        operating_income = float(title1)
        intrest = int(500)
        submitted = st.form_submit_button("Calculate")

    
    if submitted:   
        st.write("##### Intrest = ", intrest)
        st.write("##### Profit (which is dividend can be distributed in the form of = ", (operating_income-intrest))
        st.write("##### EPS = ", ((operating_income-intrest)/intrest))
        st.write("##### Stock return = ", (((operating_income-intrest)/intrest)/10))



def first_d():

    with st.form('1d'):
        title1 = st.number_input('  Operating profits : ', value = 1)
        intrest = int(1)
        operating_income = float(title1)
        submitted = st.form_submit_button("Calculate")


    
    if submitted:
        st.write("##### 2 earnings per share = ", (2*(operating_income/1000)))
        st.write("##### Intrest = ", intrest)
        st.write("##### The investor's income = ", ((2*(operating_income/1000))-intrest))
        st.write("##### The investor's return = ", (((2*(operating_income/1000))-intrest)/intrest))


def second():
    with st.form('2'):
        st.write("Before borrowing: ")

        col1, col2 = st.columns(2)

        with col1:
            re = int(st.number_input('re : ', value = 1))
        
        with col2:
            d = int(st.number_input('D : ', value = 1))

        submitted = st.form_submit_button("Calculate")


    if submitted:
        st.write("##### ra= ", re)

    with st.form('2.2'):
        st.write("After borrowing: ")

        col1, col2 = st.columns(2)

        with col1:
            ra = int(st.number_input('ra : ', value = 1))
            rd = int(st.number_input('rd: ', value = 1))
        
        with col2:
            d = int(st.number_input('D/V: ', value = 1))
        
        submitted = st.form_submit_button("Calculate")


    if submitted:
        st.write("##### E/V= ", (100-d))
        st.write("##### re= ", ((ra/100) + (d/(100-d)) * (ra/100 - rd/100)))


def third():

    with st.form('3'):
        st.write("D = V - E")
        de = float(st.number_input('D/E : ', value = 1))
        submitted = st.form_submit_button("Calculate")
    
    if submitted:
        st.write("##### V/E = ", (1+de))
        st.write("##### E/V = ", (1/(1+de)))
        st.write("##### D/V= ", (1-((1/(1+de)))))


    with st.form('3.2'):
        st.write("\nBefore borrowing: ")

        col1, col2 = st.columns(2)

        with col1:
            re = float(st.number_input('re  : ', value = 1))
        
        with col2:
            rd = float(st.number_input('rd  : ', value = 1))
        
        submitted = st.form_submit_button("Calculate")

    if submitted:
        st.write("##### WACC = ", ((re*(1/(1+de))) + (rd*(1-((1/(1+de)))))))


    with st.form('3.3'):
        st.write("\nAfter borrowing: ")

        col1, col2 = st.columns(2)

        with col1:
            ra = float(st.number_input('ra  : ', value = 1))
        
        with col2:
            de2 = float(st.number_input('D/E  : ', value = 1))
        submitted = st.form_submit_button("Calculate")

    if submitted:
        st.write("##### re = ", (ra+de2*(ra-rd)))


def fourth():
    with st.form('4'):
        st.write("Before borrowing: ")

        col1, col2 = st.columns(2)

        with col1:
            e = float(st.number_input('E   : ', value = 1))
            re = float(st.number_input('re   : ', value = 1))
        
        with col2:
            d = float(st.number_input('D   : ', value = 1))
            rd = float(st.number_input('rd   : ', value = 1))

        submitted = st.form_submit_button("Calculate")

    if submitted:
        st.write("##### V = ", (e+d))
        st.write("##### WACC = ", ((re*(e/(e+d)) + (rd*(d/(e+d))))))

    with st.form('4.2'):
        st.write("After borrowing: ")
        col1, col2 = st.columns(2)

        with col1:
            e = float(st.number_input('E    : ', value = 1))
            ra = float(st.number_input('ra   : ', value = 1))
        
        with col2:
            d = float(st.number_input('D    : ', value = 1))

        submitted = st.form_submit_button("Calculate")

    if submitted:
        st.write("##### V = ", (e+d))
        st.write("##### re = ", (ra+(d/e)*(ra-rd)))


