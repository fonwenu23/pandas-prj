import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

cur.close()

