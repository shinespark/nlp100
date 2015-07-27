# -*- coding: UTF-8 -*-


def char_n_gram(text, n):
    results = []
    for i in range(len(text) - n + 1):
        results.append(text[i:i+n])

    return results


def word_n_gram(text, n):
    word_list = text.split()
    results = []
    for i in range(len(word_list) - n + 1):
        results.append(word_list[i:i+n])

    return results


str = 'I am an NLPer'
for e in char_n_gram(str, 2):
    print(e)
for e in word_n_gram(str, 2):
    print(e)
