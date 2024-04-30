import streamlit as st
from util import main_title
from streamlit.components.v1 import html


st.set_page_config(layout="wide")
empty1,col1,empty2 = st.columns([0.3, 1.0, 0.3])

def run_home():
    st.markdown(main_title, unsafe_allow_html=True)
    st.image('./resources/home_image.png')


