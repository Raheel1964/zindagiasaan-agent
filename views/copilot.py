import streamlit as st
import pandas as pd

def show():
    st.title("💰 Export Margin & Cost Calculator")
    st.caption("Simulate land-to-market costs, duty impacts, and net profitability per shipment.")

    st.divider()

    # Controls
    col1, col2, col3 = st.columns(3)
    with col1:
        commodity = st.selectbox(
            "Agri Commodity",
            ["Fresh Oranges / Kinnow (080510)", "Basmati Rice (100630)", "Fresh Mangoes (080450)", "Groundnuts / Peanuts (120242)"]
        )
    with col2:
        volume_tons = st.number_input("Export Volume (Metric Tons)", min_value=1.0, value=25.0, step=1.0)
    with col3:
        target_market = st.selectbox("Destination Market", ["UAE (Dubai)", "Saudi Arabia (Riyadh)", "United Kingdom (London)", "China (Guangzhou)"])

    st.subheader("1. Cost Breakdown Input (PKR / Metric Ton)")
    c1, c2, c3 = st.columns(3)
    with c1:
        farmgate_price = st.number_input("Farmgate Sourcing Price", value=85000, step=5000)
        processing_pack = st.number_input("Sorting, Washing & Packaging", value=25000, step=2000)
    with c2:
        inland_freight = st.number_input("Inland Transport to Port", value=15000, step=1000)
        customs_dpp = st.number_input("Customs, DPP Inspection & Certs", value=12000, step=1000)
    with c3:
        ocean_freight = st.number_input("International Freight (Reefer)", value=45000, step=2000)
        import_duty_pct = st.number_input("Destination Tariff / Duty (%)", value=0.0, step=0.5)

    st.subheader("2. Target Selling Price")
    sp_col1, sp_col2 = st.columns(2)
    with sp_col1:
        selling_price_usd = st.number_input("Destination Market Selling Price ($ USD / Ton)", value=850.0, step=10.0)
    with sp_col2:
        pkr_usd_rate = st.number_input("USD to PKR Exchange Rate", value=280.0, step=0.5)

    # Calculation Logic
    cost_per_ton = farmgate_price + processing_pack + inland_freight + customs_dpp + ocean_freight
    duty_cost_per_ton = (selling_price_usd * pkr_usd_rate) * (import_duty_pct / 100.0)
    total_cost_per_ton = cost_per_ton + duty_cost_per_ton

    revenue_per_ton_pkr = selling_price_usd * pkr_usd_rate
    net_profit_per_ton = revenue_per_ton_pkr - total_cost_per_ton

    total_shipment_revenue = revenue_per_ton_pkr * volume_tons
    total_shipment_cost = total_cost_per_ton * volume_tons
    total_shipment_profit = net_profit_per_ton * volume_tons
    net_margin_pct = (net_profit_per_ton / revenue_per_ton_pkr) * 100 if revenue_per_ton_pkr > 0 else 0

    st.divider()
    st.subheader("📊 Export Economics Summary")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Shipment Cost", f"PKR {total_shipment_cost:,.0f}")
    m2.metric("Gross Revenue", f"PKR {total_shipment_revenue:,.0f}")
    m3.metric("Net Profit", f"PKR {total_shipment_profit:,.0f}", delta=f"{net_margin_pct:.1f}% Net Margin")
    m4.metric("Net Profit / Ton", f"PKR {net_profit_per_ton:,.0f}")

    st.subheader("📋 Unit Cost Breakdown (Per Metric Ton)")
    breakdown_df = pd.DataFrame({
        "Cost Element": ["Farmgate Sourcing", "Processing & Packaging", "Inland Transport", "Customs & DPP Clearance", "International Freight", "Import Duty Cost", "TOTAL COST"],
        "Cost (PKR / Ton)": [farmgate_price, processing_pack, inland_freight, customs_dpp, ocean_freight, duty_cost_per_ton, total_cost_per_ton],
        "Percentage of Cost": [
            f"{(farmgate_price/total_cost_per_ton)*100:.1f}%",
            f"{(processing_pack/total_cost_per_ton)*100:.1f}%",
            f"{(inland_freight/total_cost_per_ton)*100:.1f}%",
            f"{(customs_dpp/total_cost_per_ton)*100:.1f}%",
            f"{(ocean_freight/total_cost_per_ton)*100:.1f}%",
            f"{(duty_cost_per_ton/total_cost_per_ton)*100:.1f}%",
            "100.0%"
        ]
    })
    st.dataframe(breakdown_df, use_container_width=True)
