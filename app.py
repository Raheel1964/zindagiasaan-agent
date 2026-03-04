import streamlit as st
import google.generativeai as genai

# --- 1. CONFIG ---
st.set_page_config(page_title="Zindagiasaan Agent", layout="wide")
st.title("🌾 Zindagiasaan: Agri-Trade Intel")

# --- 2. SECURE KEY ---
# In Streamlit, the key is entered in the sidebar
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    # Using the 2026 stable model
    model = genai.GenerativeModel('gemini-3-flash-preview')

    # --- 3. INPUTS ---
    col1, col2 = st.columns(2)
    with col1:
        prod = st.selectbox("Product", ["Onions", "Potatoes", "Mangoes", "Tomatoes"])
        v26 = st.number_input("2026 Projected Value (kUSD)", value=1200)
        v22 = st.number_input("2022 Base Value (kUSD)", value=450)
    
    if st.button("🚀 Generate Strategy"):
        with st.spinner("Analyzing TIPP ID 305 & ITC Data..."):
            # The Prompt - Ensure no extra spaces at the start of these lines
            prompt = f"""
Act as the Zindagiasaan Lead Strategist. 
Analyze {prod} (HS Chapter 07/08/20).
Growth Stats: ${v22}k in 2022 to ${v26}k in 2026.

TASK:
1. Reference TIPP Procedure ID 305 for mandatory certificates (DPP/PSW).
2. Use ITC logic to identify 'Untapped Potential' in the EU market.
3. Pitch the ROI of Chapter 20 (Freeze-Drying) to reduce post-harvest waste.
4. Provide English analysis first, then '---', then a professional Urdu report.
"""
            try:
                response = model.generate_content(prompt)
                res = response.text
                
                # --- 4. OUTPUTS ---
                if "---" in res:
                    eng, urdu = res.split("---", 1)
                    st.subheader("English Strategic Analysis")
                    st.write(eng)
                    st.divider()
                    st.subheader("اردو برآمدی رپورٹ")
                    # RTL (Right-to-Left) formatting for Urdu
                    st.markdown(f"<div style='text-align: right; direction: rtl;'>{urdu}</div>", unsafe_allow_html=True)
                else:
                    st.write(res)
            except Exception as e:
                st.error(f"API Error: {str(e)}")
else:
    st.info("Please enter your Gemini API Key in the sidebar to activate the agent.")
