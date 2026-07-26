import streamlit as st
import uuid
from langchain_core.messages import HumanMessage, AIMessage
from src.agent.graph import build_financial_agent

# Styled corporate theme (Inter font, teal accents)
st.set_page_config(page_title="Financial AI Advisor", layout="wide")

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }
        .main-header {
            color: #1F2937;
            font-size: 2.2rem;
            font-weight: 700;
            border-bottom: 3px solid #14B8A6;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
        .stButton>button {
            background-color: #14B8A6;
            color: white;
            border-radius: 6px;
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-header'>LangGraph Financial AI Agent Portal</div>", unsafe_allow_html=True)

# Initialize Session state
if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "agent" not in st.session_state:
    st.session_state.agent = build_financial_agent()

# Load states
config = {"configurable": {"thread_id": st.session_state.thread_id}}
state_data = st.session_state.agent.get_state(config)

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Chat Assistant")
    
    # Display historical chat messages
    for msg in st.session_state.chat_history:
        if isinstance(msg, HumanMessage):
            st.chat_message("user").write(msg.content)
        else:
            st.chat_message("assistant").write(msg.content)
            
    user_input = st.chat_input("Enter your financial inquiry...")
    
    if user_input:
        st.chat_message("user").write(user_input)
        st.session_state.chat_history.append(HumanMessage(content=user_input))
        
        # Invoke agent
        inputs = {
            "messages": [HumanMessage(content=user_input)],
            "profile": {"risk_tolerance": "moderate"},
            "goals": []
        }
        
        res = st.session_state.agent.invoke(inputs, config)
        
        # Refresh state
        state_data = st.session_state.agent.get_state(config)

with col2:
    st.subheader("LangGraph State Inspect")
    st.info(f"Thread ID: {st.session_state.thread_id}")
    
    if state_data.next:
        st.warning(f"Interrupt Triggered: Next node is **{state_data.next[0]}**")
        st.write("This action requires verification before execution.")
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Approve Proposal"):
                # Resume execution with approved = True
                st.session_state.agent.update_state(config, {"approved": True}, as_node="human_approval")
                # Run graph again
                res = st.session_state.agent.invoke(None, config)
                st.session_state.chat_history.append(AIMessage(content="Adviser: Investment Proposal Approved and Logged."))
                st.rerun()
        with c2:
            if st.button("Reject Proposal"):
                st.session_state.agent.update_state(config, {"approved": False}, as_node="human_approval")
                res = st.session_state.agent.invoke(None, config)
                st.session_state.chat_history.append(AIMessage(content="Adviser: Investment Proposal Rejected."))
                st.rerun()
    else:
        st.success("State status: Ready / Idle")
        if state_data.values:
            st.write("**Current state values:**")
            st.write(state_data.values.get("profile", {}))
            st.write(state_data.values.get("goals", []))
""")
