# -*- coding: utf-8 -*-
"""Capstone(Streamlit.io).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wRJOyfT29QxeydQDeCOuvIfvW2FyBTs_

## **Data Understanding**

**Import Library**
"""
#melakukan import library
import streamlit as st
import numpy as np
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import plotly.express as ex
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import ShuffleSplit
from sklearn import preprocessing
from sklearn.pipeline import make_pipeline
from sklearn import svm
from sklearn.model_selection import cross_val_score
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
import tensorflow as tf

"""**Meload dataste dari github**"""

# load dataset
url = 'https://raw.githubusercontent.com/muhamadilyas17/capstone/main/water_potability.csv'
kualitas_air = pd.read_csv(url)
kualitas_air

"""**Cek Tipe Data**"""

#mengecek dataset
kualitas_air.info()

"""**Describe Data**"""

#mendeskripsikann data
kualitas_air.describe()

"""## **Data Preparation**

**Mengatasi Missing Value**
"""

#cek missing value
kualitas_air.isnull().sum()

"""**Mengisi Nilai Null dan Merawat Nilai yang hilang**

Kekerasan merupakan salah satu faktor yang mempengaruhi pH air. Para ilmuwan mengukur kekerasan air menggunakan skala pH, yang mengukur konsentrasi ion hidrogen dalam cairan. Air dengan pH rendah lebih bersifat asam, sedangkan air dengan pH lebih tinggi lebih keras atau lebih basa, artinya mampu menetralkan asam. pH air menentukan kelayakan air.
"""

x = kualitas_air[(kualitas_air['Potability']==0) & (kualitas_air['Hardness']<=150)][['ph']].mean()
x

y = kualitas_air[(kualitas_air['Potability']==0) & (kualitas_air['Hardness']>150)][['ph']].mean()
y

z = kualitas_air[(kualitas_air['Potability']==1) & (kualitas_air['Hardness']<=150)][['ph']].mean()
z

o = kualitas_air[(kualitas_air['Potability']==1) & (kualitas_air['Hardness']>150)][['ph']].mean()
o

#mengisi nilai null
for i in range (0,len(kualitas_air)):
    if (pd.isnull(kualitas_air['ph'][i]) == True):
        if ((kualitas_air['Potability'][i]==0) & (kualitas_air['Hardness'][i]<=150)):
            kualitas_air['ph'][i] = x
        elif ((kualitas_air['Potability'][i]==0) & (kualitas_air['Hardness'][i]>150)):
            kualitas_air['ph'][i] = y
        elif ((kualitas_air['Potability'][i]==1) & (kualitas_air['Hardness'][i]<=150)):
             kualitas_air['ph'][i] = z
        else:
             kualitas_air['ph'][i] = o

"""Kehadiran sulfat dalam air minum salah satu faktor penting untuk menentukan kelayakan air"""

x = kualitas_air[(kualitas_air['Potability']==0)][['Sulfate']].mean()
x

y = kualitas_air[(kualitas_air['Potability']==1)][['Sulfate']].mean()
y

#mengisi nilai null pada kolom sulfate
for i in range(0,len(kualitas_air)):
  if (pd.isnull(kualitas_air['Sulfate'][i]) == True):
    if (kualitas_air['Potability'][i] == 0) :
      kualitas_air['Sulfate'][i] = x
    else :
      kualitas_air['Sulfate'][i] = y

#mengisi nilai null pada kolom Trihalomethanes
kualitas_air['Trihalomethanes'].fillna(value = kualitas_air['Trihalomethanes'].mean() , inplace = True)

#mengecek nilai null
kualitas_air.isnull().sum()

"""**Membulatkan PH**"""

kualitas_air['ph'] = kualitas_air['ph'].round(decimals=1)
kualitas_air['ph'].head()

"""**Tipe-Tipe Air**"""

kualitas_air['Zat Air'] = ""
for i in range(0,len(kualitas_air)):
  if (kualitas_air['ph'][i] <= 0 and kualitas_air['ph'][i] > 1):
    kualitas_air['Zat Air'][i] = "Asam Sulfat"
  elif (kualitas_air['ph'][i] >= 1 and kualitas_air['ph'][i] <= 2):
    kualitas_air['Zat Air'][i] = "Asam Sitrat"
  elif (kualitas_air['ph'][i] >= 2 and kualitas_air['ph'][i] <= 3):
    kualitas_air['Zat Air'][i] = "Asam Askarbonat"
  elif (kualitas_air['ph'][i] >= 3 and kualitas_air['ph'][i] <= 4):
    kualitas_air['Zat Air'][i] = "Asam Nitrat"
  elif (kualitas_air['ph'][i] >= 4 and kualitas_air['ph'][i] <= 5):
    kualitas_air['Zat Air'][i] = "Asam Chlorogenic"
  elif (kualitas_air['ph'][i] >= 5 and kualitas_air['ph'][i] <= 6):
    kualitas_air['Zat Air'][i] = "Asam Amino"
  elif (kualitas_air['ph'][i] >= 6 and kualitas_air['ph'][i] <= 7.5):
    kualitas_air['Zat Air'][i] = "Air Netral"
  elif (kualitas_air['ph'][i] >= 7.5 and kualitas_air['ph'][i] <= 8):
    kualitas_air['Zat Air'][i] = "Air Laut"
  elif (kualitas_air['ph'][i] >= 8 and kualitas_air['ph'][i] <= 9):
    kualitas_air['Zat Air'][i] = "Natrium Bikarbonat"
  elif (kualitas_air['ph'][i] >= 9 and kualitas_air['ph'][i] <= 10):
    kualitas_air['Zat Air'][i] = "Alkali"
  elif (kualitas_air['ph'][i] >= 10 and kualitas_air['ph'][i] <= 11):
    kualitas_air['Zat Air'][i] = "Amonia"
  elif (kualitas_air['ph'][i] >= 11 and kualitas_air['ph'][i] <= 12):
    kualitas_air['Zat Air'][i] = "Natrium"
  elif (kualitas_air['ph'][i] >= 12 and kualitas_air['ph'][i] <= 13):
    kualitas_air['Zat Air'][i] = "Natrium Hipoklorit"
  else :
    kualitas_air['Zat Air'][i] = "Natrium Hidroksida"

kualitas_air.head()

"""## **Data Visualization**"""

#Visualisasi Potability / air dapat di minum
fig = make_subplots(rows=2, cols=1)

tr1=go.Box(x=kualitas_air['Potability'],name='Box Plot Pembagian Potability',boxmean=True)
tr2=go.Histogram(x=kualitas_air['Potability'],name='Histogram Pembagian Potability')

fig.add_trace(tr1,row=1,col=1)
fig.add_trace(tr2,row=2,col=1)

fig.update_layout(height=700, width=1200, title_text="Pembagian Pembagian Potability")
fig.show()
ex.pie(kualitas_air,names='Potability',title='Pembagian Pembagian Potability',hole=0.33)

#Box Plot Setiap kolom
fig1, ax = plt.subplots(figsize=[20, 10])
ax = sb.boxplot(data=kualitas_air, orient='h')
sb.despine(offset=10, trim=True)
plt.title('Box Plot Setiap kolom', fontsize=20)
plt.show()

#Box Plot Kecuali Solid
air1 = pd.DataFrame()
air1 = kualitas_air
air1 = air1.drop('Solids',1)
fig1, ax = plt.subplots(figsize=[20,10])
ax = sb.boxplot(data=air1, orient='h')
sb.despine(offset=10, trim=True)
plt.title('Box Plot Kecuali Solid', fontsize=20)
plt.show()

#fitur numerik
kualitas_air.hist(bins=50, figsize=(20,15))
plt.show()

#mengamati hubungan antar fitur numerik
sb.pairplot(kualitas_air, hue='Potability', diag_kind = 'kde')

#evaluasi korelasi Matrix untuk Fitur Numerik
plt.figure(figsize=(20,15))
correlation_matrix = kualitas_air.corr().round(2)
sb.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Korelasi Matrix untuk Fitur Numerik', size=20)

"""**Relasi Antar Fitur**"""

#Hubungan hardness dengan potability
x = sb.displot(data=kualitas_air, y='Hardness', hue='Potability', col='Zat Air', 
               col_wrap=2, kind='kde', height=4, aspect=2, rug=True)
plt.show()

#Hubungan antara ph dan potability
x = sb.displot(data=kualitas_air, y='ph', hue='Potability', col='Zat Air', palette = 'twilight', col_wrap=3,
    kind='ecdf', height=4, aspect=1.2,rug=True)
plt.show()

#Hubungan Antara Solid dan Potability
x = sb.displot(data=kualitas_air, x='Solids', y='Zat Air', col='Potability', cmap = 'twilight', 
               log_scale=(True, False), col_wrap=4, height=6, aspect=.9)
plt.show()

#Hubungan antara Solids dengan Conductivity
x = sb.jointplot(data=kualitas_air, x='Solids', y='Conductivity', cmap = 'twilight', 
               kind='kde', height=6, aspect=.9)
plt.show()

#Hubungan antara Organic_carbon dan Sulfat
x = sb.jointplot(data=kualitas_air, x='Organic_carbon', y='Sulfate', cmap = 'twilight', 
               kind='hex', height=8)
plt.show()

#Hubungan antara Turbidity dan Trihalomethanes
x = sb.JointGrid(data=kualitas_air, x="Turbidity", y="Trihalomethanes", space=0, ratio=17)
x.plot_joint(sb.scatterplot, size=kualitas_air["Potability"], sizes=(3, 5),
             color="green", alpha=.6, legend=False)
x.plot_marginals(sb.rugplot, height=15, alpha=1,color="Black")

"""## **Data Preprocessing**

**One-Hot-Encoding**
"""

data = pd.get_dummies(kualitas_air, columns = ['Zat Air'])
data

"""**Split Dataset**"""

#Split Dataset
x = data.drop(['Potability'], axis=1)
y = data['Potability']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.8, random_state=600)

x_test=kualitas_air.iloc[:, 0].values
y_test=kualitas_air.iloc[:, 1].values

x_test = x_test.reshape((-1,1))

"""**Standarisasi data**"""

#standarisasi data
scaller = StandardScaler()
X_train = scaller.fit_transform(x_train)
X_test = scaller.fit_transform(x_test)

#Menambahkan Cross Validasi
cv = ShuffleSplit(n_splits=5)
clf = make_pipeline(preprocessing.StandardScaler(), svm.SVC(C=1))
cross_val_score(clf, X_train, y_train, cv=cv)

"""## **Model Dan Evaluasi**

**Model**
"""

#Model
model = Sequential ([
      tf.keras.layers.LSTM(60,input_dim=2, input_shape=(None,1)),
      tf.keras.layers.Dense(60, activation='relu'),
      tf.keras.layers.Dense(40, activation='relu'),
      tf.keras.layers.Dense(20, activation='relu'),
      tf.keras.layers.Dense(10, activation='relu'),
      tf.keras.layers.Dense(2, activation='softmax')])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

history=model.fit(X_train, 
        y_train, 
        epochs=100,
        batch_size=8,
        validation_split=0.2)

#memperlihatkan grafik
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
plt.plot(acc, label='Training Accuracy')
plt.plot(val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training Accuracy and Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')

plt.subplot(1, 2, 2)
plt.plot(loss, label='Training Loss')
plt.plot(val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training Loss and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.show()

#membuat model
print(model.summary())

# convert into .h5
model.save("model.h5")