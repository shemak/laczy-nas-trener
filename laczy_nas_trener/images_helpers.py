import base64
from io import BytesIO
from PIL import Image

def image_to_base64(img_path: str) -> str:
    """
    Helper function returning base64 object stored as string,
        that can be displayed within the application.
    """
    img = Image.open(img_path)
    with BytesIO() as buffer:
        img.save(buffer, "png")  # or 'jpeg'

        return base64.b64encode(buffer.getvalue()).decode()