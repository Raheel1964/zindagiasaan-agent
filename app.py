import streamlit as st

# 1. ALWAYS FIRST
st.set_page_config(
    page_title="AgriAsaan | AI Global Trade Engine",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. SIDEBAR NAVIGATION
st.sidebar.title("🌾 AgriAsaan Platform")
st.sidebar.caption("Powered by ITC Trade Map & TIPP Data")
st.sidebar.divider()

selected_page = st.sidebar.radio(
    "Navigation Menu",
    [
        "📊 Executive Dashboard",
        "🌐 ITC & TIPP Trade Engine",
        "💰 Export Margin Calculator",
        "🤖 ZindagiAsaan AI Agent"
    ]
)

# 3. PAGE ROUTING
if selected_page == "📊 Executive Dashboard":
    from views import overview
    overview.show()
elif selected_page == "🌐 ITC & TIPP Trade Engine":
    from views import trade_intelligence
    trade_intelligence.show()
elif selected_page == "💰 Export Margin Calculator":
    from views import margin_calculator
    margin_calculator.show()
elif selected_page == "🤖 ZindagiAsaan AI Agent":
    from views import copilot
    copilot.show()
