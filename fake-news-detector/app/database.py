# app/database.py

import sqlite3
from datetime import datetime

# Initialize database (SQLite for simplicity)
def init_db():
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            prediction TEXT NOT NULL,
            probability REAL NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_article(text, prediction, probability):
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO articles (text, prediction, probability, timestamp) VALUES (?, ?, ?, ?)",
                   (text, prediction, probability, datetime.now()))
    conn.commit()
    conn.close()

def get_recent_articles(limit=10):
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()
    cursor.execute("SELECT text, prediction, probability, timestamp FROM articles ORDER BY id DESC LIMIT ?", (limit,))
    articles = cursor.fetchall()
    conn.close()
    return articles
