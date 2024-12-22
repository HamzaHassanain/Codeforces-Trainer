import sqlite3


conn = None
cur = None

ating = None


def drop_all_tables_of_db():
    cur = conn.cursor()

    sql = "DROP TABLE tasks"
    cur.execute(sql)

    conn.commit()


def insert(name, link, state, contestId, p_index):
    cur = conn.cursor()

    sql = "INSERT INTO tasks(name, link, state, contestId, p_index) VALUES(?, ?, ?, ?, ?)"
    cur.execute(sql, (name, link, state, contestId, p_index))

    conn.commit()


def load_tasks_table():
    cur = conn.cursor()
    sql = "SELECT * FROM tasks"
    cur.execute(sql)
    rows = cur.fetchall()
    return rows


def drop_column():
    cur = conn.cursor()

    sql = "ALTER TABLE tasks DROP COLUMN rating"
    cur.execute(sql)

    conn.commit()


def delete_row(id):
    cur = conn.cursor()

    sql = "DELETE FROM tasks WHERE id = ?"
    cur.execute(sql, (id,))

    conn.commit()


def get_row_by_problem_link(link):

    cur = conn.cursor()

    sql = "SELECT * FROM tasks WHERE link = ?"
    cur.execute(sql, (link,))
    row = cur.fetchone()

    conn.commit()

    return row


def close_connection():

    conn.close()


def delete_db():
    import os
    os.remove("db.db")


def create_db():
    global conn, cur
    import os
    os.system("touch db.db")

    conn = sqlite3.connect("db.db")

    cur = conn.cursor()
    sql = """CREATE TABLE tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            link TEXT,
            state TEXT,
            contestId INTEGER,
            p_index TEXT
            )"""
    cur.execute(sql)

    conn.commit()


def write_cft_to_sql():

    with open("db.cft", "r") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 5):
            name = lines[i].strip()
            if i+1 >= len(lines):
                break
            link = lines[i+1].strip()
            state = lines[i+2].strip()
            contestId = int(lines[i+3].strip())
            p_index = lines[i+4].strip()
            insert(name, link, state, contestId, p_index)
    conn.commit()


delete_db()
create_db()
