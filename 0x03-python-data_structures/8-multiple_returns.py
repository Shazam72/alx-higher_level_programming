#!/usr/bin/python3
def multiple_returns(sentence):
    first_char = 'None'
    sentence_len = len(sentence)
    if (sentence_len > 0):
        first_char = sentence[0]
    return (sentence_len, first_char)
