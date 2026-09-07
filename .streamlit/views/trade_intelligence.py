import streamlit as st
import pandas as pd

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
    
    # Summary Cards
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
    
    # Embedded Agent Quick Query
    with st.expander("🤖 Ask ZindagiAsaan Agent about this export route"):
        user_q = st.text_input("Ask a follow-up question regarding export rules:")
        if user_q:
            st.write(f"**Agent Response:** For exporting {commodity.split('-')[1]} to {target_market}, ensure cold-chain temperature logs are maintained at 4°C-6°C as per DPP guidelines.")
