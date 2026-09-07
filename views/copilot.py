import streamlit as st

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
