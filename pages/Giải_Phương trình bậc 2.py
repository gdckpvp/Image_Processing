import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Phát hiện khuôn mặt", page_icon="🧮")


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
st.markdown("# Phương trình bậc 2")


# Giai phuong trinh bac 2

a = st.number_input("Nhập a", value=1.0)
b = st.number_input("Nhập b", value=1.0)
c = st.number_input("Nhập c", value=1.0)

if st.button("Giải"):
    if a == 0:
        if b == 0:
            if c == 0:
                st.write("Phương trình vô số nghiệm")
            else:
                st.write("Phương trình vô nghiệm")
        else:
            x = -c / b
            st.write("Phương trình có nghiệm duy nhất: x = ", x)
    else:
        delta = b * b - 4 * a * c
        if delta < 0:
            st.write("Phương trình vô nghiệm")
        elif delta == 0:
            x = -b / (2 * a)
            st.write("Phương trình có nghiệm kép: x = ", x)
        else:
            x1 = (-b + np.sqrt(delta)) / (2 * a)
            x2 = (-b - np.sqrt(delta)) / (2 * a)
            st.write("Phương trình có 2 nghiệm phân biệt: x1 = ", x1, " và x2 = ", x2)


st.button("Re-run")

