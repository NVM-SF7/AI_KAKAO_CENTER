import components.subcomponents.Logo as Img
from components.subcomponents.Logo import *
import streamlit as st
import streamlit as st
def Header() :
    # gema, pkn = st.columns(2, vertical_alignment="center",)
    # with gema:
    #     Img.image(["./gema.png"])
    # with pkn:
    #     Img.image("./pkn.png")
    Img.image(["./Image/gema.png", "./Image/pkn.png"])
    
    st.title("KAKAO AI CENTER")
    st.write("Welcome to the Cacao Help Center! How can we assist you today?")