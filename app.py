import streamlit as st

# 1. ALWAYS CALL THIS FIRST!
st.set_page_config(
    page_title="AgriAsaan | AI Global Trade Engine",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. NOW YOU CAN CALL st.markdown() OR OTHER STREAMLIT COMMANDS
st.markdown("""
    <style>
    .stAppHeader {background-color: rgba(255, 255, 255, 0.0);}
    .main-header {
        font-size: 24px; font-weight: 700; color: #2E7D32; margin-bottom: 0px;
    }
    .sub-header {
        font-size: 14px; color: #555555; margin-bottom: 20px;
    }
    </style>
""", unsafe_html=True)

# Define pages using Streamlit st.Page API
overview_page = st.Page("views/overview.py", title="Executive Dashboard", icon="📊", default=True)
trade_page    = st.Page("views/trade_intelligence.py", title="ITC & TIPP Trade Engine", icon="🌐")
copilot_page  = st.Page("views/copilot.py", title="ZindagiAsaan AI Agent", icon="🤖")

# Setup Navigation Menu
pg = st.navigation(
    {
        "Main Hub": [overview_page],
        "Core Capabilities": [trade_page, copilot_page],
    },
    position="sidebar"
)

# Global Sidebar Header
st.sidebar.markdown("### 🌾 **AgriAsaan Platform**")
st.sidebar.caption("Powered by ITC Trade Map & TIPP Data")
st.sidebar.divider()

pg.run()
