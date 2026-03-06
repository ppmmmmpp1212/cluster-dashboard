import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

def run_app():
    # Konfigurasi halaman
    st.set_page_config(page_title="Portal Dashboard", layout="wide")

    # Dictionary berisi link Looker Studio
    dashboards = {
        "Ternate POS Dash": "https://lookerstudio.google.com/embed/reporting/a393ce24-3648-4e24-bc2b-abdd6a858999/page/p_k6il67mwnd",
        "Stock Monitoring": "https://lookerstudio.google.com/embed/reporting/45cde8f8-4350-45cb-bd7f-6ceb211365de/page/p_zhrpkq0urd",
        "NGRS Monitoring": "https://lookerstudio.google.com/embed/reporting/7fbe8c25-afee-4cbb-b022-7bf9b951c23c/page/RAUQF",
        "SF KPI Monitoring": "https://lookerstudio.google.com/embed/reporting/f68b6a7d-b1c2-4d4a-bc77-bc3a4a43821a/page/p_k6il67mwnd",
        "Direct Sales Monitoring": "https://lookerstudio.google.com/embed/reporting/fb7967af-ee27-4d2c-847b-a23b75a02be1/page/p_k6il67mwnd",
        "Sales Analysis": "https://lookerstudio.google.com/embed/reporting/208aa9c1-d4dd-42fa-8096-86f4dc854db4/page/3pUkF"
    }

# Menu sidebar menggunakan streamlit-option-menu
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            # Urutan baru: Sales Analysis, POS, Stock, NGRS, SF KPI, Direct Sales
            options=[
                "Sales Analysis", 
                "Ternate POS Dash", 
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












