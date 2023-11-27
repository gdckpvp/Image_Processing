import streamlit as st
#import lib.common as tools

st.set_page_config(
    page_title="Đồ án cuối kỳ",
    page_icon="📷",
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


# logo_path = "./VCT.png"
# st.sidebar.image(logo_path, width=200)



st.markdown(
    """
    # Đồ án cuối kỳ 📖
    ## Sản phẩm
    ### Project cuối kỳ cho môn học xử lý ảnh số DIPR430685.
    ### Thuộc Trường Đại Học Sư Phạm Kỹ Thuật TP.HCM.
    ## Các chức năng chính trong bài
    ### Giải phương trình bậc 2
    ### Nhận dạng chữ viết tay
    ### Nhận dạng đối tượng
    ### Nhận diện khuôn mặt
    ### Phát hiện khuôn mặt
    ### Xử lý ảnh số (Bao gồm 4 chương: 3, 4, 5, 9)    
    """
)
st.write("## Sinh viên thực hiện")
st.write("### 20133122 - Đỗ Hoàng Thịnh")
st.write("### Mã lớp : DIPR430685_23_1_01")

