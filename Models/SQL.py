import sqlite3

class sql:
    def __init__(self):
        self.conn = sqlite3.connect("knjizara.db")