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
                font-size: 40px !important;
                margin-bottom: 0px;
                border-bottom: 2px solid #999999; /* Garis bawah ABU-ABU */
                padding-bottom: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Dictionary berisi link Looker Studio (Isi link URL Anda di sini)
    # Dictionary berisi link Looker Studio
    dashboards = {
        "Banggai POS Dash": "https://lookerstudio.google.com/embed/reporting/cdd758c1-6ed9-464e-8f08-ea2c65b9d3a7/page/p_k6il67mwnd",
        "Stock Monitoring": "https://lookerstudio.google.com/embed/reporting/a83b2cc3-b544-4af4-aa1f-69c855927bf3/page/YzMZE",
        "NGRS Monitoring": "https://lookerstudio.google.com/embed/reporting/7bee7469-1bba-4f25-8ddb-5db385ef8e59/page/RAUQF",
        "SF KPI Monitoring": "https://lookerstudio.google.com/embed/reporting/7d238133-e1f5-4404-8f9e-88022ba8a6b5/page/p_k6il67mwnd",
        "Direct Sales Monitoring": "https://lookerstudio.google.com/embed/reporting/1a96ee0a-4ae7-44ec-885b-d91bea2126ab/page/p_k6il67mwnd",
        "Sales Analysis": "https://lookerstudio.google.com/embed/reporting/ddb47467-7f78-41a1-b14e-53f9d8ba83f9/page/3pUkF"
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
                st.image("Logo.new.png", width=800)
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
