import streamlit as st

def first_a():
    col1, col2 = st.columns(2)
    with col1:
        title1 = st.text_input('Number of shares: ', '0')
        
    with col2:
        title2 = st.text_input('Price of a share: ', '0')
        
    if title1 == '' or title2 == '':
        st.write("")
    else:
            share_number = float(title1)
            share_price = float(title2)
            st.write("Market value of the company= ", (share_number*share_price))

    '''
   with st.form(""):
        share_number  = st.number_input("Number of shares:")
        share_price = st.number_input("Price of a share: ")
        submitted = st.form_submit_button("Calculate")
    
        if submitted:
            st.write("Market value of the company= ", (share_number*share_price))
            '''



def first_b():
    col1, col2 = st.columns(2)

    with col1:
        title1 = st.text_input('Operating profits: ', '0')

    with col2: 
        title2 = st.text_input('Number of shares : ', '0')

    if title1 == '' or title2 == '' or title2 == '0':
        st.write("")
    else:
        operating_income = float(title1)
        number_of_share = float(title2)
        st.write("EPS= ", (operating_income/number_of_share))

    

def first_c():

    title1 = st.text_input(' Operating profits : ', '0')
    operating_income = float(title1)
    intrest = int(500)
    
    if title1 == '0':
        st.write('')
    else:
        st.write("Intrest = ", intrest)
        st.write("Profit (which is dividend can be distributed in the form of = ", (operating_income-intrest))
        st.write("EPS = ", ((operating_income-intrest)/intrest))
        st.write("Stock return = ", (((operating_income-intrest)/intrest)/10))

def first_d():
    title1 = st.text_input('  Operating profits : ', '0')
    intrest = int(1)
    operating_income = float(title1)

    
    if title1 == '0':
        st.write('')
    else:
        st.write("2 earnings per share = ", (2*(operating_income/1000)))
        st.write("Intrest = ", intrest)
        st.write("The investor's income = ", ((2*(operating_income/1000))-intrest))
        st.write("The investor's return = ", (((2*(operating_income/1000))-intrest)/intrest))


def second():
    st.write("Before borrowing: ")
    re = int(st.text_input('re : ', '0'))
    d = int(st.text_input('D : ', '0'))

    if re == '' or d == '':
        st.write("")
    else:
        st.write("ra= ", re)


    st.write("After borrowing: ")
    ra = int(st.text_input('ra : ', '0'))
    d = int(st.text_input('D/V: ', '0'))
    rd = int(st.text_input('rd: ', '0'))

    if ra == '' or d == '' or rd == '':
        st.write("")
    else:
        st.write("E/V= ", (100-d))
        st.write("re= ", ((ra/100) + (d/(100-d)) * (ra/100 - rd/100)))


def third():
    st.write("D = V - E")
    de = float(st.text_input('D/E : ', '0'))
    st.write("V/E = ", (1+de))
    st.write("E/V = ", (1/(1+de)))
    st.write("D/V= ", (1-((1/(1+de)))))

    st.write("\nBefore borrowing: ")
    re = float(st.text_input('re  : ', '0'))
    rd = float(st.text_input('rd  : ', '0'))
    st.write("WACC = ", ((re*(1/(1+de))) + (rd*(1-((1/(1+de)))))))

    st.write("\nAfter borrowing: ")
    ra = float(st.text_input('ra  : ', '0'))
    de2 = float(st.text_input('D/E  : ', '0'))
    st.write("re = ", (ra+de2*(ra-rd)))


def fifth():
    st.write("Before borrowing: ")
    e = float(st.text_input('E   : ', '0'))
    d = float(st.text_input('D   : ', '0'))
    re = float(st.text_input('re   : ', '0'))
    rd = float(st.text_input('rd   : ', '0'))

    if e == 0 or d ==0:
        st.write("")
    else:
        st.write("V = ", (e+d))
        st.write("WACC = ", ((re*(e/(e+d)) + (rd*(d/(e+d))))))


    st.write("After borrowing: ")
    e = float(st.text_input('E    : ', '0'))
    d = float(st.text_input('D    : ', '0'))
    ra = float(st.text_input('ra   : ', '0'))

    if e == 0 or d == 0:
        st.write("")
    else:
        st.write("V = ", (e+d))
        st.write("re = ", (ra+(d/e)*(ra-rd)))


