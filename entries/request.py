import sqlite3
import json

from models import Entry 
from models import Mood

def get_all_entries():
    with sqlite3.connect("dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id,
            m.label mood_label 
        FROM Entry e
        JOIN Mood m
            ON m.id = e.mood_id 
        """
        )

        entries = []

        dataset= db_cursor.fetchall()

        for row in dataset:

            entry = Entry(row["id"], row["concept"], row["entry"], row["date"], row["mood_id"])

            mood = Mood(row["mood_id"], row["mood_label"])

            entry.mood = mood.__dict__

            entries.append(entry.__dict__)
        
        return json.dumps(entries)

def get_single_entry(id):
    with sqlite3.connect("dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id
            FROM entry as e
            WHERE e.id = ?
        """
        ,( id, ))

        data = db_cursor.fetchone()

        entry = Entry(data['id'], data['concept'], data['entry'], data['date'], data['mood_id'])

        return json.dumps(entry.__dict__)

def get_all_searched_entries(search_term):
    
    with sqlite3.connect("dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id
            FROM entry as e
            WHERE entry LIKE ?
        """,("%"+search_term+"%",)
        )

        entries = []

        dataset= db_cursor.fetchall()

        for row in dataset:

            entry = Entry(row["id"], row["concept"], row["entry"], row["date"], row["mood_id"])

            entries.append(entry.__dict__)
        
        return json.dumps(entries)

def delete_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM entry
        WHERE id = ?
        """,
        (id,))

