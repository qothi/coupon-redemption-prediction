"""
Milestone 2
Nama: Qothrunnadaa Alyaa
Batch: HCK-009

File ini digunakan untuk menjalankan home page model prediksi penggunaan kupon diskon
"""

import streamlit as st
import eda
import prediction


page = st.sidebar.selectbox(label='Pilih menu untuk memulai:', options=['Home Page', 'Exploratory Data Analysis', 'Prediction Model'])

if page == 'Home Page':
    st.header('Welcome to Coupon Redemption Predictor!') 
    st.write('')
    st.subheader('Milestone 2')
    st.write('Nama      : Qothrunnadaa Alyaa')
    st.write('Batch     : HCK-009')
    st.write('Dataset   : Predicting Coupon Redemption')
    st.write('')
    st.write('')
    st.write('')
    with st.expander('Objektif'):
        st.caption('Memprediksi apakah seorang pelanggan akan menggunakan kupon untuk medapatkan diskon')

    with st.expander('Problem Statement'):
            st.caption('Bagaimana cara memprediksi apakah seorang pelanggan akan menggunakan kupon diskon yang tersedia pada suatu transaksi yang dilakukan pelanggan tersebut?')

    with st.expander('Kesimpulan'):
        st.caption('Untuk memprediksi apakah seorang pelanggan akan menggunakan kupon diskon yang disediakan akan diprediksi menggunakan model Random Forest, di mana model ini dapat memprediksi penggunaan kupon diskon dengan akurasi sekitar 90% (F1 Score).')

elif page == 'Exploratory Data Analysis':
    eda.run()

else:
     prediction.run()