#!/usr/bin/python3
def multiple_returns(sentence):
    list_tup = []
    sen_tuple = ()
    slen = len(sentence)
    first_let = ""
    if slen == 0:
        first_let = None
        list_tup = [first_let, slen]
    else:
        list_tup = [sentence[0], slen]
    sen_tuple = tuple(list_tup)
    return (sen_tuple)
