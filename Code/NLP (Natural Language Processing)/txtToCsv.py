import csv
from nltk import sent_tokenize
def corpusDialogueData():
    

def wikipediaData():
    # load text
    filename = 'C:/Users/Ltrmex/Desktop/Fourth-Main-Project/Code/NLP (Natural Language Processing)/sample.txt'
    file = open(filename, encoding="utf8")
    text = file.readlines()
    file.close()

    # define lists
    article = []
    question = []
    answer = []

    i=0
    while i < len(text):
        sentences = sent_tokenize(text[i])

        if i != 0:
            article.append(sentences[0])
            question.append(sentences[1])
            answer.append(sentences[2])

        i += 1

    with open('output.csv', 'w') as f:
        w = csv.writer(f, delimiter=',')
        w.writerow(['Article', 'Question', 'Answer'])

        i = 0
        while i < len(article):
            w.writerow([article[i], question[i], answer[i],])
            i += 1
        
    f.close()

    print "CSV saved!"


# wikipediaData()
# corpusDialogueData()