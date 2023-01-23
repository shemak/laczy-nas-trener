import streamlit as st

from laczy_nas_trener import images_helpers

image_base_log = images_helpers.image_to_base64('images/logo.jpg', logo_resize=True)
images_helpers.add_logo(image_base_log)

image_base_paulo = images_helpers.image_to_base64('images/paulo.jpg')
#st.markdown(f'<div style="text-align: center;"> <img src="data:image/jpg;base64,{image_base_paulo}" width="150" height="275"> </div>',
#            unsafe_allow_html=True)
st.image('images/paulo.jpg', width=250)

st.markdown('''Strona powstała wyłacznie w celach rozrywkowych, i nie ma na celu urażania uczuć innych osób.
    \nLogo 'Męczy nas piłka' oraz ikony były trenerów to popularne w sieci grafiki pariodujące hasło 'Lączy nas piłka' (autor nieznany?).
    \nObrazek na górze strony pochodzi z serwisu Wykop.pl, z tagu #reprezentacja (autor nieznany?).
    \nGrafiki z wybranymi trenerami są oczywiście fikcyjne, część z nich pochodzi z profilu @PanieKazimierzu na portalu Twitter.com, dla
        części z nich autor jest nieznany, natomiast większość z nich została stworzona przeze autora strony.
''')