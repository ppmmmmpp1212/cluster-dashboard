import streamlit as st
import streamlit.components.v1 as components

# Mengatur konfigurasi halaman menjadi lebar penuh (wide)
st.set_page_config(page_title="Portal Dashboard", layout="wide")

# Dictionary berisi nama dashboard dan link Looker Studio
dashboards = {
    "Banggai POS Dash": "https://lookerstudio.google.com/embed/reporting/cdd758c1-6ed9-464e-8f08-ea2c65b9d3a7/page/p_k6il67mwnd",
    "Stock Monitoring": "https://lookerstudio.google.com/embed/reporting/a83b2cc3-b544-4af4-aa1f-69c855927bf3/page/YzMZE",
    "NGRS Monitoring": "https://lookerstudio.google.com/embed/reporting/7bee7469-1bba-4f25-8ddb-5db385ef8e59/page/RAUQF"
}

# Membuat Navigasi di Sidebar
st.sidebar.title("📊 Menu Navigasi")
pilihan = st.sidebar.radio("Pilih Dashboard yang ingin dilihat:", list(dashboards.keys()))

# Menampilkan judul sesuai dengan dashboard yang dipilih
st.title(pilihan)
st.markdown("---")

# Membuat kode Iframe HTML untuk embed Looker Studio
# Lebar diset 100% agar responsif mengikuti ukuran layar
iframe_code = f"""
    <iframe 
        width="100%" 
        height="850" 
        src="{dashboards[pilihan]}" 
        frameborder="0" 
        style="border:0" 
        allowfullscreen 
        sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox">
    </iframe>
"""

# Render iframe ke dalam Streamlit
components.html(iframe_code, height=850)