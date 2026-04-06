import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

def run_app():
    # Konfigurasi halaman
    st.set_page_config(page_title="Portal Dashboard", layout="wide")

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
        selected = option_menu(
            menu_title="Main Menu",
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











