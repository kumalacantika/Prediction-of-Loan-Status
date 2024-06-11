import streamlit as st
import eda_m2
import prediction_m2

navigation = st.sidebar.selectbox('Pilih Halaman: ', ('EDA', 'Prediksi'))

if navigation == 'EDA':
    eda_m2.run()
else:
    prediction_m2.run()