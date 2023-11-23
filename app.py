import streamlit as st
import myModel

st.title("Restaurant Helper")

cusine = st.sidebar.selectbox('Pick a Cuisine', ('Indian', 'Italian', 'Mexican', 'Chinese', 'Arabic', 'American', 'Continental'))

if cusine:
    response = myModel.resturant(cusine)
    st.header(response['restaurant_name'].strip())
    menu = response['menu'].strip().split(',')
    st.write("**--Menu--**")
    for item in menu:
        st.write("-",item)