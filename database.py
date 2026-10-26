import sqlite3
import os
from datetime import datetime
import uuid

DB_PATH = os.path.join(os.path.dirname(__file__), "tickets.db")

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                ticket_id TEXT PRIMARY KEY,
                created_at TEXT NOT NULL,
                issue TEXT NOT NULL,
                category TEXT NOT NULL,
                priority TEXT NOT NULL,
                recommendation TEXT NOT NULL,
                diagnostic_result TEXT NOT NULL,
                status TEXT NOT NULL
            )
        """)

def insert_ticket(issue, category, priority, recommendation, diagnostic_result):
    ticket_id = "INC-" + uuid.uuid4().hex[:6].upper()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with get_connection() as conn:
        conn.execute(
            """INSERT INTO tickets
            (ticket_id, created_at, issue, category, priority, recommendation, diagnostic_result, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (ticket_id, created_at, issue, category, priority, recommendation, diagnostic_result, "Open")
        )
    return {"ticket_id": ticket_id}

def list_tickets():
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT ticket_id AS 'Ticket ID', created_at AS 'Created At',
                   issue AS 'Issue', category AS 'Category', priority AS 'Priority',
                   diagnostic_result AS 'Diagnostic Result', status AS 'Status'
            FROM tickets ORDER BY created_at DESC LIMIT 20
        """).fetchall()
    import pandas as pd
    return pd.DataFrame(rows, columns=[
        "Ticket ID", "Created At", "Issue", "Category", "Priority", "Diagnostic Result", "Status"
    ])
