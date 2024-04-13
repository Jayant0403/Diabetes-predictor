# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 10:59:29 2024

@author: JAYANT
"""

import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
st.set_page_config(layout="wide")



# loading the saved model
loaded_model = pickle.load(open('D:/Machine Learning/Deploying Machine Learning Model/trained_model.sav','rb'))



# sidebar for navigate
with st.sidebar:
    selected = option_menu('Welcome',
                           ['Home',
                            'Predictor',
                            'Tech Stack',
                            'ML Code',
                            'Contributors'],
                            icons=['house', 'stack', 'cpu','terminal', 'people-fill'],
                         menu_icon="activity", default_index=0, 
                         styles={
                            "container": {"padding": "5!important", "background-color": "#1a1a1a"},
                            "icon": {"color": "White", "font-size": "25px"}, 
                            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#4d4d4d"},
                            "nav-link-selected": {"background-color": "#4d4d4d"},
                        }
                           )
#Diabetes Prediction Page
if(selected == 'Predictor'):
    
    #page title
    st.title("TYPE-2 DIABETES PREDICTOR")
    st.subheader("For women above 21 years of age")
    
    
    #getting the input data from the user
#   col1,col2,col3 = st.columns(3)
#  with col1:
#       Pregnancies = st.text_input('Number of Pregnancies')
    
#    with col2:
#        Glucose = st.text_input('Glucose (mmol / L)')
    
 #   with col3:
 #       BloodPressure = st.text_input('BloodPressure (mm Hg)')
        
 #   with col1:
#        SkinThickness = st.text_input('SkinThickness ')
    
 #   with col2:
 #       Insulin = st.text_input('Insulin (mu U/ml)')
        
  #  with col3:
  #      BMI = st.text_input('BMI value')
    
 #   with col1:
  #      DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
  #  with col2:
 #       Age = st.text_input('Age (in years)')
 
 
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose (mmol / L)')
    BloodPressure = st.text_input('BloodPressure (mm Hg)')
    SkinThickness = st.text_input('SkinThickness ')
    Insulin = st.text_input('Insulin (mu U/ml)')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age (in years)')
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = loaded_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = '**The patient has high risk of Type-2 Diabetes**'
        else:
          diab_diagnosis = '**The patient has low risk of Type-2 Diabetes**'
        
        
    st.success(diab_diagnosis)
    
    
if(selected == 'Home'):
    st.title('AI for Healthcare')
    st.markdown("<p style='text-align: justify;'>The objective of the project is to diagnostically predict whether or not a patient has Type 2 diabetes. \nThis predictor is built for Women above 21 years of age. The dataset, originally from the National Institute of Diabetes and Digestive and Kidney Diseases, used for this project consists of several medical predictor variables and one target variable, Outcome. Predictor variables includes the number of pregnancies the patient has had, their BMI, insulin level, age, and so on.</p>", unsafe_allow_html=True)
    
    with open("D:/Machine Learning/Deploying Machine Learning Model/pic.html",'r') as f:
        pic=f.read();
        components.html(pic, height=400)
 #   components.iframe("https://raw.githubusercontent.com/snshahgit/healthcare-backend/develop/healthcare.gif")
        
        
if(selected == 'ML Code'):
    st.write("To view the complete code for the end-to-end project, visit our [Github]((https://github.com/Jayant0403/Diabetes-predictor)")
    components.iframe("https://www.kaggle.com/embed/sns5154/type-2-diabetes-diagnosis-val-85-7-test-72-7?kernelSessionId=98362179",height=1000,)
    
    
if(selected == 'Contributors'):
     
     
     with open("D:/Machine Learning/Deploying Machine Learning Model/conti.html",'r') as f:
         pic=f.read();
         components.html(pic, height=400)   
    


    
    
    
    
    
   