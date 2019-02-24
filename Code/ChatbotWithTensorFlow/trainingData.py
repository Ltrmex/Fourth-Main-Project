# Imports
import sqlite3
import pandas as pd

timeframes = ['2014-03']

# Build a connection to read
for timeframe in timeframes:
    # Connection with sqlite3
    connection = sqlite3.connect('{}.db'.format(timeframe))
    # Coursor connection
    c = connection.cursor()
    # Sets limit (pull at time from db)
    limit = 5000
    # Helps buffer through database
    last_unix = 0
    # Tells when pulling is done
    cur_lenght = limit
    counter = 0
    # Tells when finish building tsting data
    test_done = False
    # checks if any rows and  keep pulling the data if cur_lenght is the same as limit
    while cur_lenght == limit:
        df = pd.read_sql("SELECT * FROM parent_reply WHERE unix > {} and parent NOT NULL and score > 0 ORDER BY unix ASC LIMIT {}".format(last_unix,limit),connection)
        # Last unix
        last_unix = df.tail(1)['unix'].values[0]
        # length od data frame
        cur_length = len(df)

        # Starts testing
        if not test_done:
            with open('test.from','a', encoding='utf8') as f:
                for content in df['parent'].values:
                    f.write(content+'\n')

            with open('test.to','a', encoding='utf8') as f:
                for content in df['comment'].values:
                    f.write(str(content)+'\n')

            test_done = True
            
            # Else if the test is done, train
        else:
            with open('train.from','a', encoding='utf8') as f:
                for content in df['parent'].values:
                    f.write(content+'\n')

            with open('train.to','a', encoding='utf8') as f:
                for content in df['comment'].values:
                    f.write(str(content)+'\n')
            
            counter += 1
            # Every 100000 rows completed print the output
            if counter % 20 == 0:
                print(counter*limit,'rows completed so far')
