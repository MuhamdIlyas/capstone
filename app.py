# -*- coding: utf-8 -*-

"""**Import Library**
"""

#melakukan import library
import streamlit as st
import numpy as np
import pandas as pd
import pickle
from PIL import Image

pickle_in = open('app.pkl', 'rb')
classifier = pickle.load(pickle_in)

def welcome():
  return 'Selamat Datang'

def prediction(ph1, Hardness1, Solids1, Chloramines1, Sulfate1):
  ph = [0,0,0,0]
  Hardness = [0,0,0,0]
  Solids = [0,0,0,0,0]
  Chloramines = [0,0,0]
  Sulfate = [0,0,0,0]
  if Sulfate1>=100 and Sulfate1<250:
    Sulfate[0]=1
  elif Sulfate1>=250 and Sulfate1<400:
    Sulfate[1]=1
  elif Sulfate1>=400:
    Sulfate[2]=1
  else:
    Sulfate[3]=1
  
  if Chloramines1>=1 and Chloramines1<5:
    Chloramines[0]=1
  elif Chloramines1>=5:
    Chloramines[2]=1
  else:
    Chloramines[3]=1

<<<<<<< HEAD
  if Solids1>=100 and Solids1<600:
    Solids[0]=1
  if Solids1>=600 and Solids1<1000:
    Solids[1]=1
  if Solids1<=1000 and Solids1<1200:
    Solids[2]=1
  if Solids1<=1200:
    Solids[3]=1
  else:
    Solids[4]=1

  if Hardness1>=0 and Hardness1<50:
    Hardness[0]=1
  elif Hardness1>=50 and Hardness1<250:
    Hardness[1]=1
  elif Hardness1>=250:
    Hardness[2]=1
  else:
    Hardness[3]=1

  if ph1>=0 and ph1<6.5:
=======
def prediction(ph1):
  ph = [0,0,0,0,0,0,0,0,0,0,0,0,0]
  if ph1>=0 and ph<1:
>>>>>>> cd48d2cea0a3d50092a56a8e805a1286d56104e0
    ph[0]=1
  elif ph1>=6.5 and ph1<8.5:
    ph[1]=1
  elif ph1>=8.5:
    ph[2]=1
<<<<<<< HEAD
  else:
    ph[3]=1
=======
  elif ph1>=3 and ph<4:
    ph[3]=1
  elif ph1>=4 and ph<5:
    ph[4]=1
  elif ph1>=5 and ph<6:
    ph[5]=1
  elif ph1>=6 and ph<8:
    ph[6]=1
  elif ph1>=8 and ph<9:
    ph[7]=1
  elif ph1>=9 and ph<10:
    ph[8]=1
  elif ph1>=10 and ph<11:
    ph[9]=1
  elif ph>=11 and ph<12:
    ph[10]=1
  elif ph1>=12 and ph<13:
    ph[11]=1
  elif ph1>=13 and ph<14:
    ph[12]=1
  else:
    ph[13]=1
>>>>>>> cd48d2cea0a3d50092a56a8e805a1286d56104e0


  prediction = classifier.predict(
    [[ph[0],ph[1],ph[2],ph[3],Hardness[0],Hardness[1],Hardness[2],Hardness[3],Solids[0],Solids[1],Solids[2],Solids[3],Solids[4],Chloramines[0],Chloramines[1],Chloramines[2],Sulfate[0],Sulfate[1],Sulfate[2],Sulfate[3]]])
  
  return prediction

def result(zat1):
  zat = [0,0,0,0,0,0,0,0,0,0,0,0,0]
  if zat1=="Asam Sulfat":
    zat[0]=1
  elif zat1=="Asam Sitrat":
    zat[1]=1
  elif zat1=="Asam Askarbonat":
    zat[2]=1
  elif zat1=="Asam Nitrat":
    zat[3]=1
  elif zat1=="Asam Chlorogenic":
    zat[4]=1
  elif zat1=="Asam Amino":
    zat[5]=1
  elif zat1=="Air Netral":
    zat[6]=1
  elif zat1=="Natrium Bikarbonat":
    zat[7]=1
  elif zat1=="Alkali":
    zat[8]=1
  elif zat1=="Amonia":
    zat[9]=1
  elif zat1=="Natrium":
    zat[10]=1
  elif zat1=="Natrium Hipoklorit":
    zat[11]=1
  elif zat1=="Natrium Hidroksida":
    zat[12]=1
  else:
    zat[13]=1
  
  return result

def main():
  st.title("Prediksi Air")
  html_temp=""
  ans=0
  st.markdown(html_temp,unsafe_allow_html=True)
<<<<<<< HEAD
  get_ph = st.slider("PH Air ?", min_value=1,max_value=14, value=1)
  get_Hardness = st.slider("Kesahadan Air ?",min_value=1,max_value=400, value=1)
  get_Sulfate = st.slider("Kegunaan Sulfat ?", min_value=100,max_value=500, value=100)
  get_Chloramines = st.slider("Kandungan Klorin ?", min_value=1,max_value=15, value=1)
  get_Solids = st.slider("Kandungan Solids/TDS ?", min_value=100,max_value=3000, value=100)

  if st.button("Predict"):
    ans=prediction(get_ph,get_Hardness,get_Solids,get_Chloramines,get_Sulfate)[0]
    if ans==0:
      st.success('Air Tidak Tercemar 😊')
      st.image('img/airsehat.jpg')
    else:
      st.success('Air Tercemar 😥')
      st.image('img/tercemar.jpg')
=======
  get_ph = st.slider("Water PH ?", min_value=1,max_value=14, value=25)

  if st.button("Predict"):
    ans=prediction(get_ph)[0]
    if ans==0:
      st.success('Air Sehat')
    else:
      st.success('Air Berpolusi')
>>>>>>> cd48d2cea0a3d50092a56a8e805a1286d56104e0

if __name__=='__main__':
  main()