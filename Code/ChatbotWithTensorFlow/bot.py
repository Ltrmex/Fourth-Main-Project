# Imports
import sqlite3
import json
from datetime import datetime

# Time frame for a training file
timeframe = '2011-08'
sql_transaction = []

# Connection with sqlite3
connection = sqlite3.connect('{}.db'.format(timeframe))
# Coursor connection
c = connection.coursor()

# Create a table
def create_table():
    # Query
    c.execute("""CREATE TABLE IF NOT EXIST parent_reply(parent_id TEXT PRIMARY KEY,
     comment_id TEXT UNIQUE, parent TEXT, comment TEXT, subreddit TEXT, unix INT, score INT)""")

if __name__ == "__main__":
    create_table()




