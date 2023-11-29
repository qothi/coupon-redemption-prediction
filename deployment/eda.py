"""
Milestone 2
Nama: Qothrunnadaa Alyaa
Batch: HCK-009

File digunakan untuk menjalankan page EDA dari model prediksi penggunaan kupon diskon
"""

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# Membuat function untuk dipanggil pada app.py
def run():
    st.title('Exploratory Data Analysis')
    st.write('Laman ini berisi eksplorasi data dari dataset Predicting Coupon Redemption. Dataset ini akan digunakan untuk memprediksi apakah suatu kupon diskon akan digunakan oleh pelanggan pada suatu transaksi.')

# Load csv dataset
    df = pd.read_csv('coupon_redemption.csv')

# Dataset yang digunakan
    st.header('Dataset Coupon Redemption')
    st.table(df.head(10))

# Menampilkan penggunaan kupon berdasarkan tipe brand barang yang dibeli
    st.header('Coupon Redemption Based on Brand Type')
    num_corr = Image.open('brand_type.png')
    st.image(num_corr, caption='Coupon Redemption Based on Brand Type')

# Penjelasan dari penggunaan kupon berdasarkan tipe brand
    with st.expander('Explanation'):
        st.caption('Pelanggan cenderung menggunakan atau mendapatkan kupon diskon ketika berbelanja produk-produk dari brand yang tergolong established dibandingkan produk-produk dari brand lokal.')

# Menampilkan penggunaan kupon berdasarkan kategori barang yang dibeli
    st.header("Coupon Redemption By Item's Category")
    cat_corr = Image.open('item_category.png')
    st.image(cat_corr, caption="Coupon Redemption Based on Item's Category")

# Penjelasan dari penggunaan kupon berdasarkan kategori barang 
    with st.expander('Explanation'):
        st.caption('Pelanggan paling banyak menggunakan kupon diskon untuk membeli minuman dan snack, grocery, dan seafood. Sementara kupon diskon tidak digunakan pada produk sayuran, produk terkait kebun dan taman, produk travel, serta tidak digunakan di bakery.')

# Menampilkan penggunaan kupon berdasarkan kelompok umur pelanggan
    st.header("Coupon Redemption By Customer's Age")
    edu_def = Image.open('age_range.png')
    st.image(edu_def, caption="Coupon Redemption By Customer's Age Range")

# Penjelasan dari penggunaan kupon berdasarkan umur pelanggan
    with st.expander('Explanation'):
        st.caption('Pelanggan berumur 36 - 55 tahun merupakan pelanggan yang paling banyak menggunakan kupon diskon, dan kelompok umur 18 - 25 merupakan kelompok umur yang paling sedikit menggunakan kupon diskon.')

# Menampilkan penggunaan kupon berdasarkan tingkat pendapatan pelanggan
    st.header("Coupon Redemption By Customer's Income")
    edu_def = Image.open('income_bracket.png')
    st.image(edu_def, caption="Coupon Redemption By Customer's Income Bracket")

# Penjelasan dari penggunaan kupon berdasarkan tingkat pendapatan pelanggan
    with st.expander('Explanation'):
        st.caption('Dalam dataset ini semakin tinggi pendapatan pelanggan, maka semakin tinggi income bracket-nya. Pelanggan dengan tingkat pendapatan yang tinggi cenderung tidak menggunakan kupon diskon. Penggunaan kupon diskon paling tinggi ada pada pelanggan dengan tingkat pendapatan menengah, seperti pada income bracket 5, 6, dan 9.')        