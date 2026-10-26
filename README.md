# Agentic AI IT Helpdesk Assistant

A small, research-inspired student prototype for an 8-mark Agentic AI case study.

## Research inspiration
LLexus: An AI Agent System for Incident Management (Microsoft Research, 2024):
https://www.microsoft.com/en-us/research/publication/llexus-an-ai-agent-system-for-incident-management/

This is an independent simplified prototype, not a reproduction of LLexus.

## Features
- Incident classification and priority assignment
- Tool selection and simulated diagnostics
- Local troubleshooting knowledge base
- SQLite incident ticket creation
- Visible action log and recent ticket table
- No API key required for the demo

## Run locally (Windows PowerShell)
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

If PowerShell blocks activation, use:
```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m streamlit run app.py
```

## Deploy
1. Push this folder to a GitHub repository.
2. Visit https://share.streamlit.io/
3. Create an app, select the repository and `app.py`.
4. Deploy.

## Limitations
Diagnostics are simulated. The prototype does not access or change real devices, accounts, or network equipment. The current decision workflow uses explicit rules and tools, not an autonomous LLM planner. Describe it accurately as a lightweight agentic-workflow prototype.
