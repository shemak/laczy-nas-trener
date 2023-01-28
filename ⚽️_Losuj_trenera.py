import random
import streamlit as st
from streamlit_player import st_player

from laczy_nas_trener import coaches, images_helpers

st.set_page_config(
    layout="wide",
    page_icon="⚽️",
    page_title="Lączy nas trener - generator",
    initial_sidebar_state="expanded",
)
#sidebar
image_base_log = images_helpers.image_to_base64('images/logo.jpg', logo_resize=True)
images_helpers.add_logo(image_base_log)

st.image('images/top_reprezentacja.jpg')

st.markdown("<h2 style='text-align: center; color: white;'>Łączy nas trener</h2>", unsafe_allow_html=True)    
st.write('\n')

col1, col2, col3 = st.columns([2,1,2])
with col1:
    image_base_jerry = images_helpers.image_to_base64('images/top_coaches/jerzy_brzecz.jpg')
    st.markdown(f'<img src="data:image/jpg;base64,{image_base_jerry}" width="100" height="100" style="float:right">',
                unsafe_allow_html=True)
with col2:
    coach_sel = st.button('⚽️ Naciśnij aby wybrać trenera! ⚽️')
with col3:
    image_base_czes = images_helpers.image_to_base64('images/top_coaches/czes_mich.jpg')
    st.markdown(f'<img src="data:image/jpg;base64,{image_base_czes}" width="100" height="100" style="float:left">',
                unsafe_allow_html=True)

if coach_sel:
    st.balloons()
    coach = random.choice(list(coaches.coach_to_image.keys()))
    st.markdown('<div style="text-align: center;">Trenerem naszych orłów zostaje:</div>', unsafe_allow_html=True)    
    st.markdown(f"<h2 style='text-align: center; color: white;'>{coach}!</h2>", unsafe_allow_html=True)       
    image_base_selected_coach = images_helpers.image_to_base64(coaches.coach_to_image[coach])
    st.markdown(f'<div style="text-align: center;"> <img src="data:image/jpg;base64,{image_base_selected_coach}" width="350" height="450"> </div>',
                unsafe_allow_html=True)

st.write('\n')
with st.expander('Co warto usłyszeć w momencie wyboru nowego trenera reprezentacji Polski?'):
    st.write('''Myślę, że w tej sytuacji warto będzie przypomnieć zwycięski skład Kaiserslautern z meczu z Bayernem w sezonie 97/98: Reinke, Kadlec, H. Koch (31. Hristov), Kuka, Marschall, Ratinho (75. Reich), Roos, Schjönberg, Schäfer, Sforza, M. Wagner.''')
    st_player("https://youtu.be/qALCXfZyViw", playing=True, controls=True)
st.write('\n')
with st.expander('Czego na pewno nie usłyszymy w przyszłym roku?'):
    st_player("https://youtu.be/h5AHfXbw4ls?t=395", playing=True, controls=True)
