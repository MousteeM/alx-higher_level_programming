#!/usr/bin/python3

def multiple_returns(sentence):
    count = 0
    firstChar = sentence[0]
    if sentence == '':
        firstChar = None
    for i in range(len(sentence)):
        count += 1
    return (count, firstChar)
