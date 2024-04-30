#주요 라이브러리
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import tensorflow as tf

import streamlit as st
from streamlit import columns
from streamlit_option_menu import option_menu
#tensorflow 2.15 버전으로 설치할 것(2.16 X)  -->  Tip: 구글 코랩으로 돌렸을 때는 해당 환경이 2.15버전이었기 때문임 : 최신 버전이 반드시 좋은것은 아님
#실무에서는 버전 호환이 안 되어서 멀쩡한 명령어가 동작을 안 할 수도 있음 : 주의할 것
from keras.models import load_model
from PIL import Image, ImageOps


from util import main_title


empty1, col1, empty2 = st.columns([0.5, 1.0, 0.5])
empty3, col2, empty4 = st.columns([0.5, 1.0, 0.5])
empty5, col3, empty6 = st.columns([0.5, 1.0, 0.5])
empty7, col4, empty8 = st.columns([0.5, 1.0, 0.5])



def run_ml():
    #메인 컨텐츠
    #1. 이미지 파일을 업로드하면

    with col1:
        st.title('11종 음식 이미지 예측분류')
        st.subheader('이미지 파일을 업로드하면 음식을 예측합니다')

    with col2:
        st.markdown('<br><br>', unsafe_allow_html=True)
        user_file = st.file_uploader('하단 기능바에 원하시는 이미지 파일을 업로드하세요.', type=['jpg', 'jpeg', 'png', 'webp', 'svg'])

    with col3:
        if user_file is not None:
            st.image(user_file)
            st.subheader('사용자께서 선택하신 이미지입니다.')
        else:
            pass


    with col4:
        if user_file is not None:
            sel_pred = st.button(label='분류하기')
            if sel_pred :
                #2. 11개의 음식 중에서 예측하도록 한다
                # Disable scientific notation for clarity
                np.set_printoptions(suppress=True)

                # Load the model
                model = load_model('./ai_model/keras_model.h5', compile=False)

                # Load the labels
                class_names = open('./ai_model/labels.txt', "r", encoding='utf-8').readlines()

                # Create the array of the right shape to feed into the keras model
                # The 'length' or number of images you can put into the array is
                # determined by the first position in the shape tuple, in this case 1
                data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

                # Replace this with the path to your image
                image = Image.open(user_file).convert("RGB")

                # resizing the image to be at least 224x224 and then cropping from the center
                size = (224, 224)
                image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

                # turn the image into a numpy array
                image_array = np.asarray(image)

                # Normalize the image
                normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

                # Load the image into the array
                data[0] = normalized_image_array

                # Predicts the model
                prediction = model.predict(data)
                index = np.argmax(prediction)
                class_name = class_names[index]
                confidence_score = prediction[0][index]

                # Print prediction and confidence score
                print("Class:", class_name[2:], end="")
                print("Confidence Score:", confidence_score)


                #분류 결과를 유저한테 보여주기
                st.info(f'이 음식 이미지는 {class_name[2:]}입니다.\n 본 예측의 정확도는 {round(confidence_score*100, ndigits=0)}%입니다.')
                #st.info(f'본 예측의 정확도는 {round(confidence_score*100, ndigits=0)}%입니다.')
            
            else:
                pass


