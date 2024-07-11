import sqlite3

CONN = sqlite3.connect("db/runescape_items.db")
CURSOR = CONN.cursor()