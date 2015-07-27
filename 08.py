# -*- coding: UTF-8 -*-


def cipher(str):
    new_str = ''
    for char in str:
        if char.isalpha() and char.islower():
            code = ord(char)
            new_code = 219 - code
            new_str += chr(new_code)
        else:
            new_str += char

    return new_str


print(cipher('abCd000'))
