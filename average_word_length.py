from itertools import count
from numpy import average


def fun1(sentence):
    for p in "!?',;.":
        sentence = sentence.replace(p, '')
    words = sentence.split(" ")
    total_length = 0
    for word in words:
        total_length = total_length + len(word)
    count_words = len(words)

    average_length = total_length / count_words
    print(average_length)

def fun2(sentence):
    for p in "!?',;.":
        sentence = sentence.replace(p, '')
    
    words = sentence.split()
    average_length = round(sum(len(word) for word in words)/len(words),2)
    print(average_length)

sentence = input("Enter the sentance")
fun2(sentence)
