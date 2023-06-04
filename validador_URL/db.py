import sqlite3

conect = sqlite3.connect("url.db")


db = conect.cursor()

db.execute('''
CREATE TABLE IF NOT EXISTS url_table(
    id INTEGER PRIMARY KEY,
    url TEXT
)
''')


def create(url):
    db.execute(f"INSERT INTO url_table(url) VALUES ('{url}')")
    conect.commit()


def remove(url):
    db.execute(f"DELETE FROM url_table WHERE url='{url}'")
    conect.commit()


def update(url):
    print("Batata Update")


def findAll():
    urls = []
    db.execute("SELECT * FROM url_table")
    rows = db.fetchall()
    if rows:
        for row in rows:
            urls.append(row[1])
    return urls
