import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
from gtts import gTTS
# To install this module, run:
# python -m pip install Pillow
from io import BytesIO
from PIL import Image
from PIL import ImageDraw
import json
import streamlit as st
import tensorflow as tf
from keras.models import load_model
from keras.utils import load_img
from keras.utils import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
import numpy as np
from keras.models import load_model
from cv_zone import main

st.set_page_config(layout="wide")
#st.sidebar.image('images/Azure_Image.png', width=300)
st.sidebar.header('A website for classifying Indian Sign Language')
st.sidebar.markdown('Used CNN algorithm')


app_mode = st.sidebar.radio(
    "",
    ("About Me","camera input"),
)


st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.markdown('---')
st.sidebar.write('N.V.Suresh Krishna | sureshkrishnanv24@gmail.com https://github.com/sureshkrishna123')

if app_mode =='About Me':
    #st.image('images/wp4498220.jpg', use_column_width=True)
    st.markdown('''
              # About Me \n 
                Hey this is ** N.V.Suresh Krishna **. \n
                
                
                Also check me out on Social Media
                - [git-Hub](https://github.com/sureshkrishna123)
                - [LinkedIn](https://www.linkedin.com/in/suresh-krishna-nv/)
                - [Instagram](https://www.instagram.com/worldofsuresh._/)
                - [Portfolio](https://sureshkrishna123.github.io/sureshportfolio/)
                - [Blog](https://ingenious-point.blogspot.com/)\n
                If you are interested in building more about Microsoft Azure then   [click here](https://azure.microsoft.com/en-in/)\n
                ''')
              
     


if app_mode=='camera input':
      
      image_file = st.camera_input("Take a picture")
      if image_file:
        img = Image.open(image_file)
        st.image(image_file,width=250,caption='Uploaded image')
        

      button_translate=st.button('Click me',help='To give the image')
  
  
      if (button_translate and image_file):
        st.image(main(img))
        
        st.text("The hand sign of the above image is : ")

    #word=class_names[np.argmax(score)]
    #sound_file = BytesIO()
    #tts = gTTS(word)
    #tts.write_to_fp(sound_file)
    #st.audio(sound_file)
