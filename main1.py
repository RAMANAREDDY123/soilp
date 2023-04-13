import streamlit as st
import pandas as pd
import joblib
st.title('reddy')
model=joblib.load('rf.joblib')

def predict_soil(features):
    # Make prediction using the loaded model
    prediction = model.predict(features)
    return prediction

st.title('SOIL FERTILITY PREDICTION USING NPK')

nitrogen=st.number_input('Enter nitrogen value')
phosporous=st.number_input('Enter phosporous value')
potassium=st.number_input('Enter potassium value')
content_nitrogen=st.selectbox('Select Nitrogen content',['High','Low'])
if content_nitrogen=='High':
    content_nitrogen=1
else:
    content_nitrogen=0

content_phosporous=st.selectbox('Enter the phosporous content',['High','Low'])
if content_phosporous=='High':
    content_phosporous=1
else:
    content_phosporous=0

content_potassium=st.selectbox('Enter potassium content',['High','Low'])
if content_potassium=='High':
    content_potassium=1
else:
    content_potassium=0


data=pd.DataFrame({'Nitrogen':nitrogen,'Phosphorous':phosporous,
                   
                  'Potassium':potassium,
                  'Content of Nitrogen':content_nitrogen,
                  'Content of Phosphorous':content_phosporous,
                  'Content of Potassium':content_potassium,

                   }, index=[0]
                )
if st.button("Predict"):
    # Make prediction on the input features
    prediction = predict_soil(data)
    st.write(prediction)
