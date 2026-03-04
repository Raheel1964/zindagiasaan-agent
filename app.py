import streamlit as st
import google.generativeai as genai

# --- 1. CONFIG & STYLING ---
st.set_page_config(page_title="Zindagiasaan Agent", layout="wide")
st.title("🌾 Zindagiasaan: Agri-Trade Intel")

# --- 2. SECURE KEY ---
# On Streamlit, we put the key in "Secrets"
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-3-flash-preview')

    # --- 3. INPUTS ---
    col1, col2 = st.columns(2)
    with col1:
        prod = st.selectbox("Product", ["Onions", "Potatoes", "Mangoes"])
        v26 = st.number_input("2026 Value (kUSD)", value=1200)
        v22 = st.number_input("2022 Value (kUSD)", value=450)
    
    if st.button("🚀 Generate Strategy"):
        with st.spinner("Scraping TIPP ID 305 & ITC Data..."):
            prompt = f"Analyze {prod} (HS 07/08). TIPP Proc 305. Growth ${v22}k to ${v26}k. English & Urdu."
            response = model.generate_content(prompt)
            
            # --- 4. OUTPUTS ---
            res = response.text
            if "---" in res:
                eng, urdu = res.split("---", 1)
                st.subheader("English Analysis")
                st.write(eng)
                st.divider()
                st.subheader("اردو رپورٹ")
                st.write(f"<div dir='rtl'>{urdu}</div>", unsafe_allow_html=True)
            else:
                st.write(res)
else:
    st.warning("Please enter your API Key in the sidebar to begin.")
