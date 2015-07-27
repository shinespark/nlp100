# -*- coding: UTF-8 -*-


import random


def typoglycemia(text):
    text_list = text.split(' ')
    new_text = ''
    for word in text_list:
        if len(word) <= 4:
            new_text += word
            new_text += ' '
            continue

        word_list = list(word)

        new_text += word_list.pop(0)
        end_letter = word_list.pop()

        new_text += ''.join(sorted(word_list, key=lambda k: random.random()))
        new_text += end_letter
        new_text += ' '

    new_text.rstrip()
    return new_text


print(typoglycemia('test'))
print(typoglycemia('test2'))
print(typoglycemia("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))
