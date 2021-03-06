# Imports
import sqlite3
import json
from datetime import datetime

# Time frame for a training file
timeframe = '2014-03'
sql_transaction = []

# Connection with sqlite3
connection = sqlite3.connect('{}.db'.format(timeframe))
# Coursor connection
c = connection.cursor()

# Creates a table
def create_table():
    # Query
    c.execute("CREATE TABLE IF NOT EXISTS parent_reply(parent_id TEXT PRIMARY KEY, comment_id TEXT UNIQUE, parent TEXT, comment TEXT, subreddit TEXT, unix INT, score INT)")

def format_data(data):
    # Normalize data repleace a new line, return and ""
    data = data.replace('\n',' newlinechar ').replace('\r',' newlinechar ').replace('"',"'")
    return data

# Checks if data is acceptable( not longer then length of 50 or less then 1 in a single response)
def acceptable(data):
    if len(data.split(' ')) > 50 or len(data) < 1:
        return False
    # Checks if data is greater then 1000
    elif len(data) > 1000:
        return False
    # Checks if comment is deleted 
    elif data == '[deleted]':
        return False
    # Checks if comment is removed
    elif data == '[removed]':
        return False
    else:
        return True

def find_existing_score(pid):
    try:
        sql = "SELECT score FROM parent_reply WHERE parent_id = '{}' LIMIT 1".format(pid)
        c.execute(sql)
        result = c.fetchone()
        if result != None:
            # Only selecting from comment
            return result[0]
        else: return False
    # Error exception
    except Exception as e:
        #print(str(e))
        return False

# Find parent by parent id
def find_parent(pid):
    try:
        sql = "SELECT comment FROM parent_reply WHERE comment_id = '{}' LIMIT 1".format(pid)
        c.execute(sql)
        result = c.fetchone()
        if result != None:
            # Only selecting from comment
            return result[0]
        else: return False
    # Error exception
    except Exception as e:
        #print(str(e))
        return False

# Helper function which builds up insertion statements and commit them in groups, rather than one-by-on. (Quicker)
def transaction_bldr(sql):
    global sql_transaction
    # Keeps building transaction until it's of a certain size
    sql_transaction.append(sql)
    if len(sql_transaction) > 1000:
        # Starts the transaction
        c.execute('BEGIN TRANSACTION')
        for s in sql_transaction:
            try:
                c.execute(s)
            except:
                pass
        connection.commit()
        # Empty the transaction
        sql_transaction = []

def sql_insert_replace_comment(commentid,parentid,parent,comment,subreddit,time,score):
    try:
        sql = """UPDATE parent_reply SET parent_id = ?, comment_id = ?, parent = ?, comment = ?, subreddit = ?, unix = ?, score = ? WHERE parent_id =?;""".format(parentid, commentid, parent, comment, subreddit, int(time), score, parentid)
        transaction_bldr(sql)
    except Exception as e:
        print('s0 insertion',str(e))

def sql_insert_has_parent(commentid,parentid,parent,comment,subreddit,time,score):
    try:
        sql = """INSERT INTO parent_reply (parent_id, comment_id, parent, comment, subreddit, unix, score) VALUES ("{}","{}","{}","{}","{}",{},{});""".format(parentid, commentid, parent, comment, subreddit, int(time), score)
        transaction_bldr(sql)
    except Exception as e:
        print('s0 insertion',str(e))

def sql_insert_no_parent(commentid,parentid,comment,subreddit,time,score):
    try:
        sql = """INSERT INTO parent_reply (parent_id, comment_id, comment, subreddit, unix, score) VALUES ("{}","{}","{}","{}",{},{});""".format(parentid, commentid, comment, subreddit, int(time), score)
        transaction_bldr(sql)
    except Exception as e:
        print('s0 insertion',str(e))
   
if __name__ == '__main__':
    create_table()
    # Rows in a file
    row_counter = 0
    # Parent and child pairs
    paired_rows = 0

    # Opens a file
    with open("C:/Users/Kamilka/Year4/Traning_Data/{}/RC_{}".format(timeframe.split('-')[0], timeframe, ), buffering = 1000) as f:
        # Iterate through f
        for row in f:
            # Checks if data is printing
            # print(row)
            row_counter += 1
            # Loads the jason file which takes a string formatted like a json object
            row = json.loads(row)
            parent_id = row['parent_id']
            body = format_data(row['body'])
            created_utc = row['created_utc']
            score = row['score']
            comment_id = row['name']
            subreddit = row['subreddit']
            parent_data = find_parent(parent_id)

            # Set threshold if comments already exist
            if score >= 2:
                existing_comment_score = find_existing_score(parent_id)
                if existing_comment_score:
                    # Check if it's grater then insert data
                    if score > existing_comment_score:
                        # If comment is acceptable
                        if acceptable(body):
                            sql_insert_replace_comment(comment_id,parent_id,parent_data,body,subreddit,created_utc,score)
                            
                else:
                    # If comment is acceptable
                    if acceptable(body):
                        if parent_data:
                            sql_insert_has_parent(comment_id,parent_id,parent_data,body,subreddit,created_utc,score)
                            paired_rows += 1
                        else:
                            sql_insert_no_parent(comment_id,parent_id,body,subreddit,created_utc,score)
                            
            if row_counter % 100000 == 0:
                print('Total Rows Read: {}, Paired Rows: {}, Time: {}'.format(row_counter, paired_rows, str(datetime.now())))