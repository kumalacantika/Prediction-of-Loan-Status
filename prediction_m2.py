'''
Nama        : Kumala Cantika Ainun Maya
Batch       : SBY-004
Objective   : Pada bagian ini berisikan ----------------
---------
'''

import numpy as np
import pickle
import json
import streamlit as st
import pandas as pd


with open('model_knn.pkl', 'rb') as file_1:
    model_knn = pickle.load(file_1)

def run():
    with st.form(key='Form Parameter'):
        loanid = st.write()
        gender = st.radio("Gender",["Male","Female"])
        married = st.radio("Marital Status",['Yes','No'])
        dependents = st.selectbox("Dependents",('0','1','2','3+'))
        education = st.radio("Education",['Graduate','Not Graduate'])
        self_employed = st.radio("Self Employed",['Yes','No'])
        applicantincome =  st.number_input("Applicant Income :",min_value=150,max_value=81000,step=1)
        coapplicantincome = st.number_input("CoApplicant Income :",min_value=0,max_value=41700,step=1)
        loanamount = st.number_input("Loan Amount :",min_value=9,max_value=700,step=1)
        loanamountterm = st.selectbox("Loan Amount Term",(12,36,60,84,120,180,240,360,480))
        credithistory = st.radio("Credit History",['No','Yes'])
        propertyarea = st.radio("Property Area",['Urban', 'Semiurban', 'Rural'])
        submitted = st.form_submit_button('Predict')

    if credithistory == 'No':
        credithistory = 0
    else:
        credithistory = 1

    data_inf = {'Loan_ID':loanid,
                'Gender':gender,
                'Married':married,
                'Dependents': dependents,
                'Education':education,
                'Self_Employed':self_employed,
                'ApplicantIncome':applicantincome,
                'CoapplicantIncome':coapplicantincome,
                'LoanAmount':loanamount,
                'Loan_Amount_Term':loanamountterm,
                'Credit_History':credithistory,
                'Property_Area':propertyarea
                }

    df = pd.DataFrame([data_inf])
    st.dataframe(df)

    y_pred_inf = model_knn.predict(df)

    if y_pred_inf == 0:
        y_pred_inf = 'No'
    else:
        y_pred_inf = 'Yes'

    st.write('## Hasil Prediksi Klasifikasi Loan Status : ',str(y_pred_inf))

if __name__ == '__main__':
    run()


