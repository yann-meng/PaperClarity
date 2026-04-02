from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any

DB_PATH = Path("data/paperclarity.db")


class Database:
    def __init__(self, path: Path = DB_PATH):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(self.path)
        self.conn.row_factory = sqlite3.Row
        self._init_schema()

    def _init_schema(self) -> None:
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS documents (
                id TEXT PRIMARY KEY,
                payload TEXT NOT NULL
            )
            """
        )
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                document_id TEXT NOT NULL,
                skill_name TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        self.conn.commit()

    def save_document(self, document_id: str, payload: dict[str, Any]) -> None:
        self.conn.execute(
            "INSERT OR REPLACE INTO documents(id, payload) VALUES(?, ?)",
            (document_id, json.dumps(payload, ensure_ascii=False)),
        )
        self.conn.commit()

    def get_document(self, document_id: str) -> dict[str, Any] | None:
        row = self.conn.execute("SELECT payload FROM documents WHERE id = ?", (document_id,)).fetchone()
        return json.loads(row["payload"]) if row else None

    def save_note(self, document_id: str, skill_name: str, content: dict[str, Any]) -> int:
        cur = self.conn.execute(
            "INSERT INTO notes(document_id, skill_name, content) VALUES(?, ?, ?)",
            (document_id, skill_name, json.dumps(content, ensure_ascii=False)),
        )
        self.conn.commit()
        return int(cur.lastrowid)

    def list_notes(self, document_id: str) -> list[dict[str, Any]]:
        rows = self.conn.execute(
            "SELECT id, document_id, skill_name, content, created_at FROM notes WHERE document_id = ? ORDER BY id DESC",
            (document_id,),
        ).fetchall()
        return [
            {
                "id": row["id"],
                "document_id": row["document_id"],
                "skill_name": row["skill_name"],
                "content": json.loads(row["content"]),
                "created_at": row["created_at"],
            }
            for row in rows
        ]
