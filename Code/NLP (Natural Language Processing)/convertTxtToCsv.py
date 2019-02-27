import csv

file = open('C:/Users/Ltrmex/Desktop/Fourth-Main-Project/Code/NLP (Natural Language Processing)/sample.txt','r',errors = 'replace')

dictionary = {}
article = []
question = []
answer = []
difficultyQ = []
difficultyA = []
articleFile = []

file.close()


with open('output.csv', 'w') as f:
    w = csv.writer(f, delimiter=',')
    w.writerow(['Article', 'Question', 'Answer', 'DifficultyQ', 'DifficultyA', 'ArticleFile'])

    for Topic, Words in dictionary.items():
        for Word, Meaning, Sentence in Words:
            w.writerow([Topic, Word, Meaning, Sentence,])
            w.writerow('\n')
         
f.close()



