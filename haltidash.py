import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

def run_app():
    # Konfigurasi halaman
    st.set_page_config(page_title="Portal Dashboard", layout="wide")

    # --- CUSTOM CSS ---
    # Disuntikkan setelah page_config untuk mengubah tampilan dasar Streamlit
    st.markdown("""
        <style>
            /* Mengatur background utama menjadi putih */
            .stApp {
                background-color: #ffffff;
            }
            
            /* Warna teks utama abu-abu gelap */
            html, body, [class*="css"] {
                color: #333333; 
            }

            /* Mempercantik Sidebar */
            [data-testid="stSidebar"] {
                background-color: #f8f9fa; /* Abu-abu sangat terang */
                border-right: 1px solid #999999; /* Batas abu-abu palet */
            }

            /* Menyembunyikan header default Streamlit agar lebih bersih */
            header {visibility: hidden;}
            .block-container {
                padding-top: 1rem;
            }
            
            /* Judul Halaman Custom di Main Area */
            .custom-title {
                color: #d32f2f; /* Aksen MERAH pada judul */
                font-weight: 700;
                font-size: 20px !important;
                margin-bottom: 0px;
                border-bottom: 2px solid #999999; /* Garis bawah ABU-ABU */
                padding-bottom: 10px;
            }
        </style>
    """, unsafe_allow_html=True)


    # Dictionary berisi link Looker Studio
    dashboards = {
        "HALTI POS Dash": "https://lookerstudio.google.com/embed/reporting/8c1e5f22-608a-4f73-880e-afb950894780/page/p_k6il67mwnd",
        "Stock Monitoring": "https://lookerstudio.google.com/embed/reporting/6d25ce8f-3bdc-4d05-912c-497d9269cbb3/page/p_96pfhq0urd",
        "NGRS Monitoring": "https://lookerstudio.google.com/embed/reporting/4098e34d-e267-40a8-b617-5bb5f6006447/page/RAUQF",
        "SF KPI Monitoring": "https://lookerstudio.google.com/embed/reporting/767014ae-1f57-4935-bb59-141ba8a9292d/page/p_k6il67mwnd",
        "Direct Sales Monitoring": "https://lookerstudio.google.com/embed/reporting/9ce8f30a-bec7-490a-8622-3409720ccf3e/page/p_k6il67mwnd",
        "Sales Analysis": "https://datastudio.google.com/embed/reporting/e73bc6b3-166b-4c47-913b-b9ae890df48f/page/p_c1xa12xg3d"
    }

# Menu sidebar menggunakan streamlit-option-menu
    with st.sidebar:
        # Tambahan: Header Sidebar Kustom dengan Logo
        try:
            # Membuat 3 kolom pembantu untuk mengatur posisi gambar di tengah (center alignment)
            # Rasio [1, 3, 1] artinya kolom tengah lebih lebar dari kolom pinggir
            col1, col2, col3 = st.columns([1, 3, 1])
            with col2:
                # Gambar dimasukkan ke kolom tengah (col2) agar rata tengah otomatis
                st.image("Logo.new.png", width=700)
        except Exception as e:
            # Teks cadangan jika gambar belum diupload/tidak terbaca
            st.warning("Gambar Logo.new.png tidak ditemukan. Pastikan nama file sama persis (perhatikan huruf besar/kecil).")
        
        st.markdown(
            """
            <div style="text-align: center; margin-bottom: 20px;">
                <p style="color: #999999; margin: 0; font-size: 14px; font-weight: 600;">DASHBOARD SYSTEM</p>
            </div>
            """, 
            unsafe_allow_html=True
        )

        selected = option_menu(
            menu_title=None, # Dihilangkan karena sudah pakai header custom di atas
            # Urutan baru: Sales Analysis, POS, Stock, NGRS, SF KPI, Direct Sales
            options=[
                "Sales Analysis", 
                "Banggai POS Dash", 
                "Stock Monitoring", 
                "NGRS Monitoring", 
                "SF KPI Monitoring", 
                "Direct Sales Monitoring"
            ],
            # Ikon disesuaikan dengan urutan baru
            icons=[
                "graph-up-arrow", # Sales Analysis
                "bar-chart-line", # POS
                "box-seam",       # Stock
                "activity",       # NGRS
                "speedometer2",   # SF KPI
                "briefcase"       # Direct Sales (Diubah sedikit dari speedometer agar beda)
            ], 
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {
                    "padding": "0!important", 
                    "background-color": "transparent" # Mengikuti warna bg sidebar dari CSS
                },
                "icon": {
                    "color": "#999999", # Ikon warna ABU-ABU palet
                    "font-size": "18px"
                },
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "4px 0px",
                    "padding": "12px 15px",
                    "color": "#555555",
                    "--hover-color": "#e0e0e0",
                    "border-radius": "8px"
                },
                "nav-link-selected": {
                    "background-color": "#d32f2f", # Menu aktif warna MERAH palet
                    "color": "#ffffff", # Teks PUTIH saat aktif
                    "font-weight": "bold"
                },
            },
        )
  
    # Menampilkan Judul di area utama sesuai menu yang dipilih
    st.markdown(f'<h1 class="custom-title">{selected}</h1>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True) # Spasi

    # Logika render iframe (cukup satu blok kode ini saja yang berjalan dinamis mengikuti menu)
    iframe_code = f"""
        <div style="border-radius: 10px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border: 1px solid #999999;">
            <iframe 
                width="100%" 
                height="850" 
                src="{dashboards[selected]}" 
                frameborder="0" 
                style="border:0; background-color: #ffffff;" 
                allowfullscreen 
                sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox">
            </iframe>
        </div>
    """
    
    # Menampilkan iframe di Streamlit
    components.html(iframe_code, height=860) # height ditambah sedikit untuk mengakomodasi box-shadow

if __name__ == "__main__":
    run_app()


