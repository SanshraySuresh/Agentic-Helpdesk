import streamlit as st
from agent import run_agent
from database import init_db, list_tickets

st.set_page_config(page_title="Agentic IT Helpdesk", page_icon="🛠️", layout="wide")
init_db()

st.title("🛠️ Agentic AI IT Helpdesk Assistant")
st.caption("A research-inspired prototype based on agentic incident troubleshooting workflows.")
st.info("Demo mode: diagnostic checks and ticket actions are simulated. No real devices or accounts are changed.")

with st.sidebar:
    st.header("Try a sample issue")
    samples = {
        "Wi-Fi connected, no internet": "My laptop is connected to Wi-Fi, but I cannot access websites.",
        "Password reset": "I forgot my password and need to reset it.",
        "Printer issue": "The office printer is not responding.",
        "Software installation": "I cannot install the required software on my laptop.",
        "Unknown issue": "My computer is behaving strangely and I don't know why."
    }
    selected_sample = st.selectbox("Choose an example", list(samples.keys()))
    if st.button("Use example", use_container_width=True):
        st.session_state["issue_text"] = samples[selected_sample]

issue = st.text_area(
    "Describe the IT issue",
    key="issue_text",
    placeholder="Example: My laptop connects to Wi-Fi, but websites do not load.",
    height=110
)

if st.button("Analyze issue and create ticket", type="primary", use_container_width=True):
    if not issue.strip():
        st.warning("Please describe the issue first.")
    else:
        result = run_agent(issue.strip())
        st.session_state["last_result"] = result

result = st.session_state.get("last_result")
if result:
    st.divider()
    st.subheader("Agent result")
    a, b, c = st.columns(3)
    a.metric("Detected category", result["category"])
    b.metric("Priority", result["priority"])
    c.metric("Ticket ID", result["ticket_id"])

    st.markdown("### Troubleshooting recommendation")
    st.write(result["recommendation"])

    st.markdown("### Agent action log")
    for step in result["steps"]:
        st.write(f"✓ {step}")

    st.markdown("### Knowledge base evidence")
    st.write(result["knowledge"])

    st.caption("This prototype recommends actions only. Follow your organization's IT policies for real incidents.")

st.divider()
st.subheader("Recent simulated tickets")
tickets = list_tickets()
if tickets:
    st.dataframe(tickets, use_container_width=True, hide_index=True)
else:
    st.write("No tickets created yet. Submit an issue above to create the first ticket.")

st.caption("Case study inspiration: LLexus, *An AI Agent System for Incident Management* (Microsoft Research, 2024). This student prototype is not the LLexus implementation.")
