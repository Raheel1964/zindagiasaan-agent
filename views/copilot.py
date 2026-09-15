import streamlit as st

def show():
    st.title("🤖 ZindagiAsaan AI Copilot")
    st.caption("Multilingual AI Assistant for Pakistani Agri-Exporters and Farmers")

    st.divider()

    # Initialize chat history in session state
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Assalam-o-Alaikum! I am your ZindagiAsaan Copilot. Ask me anything about crop export requirements, TIPP rules, or WeBOC registration."
            }
        ]

    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # React to user input
    if prompt := st.chat_input("Type your export or compliance question here..."):
        # Display user message in chat message container
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        # Simulated AI Response
        if "weboc" in prompt.lower() or "register" in prompt.lower():
            response = "To register on WeBOC for agri exports, you need: 1. Active NTN & Sales Tax Registration, 2. Bank Verification Letter, 3. Chamber of Commerce Membership, and 4. CNIC of the proprietor."
        elif "kinnow" in prompt.lower() or "orange" in prompt.lower():
            response = "Kinnow exports to the GCC (UAE/Saudi) require a Phytosanitary Certificate issued by the Department of Plant Protection (DPP) after cold-treatment verification (4°C-6°C)."
        else:
            response = f"Thank you for asking about: '{prompt}'. AgriAsaan Copilot provides automated compliance guidance based on TIPP regulatory tables and DPP guidelines."

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
