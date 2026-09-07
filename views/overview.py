import streamlit as st

st.markdown("<div class='main-header'>AgriAsaan Trade Intelligence Hub</div>", unsafe_html=True)
st.markdown("<div class='sub-header'>Real-time export suitability, tariff analysis, and compliance automation for Pakistani Agriculture</div>", unsafe_html=True)

# Top KPIs
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Export Markets Tracked", "120+", delta="Live Data")
with col2:
    st.metric("TIPP Compliance Checklists", "45 Agri Commodities")
with col3:
    st.metric("Avg. Exporter Cost Saved", "PKR 45,000/shipment")
with col4:
    st.metric("Active Queries Resolved", "1,850+", delta="+18% this month")

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
