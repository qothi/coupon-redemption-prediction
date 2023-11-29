"""
Milestone 2
Nama: Qothrunnadaa Alyaa
Batch: HCK-009

File ini digunakan untuk menjalankan model prediksi penggunaan kupon diskon
"""

import streamlit as st
import pandas as pd
import pickle

# Membuat function untuk dipanggil di app.py
def run():
    st.title('Coupon Redemption Predictor')

    # Memasukkan besaran diskon menggunakan kupon
    coupon_discount = st.number_input(label='Discount from Coupon', min_value=0.00)

    # Memasukkan lamanya periode promo
    campaign_length = st.number_input(label='Promo Period (in Days)', min_value=0.00)

    # Memasukkan tanggal transaksi
    trx_day = st.number_input(label='Transaction Date', min_value=0.00)

    # Memasukkan tanggal mulai periode promosi
    start_day = st.number_input(label='Promotion Start Date', min_value=0.00)

    # Memasukkan tanggal berakhir periode promosi
    end_day = st.number_input(label='Promotion End Date', min_value=0.00)

    # Memasukkan tipe brand
    brand_type = st.selectbox(label='Brand Type', options=['Established','Local'])

    # Daftar kategori barang
    category_opt = ['Dairy, Juices & Snacks','Grocery','Seafood','Prepared Food','Packaged Meat','Meat',
                'Pharmaceutical','Natural Products','Skin & Hair Care','Flowers & Plants','Garden',
                'Travel','Miscellaneous','Bakery','Vegetables (cut)','Salads']
    
    # Memasukkan kategori barang
    category = st.selectbox(label='Item Category', options=category_opt)

    # Memasukkan tipe campaign/promosi
    campaign_type = st.selectbox(label='Campaign Type', options=['Y','X'])

    # Daftar kelompok umur
    age_option = ['18-25','26-35','36-45','46-55','56-70','70+']

    # Memasukkan kelompok umur pelanggan
    age_range = st.selectbox(label='Customer Age Range', options=age_option)

    # Memasukkan tingkat pendapatan pelanggan
    income_bracket = st.select_slider(label='Customer Income Bracket',options=[n for n in range(1,13)])

    # Membuat data inference dari data yang dimasukkan
    data_inf = pd.DataFrame({
        'coupon_discount': coupon_discount,
        'campaign_length': campaign_length,
        'trx_day': trx_day,
        'start_day': start_day,
        'end_day': end_day,
        'brand_type': brand_type,
        'category': category,
        'campaign_type': campaign_type,
        'age_range': age_range,
        'income_bracket': income_bracket
    }, index=[0])
    
    # Menampilkan data 
    st.header("Transaction Overview")
    st.table(data_inf)

    # Memprediksi apakah kupon akan digunakan atau tidak
    if st.button(label='Predict'):
        with open('model.pkl','rb') as model:
            model = pickle.load(model)
            
        y_pred_inf = model.predict(data_inf)
        
        if y_pred_inf == 0:
            st.write('Coupon was not redeemed.')
        else:
            st.write('Coupon was redeemed.')