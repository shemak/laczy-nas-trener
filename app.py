import streamlit as st

with st.sidebar:
    st.image('images/logo.jpg')


col1, col2, col3 = st.columns(3)

with col1:
    st.image('images/top_coaches/jerry_buzzer.jpg')

with col2:
    coachsel = st.button('⚽️ Naciśniej aby wybrać trenera! ⚽️')

with col3:
    st.image('images/top_coaches/czes_mich.jpg')