import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Jarak Tempuh Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Bahan Bakar Mobil')
engineSize = st.number_input('Input Ukuran Mesin Mobil')

kurs = st.number_input('Kurs 1 GBP ke Rupiah', value=24000, step=100)

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    harga_gbp = predict[0]
    harga_idr = harga_gbp * kurs

    harga_idr_str = f'{harga_idr:,.0f}'.replace(',', '.')

    st.write(f'Estimasi Harga Mobil Bekas: £{harga_gbp:,.0f}')
    st.write(f'Estimasi dalam Rupiah: Rp{harga_idr_str}')