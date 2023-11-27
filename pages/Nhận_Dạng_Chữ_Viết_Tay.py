from tkinter import Canvas
import streamlit as st
#import lib.common as tools

st.set_page_config(
    page_title="Đồ án cuối kỳ",
    page_icon="✏",
)

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://marketplace.canva.com/EAD2962NKnQ/2/0/1600w/canva-rainbow-gradient-pink-and-purple-virtual-background-_Tcjok-d9b4.jpg");
    background-size: 100% 100%;
}
[data-testid="stHeader"]{
    background: rgba(0,0,0,0);
}
[data-testid="stToolbar"]{
    right:2rem;
}
[data-testid="stSidebar"] > div:first-child {
    background-image: url("https://images.pexels.com/photos/7130534/pexels-photo-7130534.jpeg?cs=srgb&dl=pexels-codioful-%28formerly-gradienta%29-7130534.jpg&fm=jpg");
    background-position: center;
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)


from streamlit_drawable_canvas import st_canvas
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import numpy as np

# Read image
#image = st._main.file_uploader("Upload Your Image", type=['jpg', 'png', 'jpeg', 'tif'])

def draw():
    # Create a canvas component
    canvas_result = st_canvas(
        fill_color='#FF000000',
        stroke_width=20,
        stroke_color='#FFFFFF',
        background_color= '000000',
        width=300,
        height=300,
        drawing_mode="freedraw",
        key="canvas",

    )

    # Predict
    if canvas_result.image_data is not None:
        img = canvas_result.image_data.astype(np.uint8)
        img = cv2.resize(img, (28, 28))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = np.array(img, dtype=np.uint8)
        st.image(img)
        model = tf.keras.models.load_model('./HandWriteDetection/char.keras')
        predict = model.predict(img.reshape(1,28,28,1))
        st.write('## Giá trị dự đoán: ', np.argmax(predict))

draw()
