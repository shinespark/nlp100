# -*- coding: UTF-8 -*-


def main():
    x = 'paraparaparadise'
    y = 'paragraph'

    X = set(char_n_gram(x, 2))
    Y = set(char_n_gram(y, 2))

    print(union(X, Y))
    print(diff(X, Y))
    print(product(X, Y))

    print('se' in X)
    print('se' in Y)


def char_n_gram(text, n):
    results = []
    for i in range(len(text) - n + 1):
        results.append(text[i:i+n])

    return results


def union(x, y):
    return x | y


def diff(x, y):
    return x - y


def product(x, y):
    return x ^ y


if __name__ == '__main__':
    main()
