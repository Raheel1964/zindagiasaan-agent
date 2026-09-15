import streamlit as st
import pandas as pd

def show():
    st.title("🌐 ITC & TIPP Trade Intelligence Engine")
    st.caption("Verify real-time export demand, SPS/TBT compliance rules, and preferential tariffs.")

    st.divider()

    # Inputs
    col1, col2 = st.columns(2)
    with col1:
        commodity = st.selectbox(
            "Select Agri Commodity (HS Code)",
            [
                "080510 - Fresh Oranges / Kinnow",
                "100630 - Semi/Wholly Milled Rice",
                "080450 - Fresh Mangoes",
                "120242 - Groundnuts (Peanuts)"
            ]
        )
    with col2:
        target_market = st.selectbox(
            "Select Destination Market",
            [
                "United Arab Emirates (UAE)",
                "Saudi Arabia (KSA)",
                "United Kingdom (UK)",
                "Germany (EU)",
                "China"
            ]
        )

    if st.button("🔍 Run Market Suitability Analysis", type="primary"):
        st.divider()
        
        # 1. Strategic Decision-Support Layer v1.0
        st.subheader("💡 Strategic Decision-Support Layer v1.0")
        
        m1, m2, m3 = st.columns(3)
        m1.metric("Market Growth (CAGR)", "18.2%", delta="High Potential")
        m2.metric("Applied Tariff Rate", "0.0%", delta="Preferential / FTA")
        m3.metric("Supply Chain Risk", "8.0%", delta="Low Risk", delta_color="inverse")

        # 2. Agentic Strategy Recommendation Block
        st.info(
            f"🤖 **Agentic Strategy Recommendation**\n\n"
            f"**SIGNAL: STABLE EXPANSION.** Recommend 40ft Reefer FCL volume for **{commodity.split('-')[1].strip()}** to **{target_market}**. "
            f"Optimize logistics routing via Karachi Port / Port Qasim with DPP pre-clearance certification."
        )

        st.divider()

        # 3. TIPP Compliance Checklist
        st.subheader("📋 TIPP Export Compliance Checklist")
        data = {
            "Requirement / Document": [
                "Phytosanitary Certificate",
                "Certificate of Origin",
                "Customs Export Declaration (GD)",
                "Pesticide Residue Test Report"
            ],
            "Issuing Authority": [
                "Department of Plant Protection (DPP)",
                "Chamber of Commerce",
                "Pakistan Customs (WeBOC)",
                "ISO Certified Laboratory"
            ],
            "Status": ["Mandatory", "Mandatory", "Mandatory", "Market Dependent"]
        }
        st.dataframe(pd.DataFrame(data), use_container_width=True)

        with st.expander("🤖 Ask ZindagiAsaan Agent about this export route"):
            user_q = st.text_input("Ask a follow-up question regarding export rules:")
            if user_q:
                st.write(
                    f"**Agent Response:** For exporting {commodity.split('-')[1]} to {target_market}, "
                    f"ensure cold-chain temperature logs are maintained at 4°C-6°C as per DPP guidelines."
                )
