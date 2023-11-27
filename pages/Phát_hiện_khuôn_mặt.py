import streamlit as st
import time
import numpy as np
import cv2 as cv
import object_detection as od
import FaceDetection.Haarcascade.app as ha
import FaceDetection.Facebook.face_detect as fb
from PIL import Image

st.set_page_config(page_title="Phát hiện khuôn mặt", page_icon="👨‍👩‍👧‍👦")

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
st.markdown("# Phát hiện khuôn mặt")


selected = st.sidebar.radio("Options", ["Facebook", "Haarcascade"])

if selected == "Facebook":
    fb.main_loop()
elif selected== "Haarcascade":
    ha.main_loop()


st.button("Re-run")

