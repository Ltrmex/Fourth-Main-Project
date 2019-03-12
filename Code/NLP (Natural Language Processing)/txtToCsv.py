import csv, re
from nltk import sent_tokenize
from os import listdir
from os.path import isfile, join
def corpusDialogueData():
    mypath='C:/Users/Ltrmex/Desktop/Fourth-Main-Project/dialogues/'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    
    j = 1
    while j < len(onlyfiles):
        # 11, 212, 22, 253, 274
        filename = 'C:/Users/Ltrmex/Desktop/Fourth-Main-Project/dialogues/' + onlyfiles[j]
        file = open(filename, encoding="utf8")
        text = file.read()
        file.close()

        # define lists
        responses = []

        sentences = sent_tokenize(text)
        tag = 'horror'
        #tag = re.findall('([A-Z][a-z]+)', sentences[0])[0]
        question = sentences[0]

        i = 0
        while i < len(sentences):
            if i != 0:
                responses.append(sentences[i])
            i += 1

        with open('output.csv', 'a') as f:
            w = csv.writer(f, delimiter=',')
            if j == 1:
                w.writerow(['Tag', 'Question', 'Responses']) 
            w.writerow([tag, question,'-'.join(responses),])
            
        f.close()

        j += 1

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

# wikipediaData()
corpusDialogueData()