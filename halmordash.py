import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

def run_app():
    # Konfigurasi halaman
    st.set_page_config(page_title="Portal Dashboard", layout="wide")

    # Dictionary berisi link Looker Studio
    dashboards = {
        "HALMOR POS Dash": "https://lookerstudio.google.com/embed/reporting/60f10d03-cf06-4d1e-9979-3e868ef87019/page/p_k6il67mwnd",
        "Stock Monitoring": "https://lookerstudio.google.com/embed/reporting/8a25d8b8-c6e6-4751-ab10-9b7b9dfa8a09/page/p_6hzriq0urd",
        "NGRS Monitoring": "https://lookerstudio.google.com/embed/reporting/5187caa9-adac-43b6-896c-96b975d30efb/page/RAUQF",
        "SF KPI Monitoring": "https://lookerstudio.google.com/embed/reporting/e151cd8f-fcb1-415a-b141-5173fdbaa9e5/page/p_k6il67mwnd",
        "Direct Sales Monitoring": "https://lookerstudio.google.com/embed/reporting/d521a12f-2067-4969-a16a-e7fa06accca1/page/p_k6il67mwnd",
        "Sales Analysis": "https://lookerstudio.google.com/embed/reporting/c9ed7612-b03d-4640-807a-f62c247341dd/page/3pUkF"
    }

# Menu sidebar menggunakan streamlit-option-menu
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            # Urutan baru: Sales Analysis, POS, Stock, NGRS, SF KPI, Direct Sales
            options=[
                "Sales Analysis", 
                "HALMOR POS Dash", 
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
                "speedometer2"    # Direct Sales
            ], 
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "20px"},
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "#02ab21"},
            },
        )
  

    # Logika render iframe (cukup satu blok kode ini saja yang berjalan dinamis mengikuti menu)
    iframe_code = f"""
        <iframe 
            width="100%" 
            height="850" 
            src="{dashboards[selected]}" 
            frameborder="0" 
            style="border:0" 
            allowfullscreen 
            sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox">
        </iframe>
    """
    
    # Menampilkan iframe di Streamlit
    components.html(iframe_code, height=850)

if __name__ == "__main__":
    run_app()











