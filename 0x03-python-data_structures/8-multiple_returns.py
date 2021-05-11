#!/usr/bin/python3
def multiple_returns(sentence):
    len_sentence = len(sentence)
    if not sentence:
        return (len_sentence, None)
    result_tuple = tuple((len_sentence, sentence[0]))
    return (result_tuple)
