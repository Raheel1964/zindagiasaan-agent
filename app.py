import streamlit as st
import pandas as pd

# 1. MUST BE THE VERY FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="AgriAsaan | AI Global Trade Engine",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CUSTOM CSS STYLING
st.markdown("""
    <style>
    .stAppHeader {background-color: rgba(255, 255, 255, 0.0);}
    .main-header {
        font-size: 26px; font-weight: 700; color: #2E7D32; margin-bottom: 0px;
    }
    .sub-header {
        font-size: 14px; color: #555555; margin-bottom: 20px;
    }
    </style>
""", unsafe_html=True)

# 3. SIDEBAR NAVIGATION
st.sidebar.markdown("### 🌾 **AgriAsaan Platform**")
st.sidebar.caption("Powered by ITC Trade Map & TIPP Data")
st.sidebar.divider()

selected_page = st.sidebar.radio(
    "Navigation Menu",
    ["📊 Executive Dashboard", "🌐 ITC & TIPP Trade Engine", "🤖 ZindagiAsaan AI Agent"]
)

# 4. PAGE ROUTING LOGIC

# --- PAGE 1: EXECUTIVE DASHBOARD ---
if selected_page == "📊 Executive Dashboard":
    st.markdown("<div class='main-header'>AgriAsaan Trade Intelligence Hub</div>", unsafe_html=True)
    st.markdown("<div class='sub-header'>Real-time export suitability, tariff analysis, and compliance automation for Pakistani Agriculture</div>", unsafe_html=True)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Export Markets Tracked", "120+", delta="Live Data")
    col2.metric("TIPP Compliance Checklists", "45 Agri Commodities")
    col3.metric("Avg. Exporter Cost Saved", "PKR 45,000/shipment")
    col4.metric("Active Queries Resolved", "1,850+", delta="+18% this month")

    st.divider()

    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.subheader("📌 Platform Capability Overview")
        st.write("""
        **AgriAsaan** combines two core engines:
        * **ITC & TIPP Export Engine:** Automatically pulls data from International Trade Centre (ITC) and Trade Information Portal of Pakistan (TIPP) to provide real-time tariff analysis and export market suitability scores.
        * **ZindagiAsaan AI Copilot:** Natural language agent assisting farmers, traders, and exporters with regulatory answers, document verification, and multilingual guidance.
        """)
    with col_b:
        st.info("💡 **Quick Navigation**\n\nUse the sidebar menu to launch the **ITC & TIPP Engine** or converse with the **ZindagiAsaan AI Agent**.")

# --- PAGE 2: TRADE ENGINE ---
elif selected_page == "🌐 ITC & TIPP Trade Engine":
    st.markdown("<div class='main-header'>🌐 ITC & TIPP Trade Intelligence Engine</div>", unsafe_html=True)
    st.caption("Verify real-time export demand, SPS/TBT compliance rules, and preferential tariffs.")

    col1, col2 = st.columns(2)
    with col1:
        commodity = st.selectbox(
            "Select Agri Commodity (HS Code)",
            ["080510 - Fresh Oranges / Kinnow", "100630 - Semi/Wholly Milled Rice", "080450 - Fresh Mangoes", "120242 - Groundnuts (Peanuts)"]
        )
    with col2:
        target_market = st.selectbox(
            "Select Destination Market",
            ["United Arab Emirates (UAE)", "Saudi Arabia", "United Kingdom", "Germany", "China"]
        )

    if st.button("🔍 Run Market Suitability Analysis", type="primary"):
        st.divider()
        m1, m2, m3 = st.columns(3)
        m1.metric("Market Demand Index", "High (88/100)", delta="Favorable")
        m2.metric("Customs Duty Rate", "0.0%", delta="FTA / Preferential")
        m3.metric("Compliance Complexity", "Medium", delta="SPS Check Required")

        st.subheader("📋 TIPP Export Compliance Checklist")
        data = {
            "Requirement / Document": ["Phytosanitary Certificate", "Certificate of Origin", "Customs Export Declaration (GD)", "Pesticide Residue Test Report"],
            "Issuing Authority": ["Department of Plant Protection (DPP)", "Chamber of Commerce", "Pakistan Customs (WeBOC)", "ISO Certified Laboratory"],
            "Status": ["Mandatory", "Mandatory", "Mandatory", "Market Dependent"]
        }
        st.dataframe(pd.DataFrame(data), use_container_width=True)

        with st.expander("🤖 Ask ZindagiAsaan Agent about this export route"):
            user_q = st.text_input("Ask a follow-up question regarding export rules:")
            if user_q:
                st.write(f"**Agent Response:** For exporting {commodity.split('-')[1]} to {target_market}, ensure cold-chain temperature logs are maintained at 4°C-6°C as per DPP guidelines.")

# --- PAGE 3: AI COPILOT ---
elif selected_page == "🤖 ZindagiAsaan AI Agent":
    st.markdown("<div class='main-header'>🤖 ZindagiAsaan AI Copilot</div>", unsafe_html=True)
    st.caption("Multilingual AI Assistant for Pakistani Agri-Exporters and Farmers")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Assalam-o-Alaikum! I am your ZindagiAsaan Copilot. Ask me anything about crop export requirements, TIPP rules, or market pricing."}
        ]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if prompt := st.chat_input("Type your question here (e.g., How do I register on WeBOC for rice exports?)..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        response = f"I see you asked about: '{prompt}'. Based on TIPP regulations, you need an NTN, Sales Tax Registration, and an active bank account to register on WeBOC."

        with st.chat_message("assistant"):
            st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
