from tools import classify_issue, run_diagnostic, search_knowledge_base, create_ticket

def run_agent(issue: str) -> dict:
    """
    Small tool-using agent workflow:
    1) classify the incident,
    2) choose and run a simulated diagnostic,
    3) retrieve troubleshooting guidance,
    4) create a ticket,
    5) assemble a transparent action log.
    """
    category, priority = classify_issue(issue)
    steps = [f"Classified the report as '{category}' with {priority} priority."]

    diagnostic = run_diagnostic(category, issue)
    steps.append(f"Ran simulated diagnostic tool: {diagnostic['tool_name']}.")
    steps.append(f"Diagnostic result: {diagnostic['result']}.")

    knowledge = search_knowledge_base(category, issue)
    steps.append("Searched the local troubleshooting knowledge base.")

    recommendation = knowledge["solution"]
    if diagnostic["result"] == "Insufficient information":
        recommendation += " If these steps do not help, collect the exact error message and escalate to IT support."
    elif diagnostic["result"] == "Potential outage detected":
        recommendation += " Check whether other users are affected and escalate to the network team if the outage continues."

    ticket = create_ticket(issue, category, priority, recommendation, diagnostic["result"])
    steps.append(f"Created simulated incident ticket {ticket['ticket_id']}.")
    steps.append("Prepared the recommendation and recorded the action history.")

    return {
        "category": category,
        "priority": priority,
        "ticket_id": ticket["ticket_id"],
        "recommendation": recommendation,
        "knowledge": knowledge["evidence"],
        "steps": steps,
    }
