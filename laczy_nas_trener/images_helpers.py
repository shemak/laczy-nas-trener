import base64
from io import BytesIO
from PIL import Image
import streamlit as st

def image_to_base64(img_path: str, logo_resize: bool = False) -> str:
    """
    Helper function returning base64 object stored as string,
        that can be displayed within the application.
    """
    if logo_resize:
        img = Image.open(img_path).resize((250, 250))
    else:
        img = Image.open(img_path)
    with BytesIO() as buffer:
        img.save(buffer, "png")  # or 'jpeg'

        return base64.b64encode(buffer.getvalue()).decode()

def add_logo(image_base_64):
    return st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(data:image/jpg;base64,%s);
                background-repeat: no-repeat;
                padding-top: 200px;
                background-position: 20px 20px;
            }
        </style>
        """ % image_base_64,
        unsafe_allow_html=True,
    )