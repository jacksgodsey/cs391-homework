import sqlite3

class SQLiteModel:
    def __init__(self, db_name="charities.db"):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS charities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    address TEXT,
                    service_type TEXT,
                    phone TEXT,
                    hours TEXT,
                    reviews TEXT
                )
            """)
            conn.commit()

    def insert(self, name, description, address, service_type, phone, hours, reviews):
        with sqlite3.connect(self.db_name) as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO charities (name, description, address, service_type, phone, hours, reviews)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (name, description, address, service_type, phone, hours, reviews))
            conn.commit()

    def get_all(self):
        with sqlite3.connect(self.db_name) as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM charities")
            return cur.fetchall()
