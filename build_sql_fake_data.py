import sqlite3
from random import randint
from mock_db import random_side, random_price
from datetime import datetime, timedelta
from time import time


def build_sql_fake_data(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    # creating table in database
    create_table = """CREATE TABLE IF NOT EXISTS orders 
                                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                  account_id INTEGER,
                                  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                                  side TEXT,
                                  price DECIMAL(3,2),
                                  size INTEGER);"""
    cursor.execute(create_table)
    conn.commit()
    date = datetime.strptime('2020-01-01', '%Y-%m-%d')
    for day in range(366):
        data_to_insert = create_random_data_for_single_day(date)
        sql_command =  """INSERT INTO orders
                                 (account_id, timestamp, side, price, size)
                                 VALUES (?, ?, ?, ?, ?);"""
        cursor.executemany(sql_command, data_to_insert)
        date += timedelta(days=1)
    conn.commit()
    conn.close()

def create_random_data_for_single_day(date: datetime.date, lines = 10000, number_of_account_ids =100):
    data_for_single_day = []
    seconds_to_increment = 86400 // lines
    time_inc = timedelta(hours=0, minutes=0, seconds=seconds_to_increment)
    line_date = date
    for line in range(lines):
        account_id = randint(0, number_of_account_ids)
        side = random_side()
        price = random_price(side)
        size = randint(0,6)
        data_for_single_day.append((account_id, str(line_date), side, price, size))
        line_date += time_inc
    return data_for_single_day



if __name__ == '__main__':
    DB_NAME = 'test.db'
    t1 = time()
    build_sql_fake_data(DB_NAME)
    print(f'SQL data build in {time()-t1}\nNumber of rows: 3660000\nDB name: {DB_NAME}')