import base64
import streamlit as st

# Fungsi untuk mendapatkan base64 dari file biner
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as file:
        binary_data = file.read()
        base64_data = base64.b64encode(binary_data).decode('utf-8')
    return base64_data

# Fungsi untuk menampilkan gambar dengan penyesuaian jumlah card
def image(file_paths):
    # Memulai kode CSS untuk styling gambar
    style_block = f"""
        <style>
        .Logo {{ 
            width: 25vw;
        }}
        .LogoContainer {{
            display: flex;
            margin-right: 20px;
        }}
        .card {{ 
            flex: 1 1 150px;
            max-width: 200px;
            padding: 10px;
            text-align: center;
        }}
        </style>
        <div class="LogoContainer">
        """
    # Tambahkan elemen card ketiga dan tutup div utama


    # Looping untuk menambahkan setiap gambar sebagai card
    for file_path in file_paths:
        image_base64 = get_base64_of_bin_file(file_path)
        style_block += f"""<div class="card">
                <img src="data:image/png;base64,{image_base64}" class="Logo">
            </div>
        """

    # Menutup div LogoContainer
    style_block += "</div>"

    # Render dengan markdown dan memperbolehkan HTML tidak aman
    st.markdown(style_block, unsafe_allow_html=True)