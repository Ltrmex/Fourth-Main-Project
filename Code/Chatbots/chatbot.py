import re
import sqlite3
from collections import Counter
from string import punctuation
from math import sqrt
 
# Initialize the connection to the database
connection = sqlite3.connect('chatbot.sqlite')
cursor = connection.cursor()
 
# Create the tables needed by the program
createTable = [
    'CREATE TABLE words(word TEXT UNIQUE)',
    'CREATE TABLE sentences(sentence TEXT UNIQUE, used INT NOT NULL DEFAULT 0)',
    'CREATE TABLE associations (word_id INT NOT NULL, sentence_id INT NOT NULL, weight REAL NOT NULL)',]

for request in createTable:
    try:
        cursor.execute(request)
    except:
        pass
 
def getId(entityName, text):
    # Retrieve an entity's unique ID from the database, given its associated text.
    # If the row is not already present, it is inserted.
    # The entity can either be a sentence or a word.
    tableName = entityName + 's'
    columnName = entityName
    cursor.execute('SELECT rowid FROM ' + tableName + ' WHERE ' + columnName + ' = ?', (text,))
    row = cursor.fetchone()

    if row:
        return row[0]
    else:
        cursor.execute('INSERT INTO ' + tableName + ' (' + columnName + ') VALUES (?)', (text,))
        return cursor.lastrowid
 
def getWords(text):
    # Retrieve the words present in a given string of text.
    # The return value is a list of tuples where the first member is a lowercase word,
    # and the second member the number of time it is present in the text.
    wordsRegexpString = '(?:\w+|[' + re.escape(punctuation) + ']+)'
    wordsRegexp = re.compile(wordsRegexpString)
    wordsList = wordsRegexp.findall(text.lower())
    return Counter(wordsList).items()
 
 
bot = 'Hello!'
while True:
    # Output bot's message
    print('Bot: ' + bot)

    # Ask for user input; if blank line, exit the loop
    userInput = input('User Input: ').strip()

    if userInput == 'Goodbye':
        break

    # Store the association between the bot's message words and the user's response
    words = getWords(bot)
    words_length = sum([n * len(word) for word, n in words])
    sentence_id = getId('sentence', userInput)

    for word, n in words:
        word_id = getId('word', word)
        weight = sqrt(n / float(words_length))
        cursor.execute('INSERT INTO associations VALUES (?, ?, ?)', (word_id, sentence_id, weight))

    connection.commit()

    # Retrieve the most likely answer from the database
    cursor.execute('CREATE TEMPORARY TABLE results(sentence_id INT, sentence TEXT, weight REAL)')
    words = getWords(userInput)
    words_length = sum([n * len(word) for word, n in words])

    for word, n in words:
        weight = sqrt(n / float(words_length))
        cursor.execute('INSERT INTO results SELECT associations.sentence_id, sentences.sentence, ?*associations.weight/(4+sentences.used) FROM words INNER JOIN associations ON associations.word_id=words.rowid INNER JOIN sentences ON sentences.rowid=associations.sentence_id WHERE words.word=?', (weight, word,))

    # If matches were found, give the best one
    cursor.execute('SELECT sentence_id, sentence, SUM(weight) AS sum_weight FROM results GROUP BY sentence_id ORDER BY sum_weight DESC LIMIT 1')
    row = cursor.fetchone()
    cursor.execute('DROP TABLE results')

    # Otherwise, just randomly pick one of the least used sentences
    if row is None:
        cursor.execute('SELECT rowid, sentence FROM sentences WHERE used = (SELECT MIN(used) FROM sentences) ORDER BY RANDOM() LIMIT 1')
        row = cursor.fetchone()

    # Tell the database the sentence has been used once more, and prepare the sentence
    bot = row[1]
    cursor.execute('UPDATE sentences SET used=used+1 WHERE rowid=?', (row[0],))
    