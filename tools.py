import json
import os
from database import insert_ticket

KB_PATH = os.path.join(os.path.dirname(__file__), "knowledge_base.json")

def classify_issue(issue: str):
    text = issue.lower()
    rules = [
        (["wifi", "wi-fi", "internet", "network", "website", "connection"], "Network", "High"),
        (["password", "login", "sign in", "locked out", "account"], "Account Access", "Medium"),
        (["printer", "printing", "print"], "Printer", "Low"),
        (["install", "installation", "software", "application", "app won't open"], "Software", "Medium"),
        (["slow", "freezing", "crash", "blue screen"], "Performance", "Medium"),
    ]
    for keywords, category, priority in rules:
        if any(word in text for word in keywords):
            return category, priority
    return "General IT", "Medium"

def run_diagnostic(category: str, issue: str) -> dict:
    """Simulated diagnostic tool; does not inspect or modify the real computer."""
    text = issue.lower()
    if category == "Network":
        if any(word in text for word in ["outage", "everyone", "whole office", "all users"]):
            result = "Potential outage detected"
        else:
            result = "Simulated check: connection issue reported; gateway and DNS checks recommended"
        return {"tool_name": "network_diagnostic", "result": result}
    if category == "Account Access":
        return {"tool_name": "account_help_check", "result": "Password/account assistance required; identity verification must be completed by IT"}
    if category == "Printer":
        return {"tool_name": "printer_status_check", "result": "Simulated printer status: check power, paper, queue, and network connection"}
    if category == "Software":
        return {"tool_name": "software_install_check", "result": "Simulated check: verify permissions, available storage, and installer error"}
    if category == "Performance":
        return {"tool_name": "performance_check", "result": "Simulated check: review CPU/memory usage and recent error messages"}
    return {"tool_name": "general_triage", "result": "Insufficient information"}

def search_knowledge_base(category: str, issue: str) -> dict:
    with open(KB_PATH, "r", encoding="utf-8") as f:
        articles = json.load(f)
    article = next((a for a in articles if a["category"] == category), None)
    if article is None:
        article = next(a for a in articles if a["category"] == "General IT")
    return {"evidence": article["title"] + ": " + article["steps"], "solution": article["steps"]}

def create_ticket(issue, category, priority, recommendation, diagnostic_result):
    return insert_ticket(issue, category, priority, recommendation, diagnostic_result)
