import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

def run_app():
    # Konfigurasi halaman
    st.set_page_config(page_title="Portal Dashboard", layout="wide")

    # Dictionary berisi link Looker Studio
    dashboards = {
        "Morowali POS Dash": "https://lookerstudio.google.com/embed/reporting/00eae712-7276-480b-810c-72c3c0bc4d8a/page/p_k6il67mwnd",
        "Stock Monitoring": "https://lookerstudio.google.com/embed/reporting/bcfbbc98-72d5-4c0b-ba9d-dbf1b4525fa9/page/p_kuu3aq0urd",
        "NGRS Monitoring": "https://lookerstudio.google.com/embed/reporting/5465fcc0-89f8-48cb-a204-d0b975c8df8b/page/RAUQF",
        "SF KPI Monioring": "https://lookerstudio.google.com/embed/reporting/2cf63382-7bc8-4c20-857b-7c55aa6e5c3b/page/p_k6il67mwnd",
        "Direct Sales Monitoring": "https://lookerstudio.google.com/embed/reporting/590d91ca-aac9-4431-8b4f-c443921e289b/page/p_k6il67mwnd",
        "Sales Analysis": "https://lookerstudio.google.com/embed/reporting/67eae6bf-32bc-4453-bef4-b13be5570d64/page/3pUkF"
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












