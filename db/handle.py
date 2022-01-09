import sqlite3


def create_tables():
    con = sqlite3.connect("trades.db")
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS trades (
                        trade_id TEXT PRIMARY KEY,
                        order_id TEXT,
                        pair TEXT,
                        executed TEXT,
                        direction_type TEXT,
                        order_type TEXT NOT NULL,
                        price REAL,
                        cost REAL,
                        fee REAL,
                        volume REAL
                   )''')

    con.commit()

    con.close()


def insert_new_trade(data):
    con = sqlite3.connect("trades.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    cur.execute('''INSERT INTO trades (trade_id, order_id, pair, executed, direction_type, order_type, price, cost, fee,
     volume) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', data)

    con.commit()

    con.close()

