#주요 라이브러리
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import tensorflow as tf

import streamlit as st
from streamlit_option_menu import option_menu
#tensorflow 2.15 버전으로 설치할 것(2.16 X)  -->  Tip: 구글 코랩으로 돌렸을 때는 해당 환경이 2.15버전이었기 때문임 : 최신 버전이 반드시 좋은것은 아님
#실무에서는 버전 호환이 안 되어서 멀쩡한 명령어가 동작을 안 할 수도 있음 : 주의할 것
from keras.models import load_model
from PIL import Image, ImageOps

from util import main_title
from cont1_HOME import run_home
from cont2_INTRO import run_intro
from cont3_ML import run_ml
from cont4_CS import run_cs
from cont5_ETC import run_etc





def main():
    #메뉴 사이드바
    with st.sidebar:
        option_menu_list = ['HOME', 'INTRODUCTION', 'MACHINE LEARNING', 'CUSTROMER SERVICE', 'ETC']
        choose = option_menu("WELCOME!", option_menu_list,
                            icons=['house', 'camera fill', 'kanban', 'bi bi-wechat', 'bi bi-three-dots-vertical'],
                            menu_icon="bi bi-emoji-smile", default_index=0,
                            styles={
            "container": {"padding": "5!important", "background-color": "#000000"},
            "icon": {"color": "orange", "font-size": "15px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }
        )

    if choose == option_menu_list[0]:
        run_home()
    elif choose == option_menu_list[1]:
        run_intro()
    elif choose == option_menu_list[2]:
        run_ml()
    elif choose == option_menu_list[3]:
        run_cs()
    else :
        run_etc()





if __name__ == '__main__':
    main()


