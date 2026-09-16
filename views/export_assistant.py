import streamlit as st
import pandas as pd

def show():
    st.title("🔍 Single-Product Export Assistant")
    st.caption("Search any Pakistani agri crop or artisanal produce by name or HS Code to receive an instant 360° Export Playbook.")

    st.divider()

    # Database indexed by HS Code and Product Name
    product_db = {
        "Fresh Mangoes": {
            "hs_code": "HS 080450",
            "full_title": "Fresh Mangoes (HS Code: 0804.50)",
            "top_buyers": [("UAE", "+14% Demand"), ("United Kingdom", "+18% Demand"), ("Saudi Arabia", "+9% Demand")],
            "dpp_rules": "Phytosanitary Cert + Hot Water Treatment (HWT) mandatory for EU/UK.",
            "weboc_docs": "Export GD (HS 080450), Form E (State Bank), Chamber Certificate of Origin.",
            "mrl_tariff": "0% Preferential Duty in GCC under HS 080450. Max Residue Limit (MRL) testing required.",
            "mandi_price": 120, "export_price": 550, "freight": 180, "pack_cost": 45
        },
        "Fresh Oranges / Kinnow": {
            "hs_code": "HS 080510",
            "full_title": "Fresh Oranges / Kinnow (HS Code: 0805.10)",
            "top_buyers": [("Russia", "+22% Demand"), ("UAE", "+11% Demand"), ("Indonesia", "+15% Demand")],
            "dpp_rules": "Mandatory cold-treatment protocol (4°C-6°C) for 10 days post-pack.",
            "weboc_docs": "Phytosanitary Cert, WeBOC Customs Clearance under HS 080510, Commercial Invoice.",
            "mrl_tariff": "0% FTA rate for GCC; 5% standard tariff under HS 080510 in Southeast Asia.",
            "mandi_price": 60, "export_price": 280, "freight": 95, "pack_cost": 30
        },
        "Sweet Potato": {
            "hs_code": "HS 071420",
            "full_title": "Sweet Potato (HS Code: 0714.20)",
            "top_buyers": [("United Kingdom", "+24% Growth"), ("UAE", "+16% Growth"), ("Qatar", "+12% Growth")],
            "dpp_rules": "Soil-free root clearance inspection & fungal spore laboratory test.",
            "weboc_docs": "DPP Clearance Cert, Packing List, Certificate of Origin under HS 071420.",
            "mrl_tariff": "0% Tariff in GCC. EU organic entry standards apply under HS 071420.",
            "mandi_price": 75, "export_price": 420, "freight": 140, "pack_cost": 35
        },
        "Dried Figs / Hunza Produce": {
            "hs_code": "HS 080420",
            "full_title": "Dried Figs / Hunza Produce (HS Code: 0804.20)",
            "top_buyers": [("Germany", "+30% High Margin"), ("UK", "+22% Demand"), ("UAE", "+15% Demand")],
            "dpp_rules": "Aflatoxin moisture level lab certificate (<12% moisture threshold).",
            "weboc_docs": "Lab Test Report, Chamber Cert of Origin, GD Declaration under HS 080420.",
            "mrl_tariff": "0% Duty under EU GSP+ scheme for Pakistan under HS 080420.",
            "mandi_price": 450, "export_price": 1850, "freight": 320, "pack_cost": 110
        },
        "Red Chili / Whole Dried": {
            "hs_code": "HS 090422",
            "full_title": "Red Chili / Whole Dried (HS Code: 0904.22)",
            "top_buyers": [("China", "+35% Growth"), ("UAE", "+12% Demand"), ("Malaysia", "+18% Demand")],
            "dpp_rules": "Aflatoxin & Pesticide Residue Clearance from ISO 17025 accredited lab.",
            "weboc_docs": "DPP Export Permit, WeBOC Clearance under HS 090422, Quality Test Sheet.",
            "mrl_tariff": "0% Duty under CPFTA (China-Pakistan Free Trade Agreement) for HS 090422.",
            "mandi_price": 320, "export_price": 1150, "freight": 210, "pack_cost": 60
        }
    }

    # Format options to show HS Code directly in the search dropdown
    dropdown_options = [f"{v['hs_code']} - {k}" for k, v in product_db.items()]

    selected_option = st.selectbox(
        "🔎 Search or select product by HS Code or Commodity Name:",
        dropdown_options
    )

    if selected_option:
        # Extract product key
        product_key = selected_option.split("-")[1].strip()
        item = product_db[product_key]

        # Professional Header showing exact HS Classification
        st.subheader(f"📦 Export Playbook: {item['full_title']}")
        st.caption(f"Official Customs Classification: **{item['hs_code']}** | World Customs Organization (WCO) Standard")
        
        # 1. Market Opportunity Cards
        col_a, col_b, col_c = st.columns(3)
        col_a.metric("Primary Target Market", item["top_buyers"][0][0], delta=item["top_buyers"][0][1])
        col_b.metric("Secondary Target Market", item["top_buyers"][1][0], delta=item["top_buyers"][1][1])
        col_c.metric("High Growth Corridor", item["top_buyers"][2][0], delta=item["top_buyers"][2][1])

        st.divider()

        # 2. Export & Import Compliance Requirements
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"### 🇵🇰 Pakistan Export Clearance ({item['hs_code']})")
            st.info(f"**DPP Phytosanitary Standard:**\n{item['dpp_rules']}")
            st.success(f"**WeBOC Custom Filing:**\n{item['weboc_docs']}")
        with c2:
            st.markdown(f"### 🌐 Destination Import & Tariff Rules ({item['hs_code']})")
            st.warning(f"**Tariff & MRL Requirements:**\n{item['mrl_tariff']}")
            st.write("**Recommended Packaging:** Export-grade ventilated corrugated boxes.")

        st.divider()

        # 3. Unit Profitability Breakdown
        st.subheader(f"💰 Unit Commercial Margin for {item['hs_code']} (PKR / kg)")
        
        cost_total = item["mandi_price"] + item["pack_cost"] + item["freight"]
        net_profit = item["export_price"] - cost_total
        margin_pct = (net_profit / item["export_price"]) * 100

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Local Mandi Sourcing", f"PKR {item['mandi_price']}/kg")
        m2.metric("Landed Freight & Pack Cost", f"PKR {item['pack_cost'] + item['freight']}/kg")
        m3.metric("Target Destination Price", f"PKR {item['export_price']}/kg")
        m4.metric("Est. Net Profit Margin", f"PKR {net_profit}/kg", delta=f"{margin_pct:.1f}% ROI")
