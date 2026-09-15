import streamlit as st

def show():
    st.title("AgriAsaan Trade Intelligence Hub")
    st.caption("Real-time export suitability, tariff analysis, and compliance automation for Pakistani Agriculture")

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
        **AgriAsaan** combines three core engines:
        * **ITC & TIPP Export Engine:** Tariff analysis and export market suitability scores.
        * **Export Margin Calculator:** Live profit and cost breakdown simulator per shipment.
        * **ZindagiAsaan AI Copilot:** Multilingual guidance on DPP rules and customs clearance.
        """)
    with col_b:
        st.info("💡 **Quick Navigation**\n\nUse the sidebar menu to switch between the engines.")
